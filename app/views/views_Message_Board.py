# Author: Su
# -*- coding: utf-8 -*-
import datetime
import json

from app.views.views_common import CommonHandler
from app.models.crud import CRUD


class Message_BoardHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True

    def prepare(self):
        if not self.user:
            self.redirect("/login.html")


    def get(self):
        messages = (self.get_MessageBoard)['data']
        # print(messages)
        data = dict(
            title="留言板",
            messages=messages
        )
        self.render("messageboard.html", data=data)

    def post(self):
        res = dict(code=0)
        data = {}

        # 获取所有参数名
        post_arguments = self.request.arguments
        # 遍历参数名，获取参数值
        for key in post_arguments:
            values = self.get_arguments(key)
            # 如果只有一个值，直接取第一个值
            if len(values) == 1:
                data[key] = values[0]
            # 如果有多个值，保存为列表
            else:
                data[key] = values
        if not data['content']:
            self.write(res)
            return
        # print(data)
        data['dt'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(type(data)) # dict
        # print(data)
        sender_id = int(data['user_id'])
        message = json.dumps(data)  # 将字典序列化为json
        if CRUD.save_messageboard(sender_id,message):
            res['code'] = 1
            res['data'] = message
        else:
            res['code'] = 2
        self.write(res)

