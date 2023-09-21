# Author: Su
# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.forms import LoginForm
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD

class LoginHandler(CommonHandler):
    # 若已经登录，有cookie，则无需再次登录
    def prepare(self):
        if self.name:
            self.redirect("/groupchat.html")   # 直接跳转到聊天室

    def get(self):
        data = dict(
            title="登录页面"
        )
        self.render("login.html",data=data)

    def post(self):
        form = LoginForm(MultiDict(self.params))
        res=dict(code=0)
        if form.validate():
            status = CRUD.get_login_status(form.data['name'])
            # print(f"views_login.py---------用户{form.data['name']}登录状态为：{status}")
            if status == 0:        # 该账号未登录，可以进行登录操作
                self.set_secure_cookie("name", form.data['name'])      # 设置一个cookie来识别用户登录
                CRUD.change_login_status(form.data['name'], 1)
                res['code'] = 1
            elif status == 1:          # 该账号已经登录
                res['code'] = 6
        else:
            res = form.errors
            res["code"] = 0
        self.write(res) # 指定的内容 res 写入 HTTP 响应的正文部分，以便将其返回给客户端。


