# Author: Su
# -*- coding: utf-8 -*-
import datetime
from app.tools.orm import ORM
<<<<<<< HEAD
from app.models.models import User, Msg, Yzm, Friends, Friends_Messages, Apply_Friends,Message_board
=======
from app.models.models import User, Msg, Yzm, Friends, Friends_Messages, Apply_Friends
>>>>>>> e877903b4bedbd5f4027d1196ff845c640b957e9
from werkzeug.security import generate_password_hash
from sqlalchemy import and_, or_


def dt():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 增删改查的类
class CRUD(object):

    # 验证用户的唯一性，1昵称，2邮箱，3手机
    @staticmethod
    def user_unique(data, method=1):
        # 1.调用会话
        session = ORM.db()
        user = None
        # 2.查询逻辑，事务处理
        try:
            # 执行增删改查
            model = session.query(User)
            if method == 1:
                # 验证昵称
                user = model.filter_by(name=data).first()
            if method == 2:
                # 验证邮箱
                user = model.filter_by(email=data).first()
            if method == 3:
                # 验证手机号
                user = model.filter_by(phone=data).first()
        except Exception as e:
            print("crud.py--------user_unique 报错\n", e)
            # 发生异常回滚
            session.rollback()
        else:
            # 没有发生异常提交
            session.commit()
        finally:
            # 无论是否发生异常，关闭会话
            session.close()
        return user

    # 保存注册用户
    @staticmethod
    def save_regist_user(form):
        session = ORM.db()
        result = False
        try:
            user = User(
                name=form.data['name'],
                pwd=generate_password_hash(form.data['pwd']),
                email=form.data['email'],
                phone=form.data['phone'],
                sex=None,
                face=None,
                info=None,
                createdAt=dt(),
                updatedAt=dt()
            )
            session.add(user)
            result = True
        except Exception as e:
            print("crud.py--------save_regist_user 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return result

    # 保存忘记密码用户
    @staticmethod
    def save_forgotpwd_user(form):
        session = ORM.db()
        result = None
        try:
            result = session.query(User).filter_by(name=form.data['name']).first()
            result.pwd = generate_password_hash(form.data['pwd'])
            result.updatedAt = dt()
        except Exception as e:
            print("crud.py--------save_forgotpwd_user 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 检测登录
    @staticmethod
    def check_login(name, pwd):
        session = ORM.db()
        result = False
        try:
            user = session.query(User).filter_by(name=name).first()
            if user:
                if user.check_pwd(pwd):
                    result = True
        except Exception as e:
            print("crud.py--------check_login 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return result

    # 更改登录状态
    @staticmethod
    def change_login_status(name, status=0):
        session = ORM.db()
        try:
            record = session.query(User).filter_by(name=name).first()
            record.status = status
            # print("更改登录状态为：",name,record.status)
        except Exception as e:
            print("crud.py--------change_login_status 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 获取登录状态
    @staticmethod
    def get_login_status(name):
        session = ORM.db()
        status = None  # 0  1
        try:
            status = session.query(User).filter_by(name=name).first().status
            # print("获取到的登录状态为：",name,status)
        except Exception as e:
            print("crud.py--------get_login_status 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return status

    # 根据昵称查询用户
    @staticmethod
    def name_user(name):
        session = ORM.db()
        user = None
        try:
            user = session.query(User).filter_by(name=name).first()
        except Exception as e:
            print("crud.py--------name_user 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return user

    # 根据id查询用户
    @staticmethod
    def id_user(id):
        session = ORM.db()
        user = None
        try:
            user = session.query(User).filter_by(id=id).first()
        except Exception as e:
            print("crud.py--------id_user 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return user

    # 根据昵称查询id
    @staticmethod
    def name_id(name):
        session = ORM.db()
        id = None
        try:
            id = session.query(User).filter_by(name=name).first().id
        except Exception as e:
            print("crud.py--------name_id 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return id

    # 根据id查询昵称
    @staticmethod
    def id_name(id):
        session = ORM.db()
        name = None
        try:
            name = session.query(User).filter_by(id=id).first().name
        except Exception as e:
            print("crud.py--------id_name 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return name

    # 保存好友申请
    @staticmethod
    def save_applyfriend(user_name, friend_name, info="", num=0):
        session = ORM.db()
        record = None
        try:
            # 第一次申请保存好友申请，或被拒绝后再次申请
            if num == 0:
                user_id = CRUD.name_id(user_name)
                friend_id = CRUD.name_id(friend_name)
                record = session.query(Apply_Friends).filter(and_(Apply_Friends.user_id == user_id, Apply_Friends.friend_id == friend_id)).first()
                if record:
                    record.info = info
                    record.status = "Reviewing"
                    print("更新好友申请")
                else:
                    apply = Apply_Friends(
                        user_id=user_id,
                        friend_id=CRUD.name_id(friend_name),
                        info=info,
                        status="Reviewing",
                        createdAt=dt(),
                        updatedAt=dt()
                    )
                    print("新增好友申请")
                    session.add(apply)
            else:
                # 修改好友申请状态为Accept
                if num == 1:
                    status = "Accept"
                else:
                    status = "Refuse"
                user_id = CRUD.name_id(user_name)
                friend_id = CRUD.name_id(friend_name)
                friend_record1 = session.query(Apply_Friends).filter(
                    and_(Apply_Friends.friend_id == user_id, Apply_Friends.user_id == friend_id)).first()
                friend_record2 = session.query(Apply_Friends).filter(
                    and_(Apply_Friends.friend_id == friend_id, Apply_Friends.user_id == friend_id)).first()
                if friend_record1:
                    friend_record1.status = status
                    friend_record1.updatedAt = dt()
                    if friend_record2:
                        friend_record2.status = status
                        friend_record2.updatedAt = dt()
        except Exception as e:
            print("crud.py--------save_applyfriend 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 保存好友
    @staticmethod
    def save_friend(user_name, friend_name, note=None):
        session = ORM.db()
        try:
            user_id = CRUD.name_id(user_name)
            friend_id = CRUD.name_id(friend_name)
            record = session.query(Friends).filter(
                and_(Friends.user_id == user_id, Friends.friend_id == friend_id)).first()
            if not record:
                friend_note = session.query(Friends).filter_by(user_id=user_id).first()
                if note:
                    friend_note.note = note
                else:
                    friend1 = Friends(
                        user_id=user_id,
                        friend_id=friend_id,
                        createdAt=dt(),
                    )
                    friend2 = Friends(
                        user_id=friend_id,
                        friend_id=user_id,
                        createdAt=dt(),
                    )
                    session.add(friend1)
                    session.add(friend2)
        except Exception as e:
            print("crud.py--------save_friend 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 删除好友
    @staticmethod
    def delete_friend(user_id, friend_id):
        session = ORM.db()
        try:
            record = session.query(Friends).filter(
                and_(Friends.user_id == user_id, Friends.friend_id == friend_id)
            ).first()
            if record:
                # 删除好友记录
                session.delete(record)
            else:
                # 如果记录不存在，可以执行其他操作，例如抛出异常或返回错误信息
                session.close()
                return False
        except Exception as e:
            print("crud.py--------delete_friend 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 获取好友列表
    @staticmethod
    def get_friends(user_name):
        session = ORM.db()
        friends = []
        try:
            user_id = CRUD.name_id(user_name)
            records = session.query(Friends).filter(Friends.user_id == user_id).order_by(
                Friends.createdAt.desc()).limit(100).all()
            for record in records:
                friend = CRUD.id_user(record.friend_id)
                friends.append(friend)
        except Exception as e:
            print("crud.py--------get_friends 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return friends

    # 检查是否已经是好友
    @staticmethod
    def check_isfriends(user_name, friend_name):
        session = ORM.db()
        result = False
        try:
            user_id = CRUD.name_id(user_name)
            friend_id = CRUD.name_id(friend_name)
            # print(user_id, friend_id)
            record1 = session.query(Friends).filter(
                and_(Friends.user_id == user_id, Friends.friend_id == friend_id)).first()
            record2 = session.query(Friends).filter(
                and_(Friends.user_id == friend_id, Friends.friend_id == user_id)).first()
            if record1 and record2:
                result = True
        except Exception as e:
            print("crud.py--------check_isfriends 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        # print(result)
        return result

    # 查询发出的好友申请
    @staticmethod
    def get_sendapplyfriend(user_id):
        session = ORM.db()
        data = None
        try:
            data = session.query(Apply_Friends).filter(Apply_Friends.user_id == user_id).order_by(
                Apply_Friends.createdAt.desc()).limit(100).all()
        except Exception as e:
            print("crud.py--------get_sendapplyfriend 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return data

    # 查询收到的好友申请
    @staticmethod
    def get_receapplyfriend(user_id):
        session = ORM.db()
        data = []
        try:
            data = session.query(Apply_Friends).filter(Apply_Friends.friend_id == user_id).order_by(
                Apply_Friends.createdAt.desc()).limit(100).all()
        except Exception as e:
            print("crud.py--------get_receapplyfriend 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        # print("get_receapplyfriend:",data)
        return data

    # 保存用户数据
    @staticmethod
    def save_user(form):
        session = ORM.db()
        try:
            user = session.query(User).filter_by(id=form.data['id']).first()
            user.name = form.data['name']
            user.email = form.data['email']
            user.phone = form.data['phone']
            if form.data['sex'] == None:
                user.sex = 3
            else:
                user.sex = int(form.data['sex'])
            user.info = form.data['info']
            user.updatedAt = dt()
        except Exception as e:
            print("crud.py--------save_user 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 保存用户头像
    @staticmethod
    def save_user_face(id, face):
        session = ORM.db()
        try:
            user = session.query(User).filter_by(id=id).first()
            user.face = face
            user.updatedAt = dt()
        except Exception as e:
            print("crud.py--------save_user_face 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 保存消息
    @staticmethod
    def save_msg(content):
        session = ORM.db()
        try:
            msg = Msg(
                content=content,
                createdAt=dt(),
                updatedAt=dt()
            )
            session.add(msg)
        except Exception as e:
            print("crud.py--------save_msg 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 加载消息
    @staticmethod
    def lastest_msg():
        session = ORM.db()
        data = []
        try:
            data = session.query(Msg).order_by(Msg.createdAt.desc()).limit(100).all()
        except Exception as e:
            print("crud.py--------lastest_msg 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return data

    # 保存私聊消息
    @staticmethod
    def save_private_msg(sender_id, friend_id, content):
        session = ORM.db()
        try:
            record = session.query(Friends).filter(
                and_(
                    and_(Friends.user_id == sender_id, Friends.friend_id == friend_id),
                    and_(Friends.user_id == friend_id, Friends.friend_id == sender_id)
                ))
            if record:
                msg = Friends_Messages(
                    sender_id=sender_id,
                    receiver_id=friend_id,
                    content=content,
                    createdAt=dt()
                )
                session.add(msg)
            else:
                content['content'] = "咱们已经不是好友了，你死心吧。"
                msg = Friends_Messages(
                    sender_id=friend_id,
                    receiver_id=sender_id,
                    content=content,
                    createdAt=dt()
                )
                session.add(msg)
        except Exception as e:
            print("crud.py--------save_private_msg 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 加载私聊消息
    @staticmethod
    def lastest_private_msg(sender_id, friend_id):
        session = ORM.db()
        data = []
        try:
            data = session.query(Friends_Messages).filter(
                or_(
                    and_(Friends_Messages.sender_id == sender_id, Friends_Messages.receiver_id == friend_id),
                    and_(Friends_Messages.sender_id == friend_id, Friends_Messages.receiver_id == sender_id)
                )
            ).order_by(Friends_Messages.createdAt.desc()).limit(100).all()
        except Exception as e:
            print("crud.py--------lastest_private_msg 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return data

    # 加载最新一条私聊消息
    @staticmethod
    def lastestone_private_msg(sender_id, receiver_id):
        session = ORM.db()
        data = []
        try:
            data = session.query(Friends_Messages).filter(
                and_(Friends_Messages.sender_id == sender_id, Friends_Messages.receiver_id == receiver_id),
            ).order_by(Friends_Messages.createdAt.desc()).first()
        except Exception as e:
            print("crud.py--------lastestone_private_msg 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return data

    # 保存邮箱与对应验证码
    @staticmethod
    def save_code(email, code):
        session = ORM.db()
        try:
            if session.query(User).filter_by(email=email).first():
                yzm = Yzm(
                    email=email,
                    code=code
                )
                record = session.query(Yzm).filter_by(email=email).first()
                if record:
                    record.code = code
        except Exception as e:
            print("crud.py--------save_code 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return True

    # 获取验证码
    @staticmethod
    def get_code(email):
        session = ORM.db()
        code = None
        try:
            code = session.query(Yzm).filter_by(email=email).first()
        except Exception as e:
            print("crud.py--------get_code 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return code.code

    # 验证信息都是同一用户
    @staticmethod
    def check_one_user(form):
        session = ORM.db()
        id1 = None
        id2 = None
        id3 = None
        result = False
        try:
            id1 = session.query(User).filter_by(name=form.data['name']).first().id
            id2 = session.query(User).filter_by(email=form.data['email']).first().id
            id3 = session.query(User).filter_by(phone=form.data['phone']).first().id
            if id1 == id2 == id3:
                result = True
        except Exception as e:
            print("crud.py--------check_one_user 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return result
<<<<<<< HEAD

    # 保存留言板消息
    @staticmethod
    def save_messageboard(id,content):
        session = ORM.db()
        result = False
        try:
            # 获取当前日期
            today = datetime.datetime.now().date()
            today_start = datetime.datetime.combine(today, datetime.datetime.min.time())
            # 检查是否同一天内已经存在具有相同id的记录
            existing_msg = session.query(Message_board).filter(
                and_(
                    Message_board.sender_id == id,
                    Message_board.createdAt >= today_start
                )
            ).first()
            if not existing_msg:
                msg = Message_board(
                    sender_id=id,
                    message=content,
                    createdAt=dt(),
                    updatedAt=dt()
                )
                session.add(msg)
                result = True
        except Exception as e:
            print("crud.py--------save_messageboard 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return result

    # 获取留言板消息
    @staticmethod
    def get_messageboard():
        session = ORM.db()
        data = []
        try:
            data = session.query(Message_board).order_by(Message_board.createdAt.desc()).limit(100).all()
        except Exception as e:
            print("crud.py--------get_messageboard 报错\n", e)
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return data
=======
>>>>>>> e877903b4bedbd5f4027d1196ff845c640b957e9
