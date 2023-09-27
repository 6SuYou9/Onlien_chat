# Author: Su
# -*- coding: utf-8 -*-

import mysql.connector # 导入数据连接驱动
from sqlalchemy import create_engine # 导入创建引擎工具
from sqlalchemy.orm import sessionmaker # 会话创建工具
from app.configs import mysql_configs # mysql配置

#  专门用于创建会话类
class ORM:
    @staticmethod
    def db():
        # 创建连接引擎
        engine = create_engine(
            'mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8'.format(
                **mysql_configs),
            echo=False,
            pool_size=100,   # 连接池中的连接数,这有助于提高并发访问性能。
            pool_recycle=10, # 接池中的连接重用时间。设置 10 秒，表示连接在闲置 10 秒后将被重新使用，这有助于避免连接资源的浪费。
            connect_args={'charset':"utf8"}  # 连接参数。设置字符集为 UTF-8，以确保支持中文等特殊字符的存储和检索
        )
        # 创建会话
        Session = sessionmaker(
            bind=engine,
            autocommit=False,  # 在会话中关闭自动提交。在处理数据库操作时，显式调用 commit() 方法来提交更改。这有助于确保事务的完整性，只有在所有操作都成功后才提交更改。
            autoflush=True, # 自动刷新。在会话中启用自动刷新，以确保会话中的对象与数据库保持同步。
            expire_on_commit=False  # 在会话提交后使对象过期。
        )
        return Session()