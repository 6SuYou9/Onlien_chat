# Author: Su
# -*- coding: utf-8 -*-
import json

import tornado.web
from app.models.crud import CRUD


class CommonHandler(tornado.web.RequestHandler):
    # 客户端发送的参数
    @property
    def params(self):
        data = self.request.arguments
        data = {
            k: list(
                map(
                    lambda val: str(val, encoding="utf-8"),
                    v
                )
            )
            for k, v in data.items()
        }
        return data

    # 返回登录账号名
    @property
    def name(self):
        return self.get_secure_cookie("name", None)

    # 返回用户信息
    @property
    def user(self):
        return CRUD.name_user(self.name)

    # 返回头像
    def get_face(self,id):
        return CRUD.id_user(id).face

    # 返回登录用户id
    @property
    def id(self):
        return CRUD.name_id(self.name)

    # 返回好友申请(我发出的和我收到的)  num-1 查询我发出的   0 查询我收到的
    def applyfriend(self, num):
        applys = []
        if num == 1:     #  发出的好友申请
            datas = CRUD.get_sendapplyfriend(self.id)
            for i in datas:
                apply = {}
                send_friend = CRUD.id_user(i.friend_id)
                apply['friend_name'] = send_friend.name
                apply['friend_face'] = send_friend.face
                apply['info'] = i.info
                apply['status'] = i.status
                applys.append(apply)
                # print("发出的好友申请",apply)
                # print(i.user_id,i.friend_id,i.info,i.status)
        else:       #  收到的好友申请
            datas = CRUD.get_receapplyfriend(self.id)
            for i in datas:
                apply = {}
                rece_friend = CRUD.id_user(i.user_id)
                apply['friend_name'] = rece_friend.name
                apply['friend_face'] = rece_friend.face
                apply['info'] = i.info
                apply['status'] = i.status
                applys.append(apply)
                # print("收到的好友申请",apply)
                # print(i.user_id,i.friend_id,i.info,i.status)
        return applys

    # 获取好友列表
    @property
    def friends(self):
        return CRUD.get_friends(self.name)

    # 验证是不是好友
    def check_isfriends(self,friend_id):
        friend_name = CRUD.id_name(friend_id)
        # print("check_isfriends",self.name,friend_name,friend_id)
        return CRUD.check_isfriends(self.name,friend_name)

    @property
    def get_MessageBoard(self):
        data = CRUD.get_messageboard()
        result = []
        for v in data:
            result.append(json.loads(v.message))
            # print(type((json.loads(v.message))['user_id']))
            # print(type(self.id))
        return dict(data=result)
