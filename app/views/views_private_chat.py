# Author: Su
# -*- coding: utf-8 -*-

from app.views.views_common import CommonHandler

class PrivateChatHandler(CommonHandler):

    def prepare(self):
        if not self.name:
            self.redirect("/login.html")

    def get(self):
        data = dict(
            title="SuYou-Online_Chat",
            friend_id = self.get_argument("friend_id", "0")
        )
        self.render('privatechat.html', data=data)
