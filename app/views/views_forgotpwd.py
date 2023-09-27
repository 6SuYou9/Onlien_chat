# Author: Su
# -*- coding: utf-8 -*-
import random
from app.views.views_common import CommonHandler
from app.tools.forms import ForgotPwdForm2
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD

class FogotPwdHandler(CommonHandler):
    # 若已经登录则无法到忘记密码页面
    def prepare(self):
        if self.name:
            self.redirect("/groupchat.html")   # 直接跳转到聊天室

    def get(self):
        data = dict(
            title="找回密码"
        )
        self.render("forgotpwd.html", data=data)

    def post(self):
        # 验证客户端提交参数
        form = ForgotPwdForm2(MultiDict(self.params))
        res = dict(code=0)
        code = self.get_body_argument('yanzheng_code',"")
        if code:
            db_code = CRUD.get_code(self.get_body_argument('email'))
        if form.validate():
            if code == db_code:
                # 确保昵称，邮箱，电话均为同一用户信息，防止某一用户使用自己邮箱修改其他用户信息
                if CRUD.check_one_user(form):
                    CRUD.save_forgotpwd_user(form)
                    CRUD.save_code(self.get_body_argument('email'), random.randint(10000,99999)) # 确保每次登录使用的都是新的验证码
                    res['code'] = 1
                else:
                    CRUD.save_code(self.get_body_argument('email'), random.randint(10000,99999)) # 确保每次登录使用的都是新的验证码
                    res['code'] = 8
            else:
                res['code'] = 9
        else:
            res = form.errors
            res['code'] = 0
        self.write(res)
