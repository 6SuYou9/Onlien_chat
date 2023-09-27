# Author: Su
# -*- coding: utf-8 -*-
from app.views.views_common import CommonHandler
from app.tools.forms import RegistForm
from werkzeug.datastructures import MultiDict
from app.models.crud import CRUD

class RegistHandler(CommonHandler):
    # 若已经登录，有cookie，则无需再次登录
    def prepare(self):
        if self.name:
            self.redirect("/groupchat.html")  # 直接跳转到聊天室

    def get(self):
        data = dict(
            title="注册页面"
        )
        self.render("regist.html", data=data)

    # 通过post提交
    def post(self):
        # 验证客户端提交参数
        form = RegistForm(MultiDict(self.params))
        # print(form)
        res = dict(code=0)
        if form.validate():
            # 验证通过
            if CRUD.save_regist_user(form):
                res['code'] = 1
        else:
            res = form.errors
            res['code'] = 0
        # 返回json格式数据
        self.write(res)
