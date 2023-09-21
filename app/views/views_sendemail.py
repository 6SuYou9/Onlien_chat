# Author: Su
# -*- coding: utf-8 -*-
import random
from app.configs import email
from app.views.views_common import CommonHandler
from app.tools.send_emails import Send_Mail
from app.models.crud import CRUD
from app.tools.forms import ForgotPwdForm1
from werkzeug.datastructures import MultiDict


class SendEmailHandler(CommonHandler):
    # 产生邮箱验证码
    def generate_code(self, user_email):
        yanzhen_code = str(random.randint(1000, 9999))
        # 将验证码保存到数据库中
        CRUD.save_code(user_email, yanzhen_code)
        return yanzhen_code

    # 发送邮件的接口
    def post(self):
        res = dict(code=0)
        user_email = self.get_body_argument('email')  # 获取前端form输入框中输入的邮箱
        form = ForgotPwdForm1(MultiDict(self.params))
        # 跳过yanzheng_code的验证，因为这里才开始获取验证码
        if form.validate():
            try:
                # 确保昵称，邮箱，电话均为同一用户信息，防止某一用户使用自己邮箱修改其他用户信息
                if CRUD.check_one_user(form):
                    print(user_email, "11111111111111111111111111")
                    msg = f'您好，您正在使用{user_email}验证<SuYou-Online_Chat>用户，修改账号密码，您的验证码为{self.generate_code(user_email)},如果不是本人操作，请忽略'
                    Send_Mail(email.get('uname'), email.get('pwd'), user_email, '<SuYou-Online_Chat>用户修改密码', msg)
                    res['code'] = 1
                else:
                    res['code'] = 8
            except Exception as e:
                print("views_sendemail----------------------------post报错\n", e)
        else:
            res = form.errors
            res['code'] = 0
        self.write(res)