# Author: Su
# -*- coding: utf-8 -*-

from app.views.views_common import CommonHandler
from app.tools.forms import UserEditForm
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD

# 聊天视图,RequestHandler封装请求和响应所有操作
class UserprofileHandler(CommonHandler):
    # 若未登录，跳转登录页面
    def prepare(self):
        if not self.user:
            self.redirect("/login.html")
    # get时返回
    def get(self):
        data = dict(
            title="个人界面",
            user=self.user
        )
        self.render('userprofile.html', data=data)
    # post时返回
    def post(self):
        formdata = MultiDict(self.params)
        common_user = self.user
        form = UserEditForm(formdata,common_user)
        res = dict(code=0)
        # 用户什么都没有修改，返回错误响应
        if form.data['name'] == common_user.name and form.data['phone'] == common_user.phone and form.data['email'] == common_user.email and form.data['sex'] == common_user.sex and form.data['info'] == common_user.info:
            res['code'] = 10
            self.write(res)
            return
        if form.validate():
            if not form.data['sex']:
                form.data['sex'] = 3
            #     若修改了昵称，则需要重新登录
            if form.data['name'] != common_user.name:
                res['code'] = 11
                CRUD.change_login_status(common_user.name, 0)  # 将数据库中的登录状态设置为退出
                self.clear_cookie("name")  # 清除cookie
            #     否则不需要重新登录
            else:
                res['code'] = 12
            if CRUD.save_user(form):
                res['data'] = form.data

        else:
            res = form.errors
            res['code'] = 0
        self.write(res)