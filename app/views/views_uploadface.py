# Author: Su
# -*- coding: utf-8 -*-
import io
import os
import datetime
import uuid
from app.views.views_common import CommonHandler
from app.models.crud import CRUD
from PIL import Image  # 导入Pillow库 判断上传文件是否是图片


# 上传头像
class UploadFaceHandler(CommonHandler):
    # 开启跨站伪装登录的防护，是tornado的一种安全机制
    def check_xsrf_cookie(self):
        return True

    # post时返回
    def post(self):
        # 指定保存目录
        upload_path = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)), "static\\uploads"  # 拼接目录 在当前目录的上一级目录的static/uploads目录下
        )
        # 判断目录是否存在,不存在创建
        if not os.path.exists(upload_path):
            os.mkdir(upload_path)

        img = self.request.files["img"][0]

        # 检测上传的文件是否是图片
        try:
            # 尝试使用Pillow库打开上传的文件
            uploaded_image = Image.open(io.BytesIO(img['body']))
            # 如果成功打开，表示是有效的图片文件
            is_valid_image = True
            # print("是图片")
        except Exception as e:
            # 如果打开失败，表示不是图片文件
            is_valid_image = False
            # print("不是图片")

        # 如果不是有效的图片文件，返回错误响应
        if not is_valid_image:
            res = dict(
                code=0,
                message="上传的文件不是有效的图片文件"
            )
            self.write(res)
            return

        if self.user.face:
            original_face = os.path.join(upload_path, self.user.face)
            if os.path.exists(original_face):
                # 使用Pillow库打开上传的图片和原始头像
                uploaded_image = Image.open(io.BytesIO(img['body']))
                original_image = Image.open(original_face)

                # 检查两个图像是否相同
                if uploaded_image.size == original_image.size and list(uploaded_image.getdata()) == list(
                        original_image.getdata()):
                    is_same_image = True
                    # print("是同一张图片")
                else:
                    is_same_image = False
                    # print("不是同一张图片")

                # 如果是同样的头像，返回错误响应
                if is_same_image:
                    res = dict(
                        code=0,
                        message="和之前头像一样就不用上传了哦!"
                    )
                    self.write(res)
                    return

        # 文件格式:时间+唯一标志+后缀
        prefix1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        prefix2 = uuid.uuid4().hex
        newname = prefix1 + prefix2 + os.path.splitext(img['filename'])[-1]
        with open(os.path.join(upload_path, newname), 'ab') as f:
            f.write(img['body'])
        res = dict(
            code=1,
            image=newname
        )
        CRUD.save_user_face(self.id, newname)
        self.write(res)
