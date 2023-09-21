# Author: Su
# -*- coding: utf-8 -*-
import os  # 文件目录操作模块

# 常用配置
# 调试模式：开发者模式，debug=true
# 模板路径：template_path
# 静态文件路径：static_path
# 开启防跨站伪装登录，xsrf_cookies=True
# 密钥，cookie_sercet="xxxxxxxxxxx"

# 获取当前文件所在目录
root_path = os.path.dirname(__file__)

# 站点配置
configs = dict(
    debug=True,
    template_path=os.path.join(root_path, "templates"),
    static_path=os.path.join(root_path, "static"),
    xsrf_cookies=True,
    cookie_secret="b24219a98c844ae383b969b034eb2f69"
)

# 数据库连接配置
mysql_configs = dict(
    db_host="127.0.0.1",
    db_name="chatroom",
    db_port=3306,
    db_user="root",
    db_pwd="123456"
)

# 邮件服务登录配置
email = {
    'uname':'su_you_world@qq.com',
    'pwd':'xivfgetaznlogegh'
}

