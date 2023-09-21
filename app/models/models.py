# Author: Su
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base  # 创建模型继承的父类
from sqlalchemy.dialects.mysql import BIGINT, TEXT, DATETIME, VARCHAR, TINYINT  # 导入字段类型
from sqlalchemy import Column, ForeignKey, text  # 定义字段
from werkzeug.security import check_password_hash # 检查密码
from sqlalchemy.orm import relationship   # 导入外键


# 创建父类
Base = declarative_base()
metadata = Base.metadata


# 创建消息保存模型
class Msg(Base):
    __tablename__ = 'msg'  # 指定表名称
    id = Column(BIGINT, primary_key=True)  # 编号，自动递增
    content = Column(TEXT)  # 内容
    createdAt = Column(DATETIME, nullable=False)  # 创建时间
    updatedAt = Column(DATETIME, nullable=False)  # 修改时间


# 创建用户模型
class User(Base):
    __tablename__ = "user"  # 指定表名称
    id = Column(BIGINT, primary_key=True)  # 编号
    name = Column(VARCHAR(20), nullable=False, unique=True)  # 昵称
    pwd = Column(VARCHAR(255), nullable=False)  # 密码
    email = Column(VARCHAR(100), nullable=False, unique=True)  # 邮箱
    phone = Column(VARCHAR(11), nullable=False, unique=True)  # 手机
    sex = Column(TINYINT, nullable=True)  # 性别    1-男  2-女   3-保密
    face = Column(VARCHAR(100), nullable=True)  # 头像
    info = Column(VARCHAR(600), nullable=True)  # 介绍
    status = Column(TINYINT,nullable=False,default=0)   # 登录状态检测   0-未登录  1-登录
    createdAt = Column(DATETIME, nullable=False)  # 创建时间
    updatedAt = Column(DATETIME, nullable=False)  # 修改时间

    # 验证密码
    def check_pwd(self,pwd):
        return check_password_hash(self.pwd,pwd)

# 创建验证码模型
class Yzm(Base):
    __tablename__="Yzm"
    id = Column(BIGINT, primary_key=True)  # 编号，自动递增
    email = Column(VARCHAR(100), nullable=False, unique=True)  # 邮箱
    code = Column(VARCHAR(5), nullable=True)  # 验证码


# 创建好友模型（不是很好有冗余）
class Friends(Base):
    __tablename__ = "Friends"  # 指定表名称
    id = Column(BIGINT, primary_key=True,autoincrement=True)  # 编号
    user_id = Column(BIGINT, ForeignKey('user.id'), nullable=False)  # 使用编号
    friend_id = Column(BIGINT, ForeignKey('user.id'), nullable=False) # 使用编号
    notes = Column(VARCHAR(20))  # 好友备注
    createdAt = Column(DATETIME, nullable=False)  # 创建时间
    # 添加外键关联
    user = relationship("User", foreign_keys=[user_id])
    friend = relationship("User", foreign_keys=[friend_id])

# 创建好友申请模型
class Apply_Friends(Base):
    __tablename__ = "Apply_Friends"  # 指定表名称
    id = Column(BIGINT, primary_key=True,autoincrement=True)  # 编号
    user_id = Column(BIGINT, ForeignKey('user.id'), nullable=False)  # 使用编号
    friend_id = Column(BIGINT, ForeignKey('user.id'), nullable=False) # 使用编号
    info = Column(VARCHAR(100), nullable=True)  # 申请内容
    status = Column(VARCHAR(10),nullable=True)   # 申请好友状态检测   Accept-接受  Refuse-拒绝 Reviewing-审核中
    createdAt = Column(DATETIME, nullable=False)  # 创建时间
    updatedAt = Column(DATETIME, nullable=False)  # 修改时间

    # 添加外键关联
    user = relationship("User", foreign_keys=[user_id])
    friend = relationship("User", foreign_keys=[friend_id])

# 创建好友聊天消息模型
class Friends_Messages(Base):
    __tablename__ = "Friends_Messages"
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    sender_id = Column(BIGINT, ForeignKey('user.id'), nullable=False)
    receiver_id = Column(BIGINT, ForeignKey('user.id'), nullable=False)
    content = Column(TEXT, nullable=False)
    createdAt = Column(DATETIME, nullable=False)  # 创建时间
    # 添加外键关联
    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])


if __name__ == '__main__':
    import mysql.connector  # 导入数据库连接驱动
    from sqlalchemy import create_engine  # 创建连接引擎
    from app.configs import mysql_configs

    # 创建连接引擎,连接地址、编码、是否输出日志
    # 连接格式:'数据库系统名称+连接驱动名称://用户:密码@主机:端口/数据库名称?指定字符集
    engine = create_engine(
        'mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8'.format(**mysql_configs),
        echo=True
    )

    # 元类映射到数据库中去，即创建数据库对应表
    metadata.create_all(engine)

    # 修改表时使用
    # from sqlalchemy.orm import sessionmaker
    # from sqlalchemy.sql import text
    # Session = sessionmaker(bind=engine)
    # session = Session()
    #
    # # 添加 status 列
    # alter_query = text("ALTER TABLE friends ADD COLUMN notes VARCHAR(20)")
    # session.execute(alter_query)
    # session.commit()
    #
    # # 关闭会话
    # session.close()