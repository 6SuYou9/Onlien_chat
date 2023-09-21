# Author: Su
# -*- coding: utf-8 -*-

from app.views.views_common import CommonHandler

# 聊天视图,RequestHandler封装请求和响应所有操作
class ChatHandler(CommonHandler):

    def prepare(self):
        if not self.name:
            self.redirect("/login.html")

    def get(self):
        data = dict(
            title="SuYou-Online_Chat"
        )
        self.render('groupchat.html',data=data)
