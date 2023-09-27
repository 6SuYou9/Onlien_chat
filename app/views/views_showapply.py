# Author: Su
# -*- coding: utf-8 -*-

from app.views.views_common import CommonHandler
from app.models.crud import CRUD

class ShowApplyHandler(CommonHandler):
    def check_xsrf_cookie(self):
        return True
    # 跳转
    def prepare(self):
        if not self.name:
            self.redirect("/login.html")

    def get(self):
        data = dict(
            title="审批好友申请",
            send_applys=self.applyfriend(1),
            rece_applys=self.applyfriend(0)
        )
        self.render('showapply.html', data=data)

    # 处理申请
    def post(self):
        res = dict(code=0)
        way = self.get_body_argument("way")
        # 处理好友申请
        if way=='Apply':
            friend_name = self.get_body_argument("friendname")
            flag = int(self.get_body_argument("num"))
            # print(friend_name,flag)
            if flag == 1:  # 同意好友申请
                CRUD.save_friend(self.name, friend_name)
                CRUD.save_applyfriend(self.name, friend_name,num=1)
                res['code'] = 1
            elif flag == 2:  # 拒绝好友申请
                CRUD.save_applyfriend(self.name, friend_name,num=2)
                res['code'] = 1
            self.write(res)
        # 处理删除好友
        elif way=='Delete':
            friend_id = self.get_body_argument("friend_id")
            if CRUD.delete_friend(self.id,friend_id):
                res['code'] = 2   # 删除好友成功
            else:
                res['code'] = 3
            self.write(res)