# Author: Su
# -*- coding: utf-8 -*-

from sockjs.tornado import SockJSRouter                                             # 聊天室
from app.views.views_group_chat import ChatHandler as chat                          # 聊天室界面
from app.views.views_regist import RegistHandler as regist                          # 注册
from app.views.views_login import LoginHandler as login                             # 登录
from app.views.views_userprofile import UserprofileHandler as userprofile           # 个人信息
from app.views.views_logout import LogoutHandler as logout                          # 退出登录逻辑
from app.views.views_uploadface import UploadFaceHandler as uploadface              # 上传头像
from app.views.views_group_chatroom import ChatRoomHandler as chatroom              # 群聊逻辑处理
from app.views.views_forgotpwd import FogotPwdHandler as forgotpwd                  # 忘记密码
from app.views.views_sendemail import SendEmailHandler as sendemail                 # 忘记密码发送邮箱验证逻辑
from app.views.views_msg import MSGHandler as msg                                   # 获取历史聊天信息
from app.views.views_addfriend import AddFriendHandler as addfriend                 # 添加好友
from app.views.views_showapply import ShowApplyHandler as showapply                 # 展示好友申请，审批界面，处理好友申请逻辑
from app.views.views_private_chat import PrivateChatHandler as privatechat_html     # 私聊页面
from app.views.views_getlatestmsg import GetLatestMsgHandler as getlatestmsg        # 获取最新聊天消息
from app.views.views_private_chatroom import PrivateChatRoomHandler as privatechat  # 私聊逻辑处理
<<<<<<< HEAD
from app.views.views_Message_Board import Message_BoardHandler as messageboard      # 留言板逻辑处理
=======
>>>>>>> e877903b4bedbd5f4027d1196ff845c640b957e9



# 路由视图映射:(路由地址，视图)
urls = [
<<<<<<< HEAD
        (r"/", login),                         # 登录界面
        (r"/regist.html", regist),            # 注册界面
        (r"/forgotpwd.html", forgotpwd),      # 忘记密码界面
        (r"/login.html", login),              # 登录界面
        (r"/addfriend.html", addfriend),      # 添加好友界面
        (r"/showapply.html", showapply),      # 展示好友申请界面
        (r"/userprofile.html", userprofile),  # 个人信息界面
        (r"/groupchat.html", chat),              # 聊天室界面
        (r"/privatechat.html", privatechat_html),  # 私聊界面
        (r"/messageboard.html", messageboard),  # 留言板界面
        (r'/websocket', privatechat),             # 私聊处理
        (r"/get_latest_message", getlatestmsg), # 获取最新好友聊天消息
        (r"/logout/", logout),                # 退出登录
        (r"/msg/", msg),                      # 获取历史聊天信息
        (r"/uploadface/", uploadface),        # 上传头像
        (r"/sendemail/", sendemail),          # 发送邮件
=======
           (r"/", login),                         # 登录界面
           (r"/regist.html", regist),            # 注册界面
           (r"/forgotpwd.html", forgotpwd),      # 忘记密码界面
           (r"/login.html", login),              # 登录界面
           (r"/addfriend.html", addfriend),      # 添加好友界面
           (r"/showapply.html", showapply),      # 展示好友申请界面
           (r"/userprofile.html", userprofile),  # 个人信息界面
           (r"/groupchat.html", chat),              # 聊天室界面
           (r"/privatechat.html", privatechat_html),  # 私聊界面
           (r'/websocket', privatechat),             # 私聊处理
           (r"/get_latest_message", getlatestmsg), # 获取最新好友聊天消息
           (r"/logout/", logout),                # 退出登录
           (r"/msg/", msg),                      # 获取历史聊天信息
           (r"/uploadface/", uploadface),        # 上传头像
           (r"/sendemail/", sendemail),          # 发送邮件
>>>>>>> e877903b4bedbd5f4027d1196ff845c640b957e9
       ] + SockJSRouter(chatroom, "/chatroom").urls
