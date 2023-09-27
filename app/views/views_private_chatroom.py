# Author: Su
# -*- coding: utf-8 -*-

import datetime
import json
import traceback    # 找报错的时候用到了的
import tornado.websocket
from app.models.crud import CRUD
from app.views.views_common import CommonHandler

# 处理私聊
class PrivateChatRoomHandler(tornado.websocket.WebSocketHandler,CommonHandler):
    # 存储客户端连接
    clients = set()
    users = {}
    def check_origin(self, origin):
        return True  # 允许WebSocket的跨域请求

    def open(self):
        # 在连接建立时将连接对象添加到 clients 集合中
        # print("PrivateChatRoomHandler------------------open\n")
        self.clients.add(self)
        user_id = self.id
        if user_id not in self.users:
            self.users[user_id] = self
            # print(self)
        # print(self.users)

    def on_message(self, message):
        try:
            # 处理消息
            # print("PrivateChatRoomHandler-------on_message\n")
            data = json.loads(message)  # 将json字符串反序列化为字典
            # receiver_id = data["recipient"]
            data['dt'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sender_id = int(data['user_id'])
            receiver_id = int(data['friend_id'])
            content = json.dumps(data)  # 将字典序列化为json
            if sender_id in self.users or receiver_id in self.users:
                if data['code'] == 2:
                    if sender_id in self.users:
                        sender = self.users[sender_id]
                        sender.write_message(content)
                    if receiver_id in self.users:
                        receiver = self.users[receiver_id]
                        receiver.write_message(content)
                    # print(str(sender_id)+"给"+"========="+str(receiver_id)+"广播消息啦")
                    # print(content)
                    CRUD.save_private_msg(sender_id, receiver_id, content)
        except Exception as e:
            print("PrivateChatRoomHandler-------on_message报错\n", e)
            # traceback.print_exc()

    def on_close(self):
        # 在连接关闭时将连接对象从 clients 集合中移除
        try:
            self.clients.remove(self)
            del self.users[self.id]
        except Exception as e:
            print("PrivateChatRoomHandler-------on_close\n",e)

