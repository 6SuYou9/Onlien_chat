# Author: Su
# -*- coding: utf-8 -*-

from app.views.views_common import CommonHandler
from app.models.crud import CRUD

class LogoutHandler(CommonHandler):
    # 若用户未登录，则不可退出，访问该url跳转登录页面
    def prepare(self):
        if not self.name:
            self.redirect("/login.html")

    def get(self):
        CRUD.change_login_status(self.name, 0)   # 将数据库中的登录状态设置为退出
        self.clear_cookie("name")         # 清除cookie
        self.redirect("/login.html")   # 退出后跳转登录页面
