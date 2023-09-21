# Author: Su
# -*- coding: utf-8 -*-

from wtforms import Form  # 导入父类
from wtforms.fields import StringField, PasswordField, IntegerField  # 导入字段类型
from wtforms.validators import DataRequired, Regexp, Email, EqualTo, ValidationError  # 导入验证器
from app.models.crud import CRUD
from app.views.views_common import CommonHandler


# 注册表单验证
class RegistForm(Form):
    name = StringField(
        "昵称",
        validators=[
            DataRequired(u"昵称不能为空!")
        ]
    )
    pwd = PasswordField(
        "密码",
        validators=[
            DataRequired(u"密码不能为空!")
        ]
    )
    repwd = PasswordField(
        "确认密码",
        validators=[
            DataRequired(u"确认密码不能为空!"),
            EqualTo("pwd", message="两次输入密码不一致!")
        ]
    )
    phone = StringField(
        "手机号",
        validators=[
            DataRequired(u"手机号不能为空!"),
            Regexp("1[3456789]\\d{9}", message="手机号格式不正确!")

        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired(u"邮箱不能为空!"),
            Email(message="邮箱格式不正确!")
        ]
    )

    # 自定义验证昵称
    def validate_name(self, field):
        data = CRUD.user_unique(field.data)
        if data:
            raise ValidationError("昵称已经存在了!")

    # 自定义验证邮箱
    def validate_email(self, field):
        data = CRUD.user_unique(field.data, 2)
        if data:
            raise ValidationError("邮箱已经存在了!")

    # 自定义验证手机号
    def validate_phone(self, field):
        data = CRUD.user_unique(field.data, 3)
        if data:
            raise ValidationError("手机号已经存在了!")


# 登录表单验证
class LoginForm(Form):
    name = StringField(
        "账号",
        validators=[
            DataRequired("账号不能为空!")
        ]
    )
    pwd = PasswordField(
        "密码",
        validators=[
            DataRequired("密码不能为空!")
        ]
    )

    def validate_name(self, field):
        data = CRUD.user_unique(field.data)
        if not data:
            raise ValidationError("请先注册!")

    def validate_pwd(self, field):
        print("forms.py-----------LoginForm---validate_pwd", self.name.data, field.data)
        if not CRUD.check_login(self.name.data, field.data):
            raise ValidationError("密码错误!请重试!")


# 编辑个人信息
# 编号、昵称、手机、邮箱、头像、个性签名、性别
class UserEditForm(Form):
    def __init__(self, formdata, common_user):
        super().__init__(formdata)
        self.user = common_user

    id = IntegerField(
        "编号",
        validators=[
            DataRequired("编号不能为空!")
        ]
    )
    name = StringField(
        "昵称",
        validators=[
            DataRequired("昵称不能为空!")
        ]
    )
    phone = StringField(
        "手机号",
        validators=[
            DataRequired(u"手机号不能为空!"),
            Regexp("1[3456789]\\d{9}", message="手机号格式不正确!")

        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired(u"邮箱不能为空!"),
            Email(message="邮箱格式不正确!")
        ]
    )
    face = StringField(
        "头像",
        validators=[]
    )
    info = StringField(
        "个性签名",
        validators=[]
    )
    sex = IntegerField(
        "性别",
        validators=[]
    )

    # 自定义验证昵称
    def validate_name(self, field):
        # print(self.user.name)
        data = CRUD.user_unique(field.data)
        if data:
            if self.user.id!=data.id:
                raise ValidationError("昵称已经存在了!不能和其他用户一样哦!")

    # 自定义验证邮箱
    def validate_email(self, field):
        data = CRUD.user_unique(field.data, 2)
        if data:
            if self.user.id!=data.id:
                raise ValidationError("邮箱已经存在了!不能和其他用户一样哦!")

    # 自定义验证手机号
    def validate_phone(self, field):
        data = CRUD.user_unique(field.data, 3)
        if data:
            if self.user.id!=data.id:
                raise ValidationError("手机号已经存在了!不能和其他用户一样哦!")


# 忘记密码1表单验证(不验证验证码)
class ForgotPwdForm1(Form):
    name = StringField(
        "昵称",
        validators=[
            DataRequired(u"昵称不能为空!")
        ]
    )
    pwd = PasswordField(
        "密码",
        validators=[
            DataRequired(u"密码不能为空!")
        ]
    )
    repwd = PasswordField(
        "确认密码",
        validators=[
            DataRequired(u"确认密码不能为空!"),
            EqualTo("pwd", message="两次输入密码不一致!")
        ]
    )
    phone = StringField(
        "手机号",
        validators=[
            DataRequired(u"手机号不能为空!"),
            Regexp("1[3456789]\\d{9}", message="手机号格式不正确!")

        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired(u"邮箱不能为空!"),
            Email(message="邮箱格式不正确!")
        ]
    )

    # 自定义验证昵称
    def validate_name(self, field):
        data = CRUD.user_unique(field.data)
        if not data:
            raise ValidationError("该昵称用户不存在!")

    # 自定义验证邮箱
    def validate_email(self, field):
        data = CRUD.user_unique(field.data, 2)
        if not data:
            raise ValidationError("该邮箱用户不存在!")

    # 自定义验证手机号
    def validate_phone(self, field):
        data = CRUD.user_unique(field.data, 3)
        if not data:
            raise ValidationError("该手机号用户不存在!")

# 忘记密码2表单验证
class ForgotPwdForm2(Form):
    name = StringField(
        "昵称",
        validators=[
            DataRequired(u"昵称不能为空!")
        ]
    )
    pwd = PasswordField(
        "密码",
        validators=[
            DataRequired(u"密码不能为空!")
        ]
    )
    repwd = PasswordField(
        "确认密码",
        validators=[
            DataRequired(u"确认密码不能为空!"),
            EqualTo("pwd", message="两次输入密码不一致!")
        ]
    )
    phone = StringField(
        "手机号",
        validators=[
            DataRequired(u"手机号不能为空!"),
            Regexp("1[3456789]\\d{9}", message="手机号格式不正确!")

        ]
    )
    email = StringField(
        "邮箱",
        validators=[
            DataRequired(u"邮箱不能为空!"),
            Email(message="邮箱格式不正确!")
        ]
    )
    yanzheng_code = StringField(
        "验证码",
        validators=[
            DataRequired(u"验证码不能为空!")
        ]
    )

    # 自定义验证昵称
    def validate_name(self, field):
        data = CRUD.user_unique(field.data)
        if not data:
            raise ValidationError("该昵称用户不存在!")

    # 自定义验证邮箱
    def validate_email(self, field):
        data = CRUD.user_unique(field.data, 2)
        if not data:
            raise ValidationError("该邮箱用户不存在!")

    # 自定义验证手机号
    def validate_phone(self, field):
        data = CRUD.user_unique(field.data, 3)
        if not data:
            raise ValidationError("该手机号用户不存在!")


# 添加好友表单验证
class AddFriendForm(Form):
    name = StringField(
        "昵称",
        validators=[
            DataRequired(u"昵称不能为空!")
        ]
    )

    # 自定义验证昵称
    def validate_name(self, field):
        data = CRUD.user_unique(field.data)
        if not data:
            raise ValidationError("该昵称用户不存在!")
