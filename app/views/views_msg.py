# Author: Su
# -*- coding: utf-8 -*-
import json
from app.views.views_common import CommonHandler
from app.models.crud import CRUD


# 展示历史聊天信息
class MSGHandler(CommonHandler):

    def check_xsrf_cookie(self):
        return True

    def post(self):
        friend_id = self.get_body_argument('friend_id')
        if friend_id=="0":   # 没有选择好友进行聊天
            res = dict(code=1)
            self.write(res)
        else:
            if friend_id=="#":   # 进入了聊天室
                data = CRUD.lastest_msg()
                # print("这是群聊")
            else:    # friend_id为好友id，显示与好友的聊天
                data = CRUD.lastest_private_msg(self.id,friend_id)
                # print("这是私聊")
            result = []
            for v in data:
                result.append(json.loads(v.content))
            self.write(dict(data=result[::-1]))
