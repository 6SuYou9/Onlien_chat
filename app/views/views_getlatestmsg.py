# Author: Su
# -*- coding: utf-8 -*-

import json
import re
from app.views.views_common import CommonHandler
from app.models.crud import CRUD

class GetLatestMsgHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True

    def get(self):
        # 获取请求参数 friend_id 和 handler_id
        friend_id = self.get_argument('friend_id')
        handler_id = self.get_argument('handler_id')

        # 根据 friend_id 和 handler_id 获取最新消息
        message = CRUD.lastestone_private_msg(friend_id, handler_id)
        if message:
            # 请根据实际需求进行相应的查询和处理
            latest_message = self.get_latestone_msg(message)
            latest_message_id = self.get_message_id(message)
            # print("GetLatestMsgHandler:",latest_message_id,latest_message)

            # 返回最新消息作为文本数据
            self.write(json.dumps({'latestMessage': latest_message,'latest_message_id':latest_message_id}))

        # 获取与好友的最新消息
    def get_latestone_msg(self, message):
            # print(message.content)
            msg = json.loads(message.content).get('content', '')  # 使用 get 方法以防止键不存在时出错
            # print(msg)
            # 去除msg中的标签
            clean = re.compile('<.*?>')
            msg = re.sub(clean, '', msg)
            return msg

    # 获取消息的唯一标识符
    def get_message_id(self, message):
        id = message.id
        return id