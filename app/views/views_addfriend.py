# Author: Su
# -*- coding: utf-8 -*-

from app.views.views_common import CommonHandler
from app.tools.forms import AddFriendForm
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD

class AddFriendHandler(CommonHandler):
    # 若无登录，则跳转登录界面
    def prepare(self):
        if not self.user:
            self.redirect("/login.html")

    def get(self):
        data = dict(
            title="添加好友"
        )
        self.render("addfriend.html", data=data)

    def post(self):
        # 验证客户端提交参数
        form = AddFriendForm(MultiDict(self.params))
        res = dict(code=0)
        user_name = (self.name).decode('utf-8')  # 使用 'utf-8' 解码字节序列
        friend_name = form.data['name']
        result = CRUD.check_isfriends(user_name, friend_name)
        if self.get_body_argument('name') == user_name:      # 如果添加自己，则返回错误code 7
            res['code'] = 7
        elif result:          #   已经是好友
            res['code'] = 5
        elif form.validate():
            info = self.get_argument("info", default="交个朋友吧!")
            # print("views_addfirend---------------\n",info)
            # print(user_name, form.data['name'],info)
            CRUD.save_applyfriend(user_name, friend_name,info=info)
            # print("好友申请保存成功")
            res['code'] = 1
        else:
            res = form.errors
            res['code'] = 0
            # 返回json格式数据
        # print(res)
        self.write(res)
