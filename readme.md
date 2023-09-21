# 1.安装依赖包

- 第一种方式安装,到pypi.org去拉取 
  - pip install -r requirements.txt
- 第二种方式安装,到国内豆瓣镜像源拉取 
  - pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

使用到的依赖包如下：

- tornado:服务器端web框架
- mysql-connector-python:mysql数据库连接驱动
- sqlalchemy:数据库模型ORM
- sockjs-tornado:websocket通信库
- wtforms:表单验证库
- werkzeug:wsgi工具箱,主要用加密机制
- Pillow:用来检验图片

# 2.构建项目目录

- main.py	#   入口启动文件,启动服务
- app 	#   存放MTV的包
  - _init_.py	#   初始化模块,自定义应用
  - configs.py	#   配置信息模块
  - urls.py	#   路由模块
  - params.py	#   公共参数模块
  - models	#   模型包
    - _init__py	#   初始化模块
    - crud.py	#   增删改查操作模块
    - models.py	#   数据表模型模块
  - templates	#   模板目录
    - layout.html	#   公共布局模板
    - regist.html	#   会员注册模板
    - login.html	#   会员登录模板
    - userprofile.html	#   会员中心模板
    - chat.html	#   聊天室模板
  - views	#	视图包
    - __init__.py	#	初始化模板
      - views_regist.py	#	注册视图模块
      - views_login.py	#	登录视图模块
      - views_logout.py	#	退出视图模块
      - views_userprofile.py	#	修改个人资料视图模块
      - views_uploads.py	#	上传头像视图模块
      - views_user.py	#	会员权限控制视图模块
      - views_common.py	#	公共视图模块
      - views_chat.py	#	聊天室视图模块
      - views_chatroom.py 	#	websocket全双工通信视图模块
      - views_msg.py	#	获取历史消息视图模块
  - static	#	静态资源目录
    - css	#	存放层叠样式表
    - dist	#	存放bootstrap依赖文件
    - images	#	存放图片
    - js	#	存放客户端脚本
      - group_chat.js	#	websocket聊天
      - request.js	#	ajax请求服务器端
      - upload.js	#	上传图片文件
    - pages	#	原始模板目录
    - ue	#	ueditor编辑器
    - uploads	#	上传图片保存目录
  - tools	#	工具包
    - init_.py	#	初始化模板
    - forms.py	#	表单验证模块
    - orm.py	#	数据库连接驱动模块