/*
* 客户端向服务器端发起请求，基于http协议，ajax
* url：请求地址
* rurl：跳转地址
* fields：验证字段
* msg：消息提示
* */
function request(url, rurl, fields, msg) {
    $("#btn-sub").click(function () {
        var data = $("#form-data").serialize();
        $.ajax({
            url: url,
            data: data,
            dataType: "json",
            type: "POST",
            success: function (res) {
                if (res.code == 1) {
                    //状态code：1表示成功！
                    alert(msg);
                    location.href = rurl;
                }
                else if ( res.code==5 )
                {
                //    用户已经登录，不能重复登录
                    alert("已经是好友了哦，不需要重复添加!");
                }
                else if ( res.code==6 )
                {
                //    用户已经登录，不能重复登录
                    alert("用户已经登录，不能重复登录");
                }
                else if ( res.code==7 )
                {
                //    用户添加自己为好友
                    alert("不能添加自己为好友哦!换个朋友添加试试吧!");
                }
                else if ( res.code==8 )
                {
                //    忘记密码时输入的昵称，邮箱，电话不为同一用户
                    alert("不可以使用错误的用户信息哦!");
                   for (var k in fields) {
                        if (typeof res[fields[k]] == "undefined") {
                            $("#error_" + fields[k]).empty();
                        }
                    }
                }
                else if ( res.code==9 )
                {
                //    邮箱验证码错误
                    alert("验证码错误，请输入正确验证码哦!");
                }
                else if(res.code==10)
                {
                    alert("您什么都没有修改哦!");
                }
                else if(res.code ==11)
                {
                        location.href = rurl;
                        alert(msg);
                }
                else if(res.code==12)
                {
                        $("#show_name").val(res.data.name);
                        $("#show_email").val(res.data.email);
                        $("#show_phone").val(res.data.phone);
                        $("input[name='input_sex']").filter("[value='" + res.data.sex + "']").prop("checked", true);
                        $("#show_info").val(res.data.info);
                        alert(msg);
                }
                else
                {
                    //不成功，验证字段
                    for (var k in fields) {
                        if (typeof res[fields[k]] == "undefined") {
                            $("#error_" + fields[k]).empty();
                        } else {
                            $("#error_" + fields[k]).empty();
                            $("#error_" + fields[k]).append(
                                res[fields[k]]
                            );
                        }
                    }
                }
            }
        });
    });
}



// 发送邮件
function send_email(url,fields, msg) {
    $("#send_email").click(function () {
        var data = $("#form-data").serialize();
        $.ajax({
            url: url,
            data: data,
            dataType: "json",
            type: "POST",
            success: function (res) {
                if (res.code == 1) {
                    //状态code：1表示成功！
                    alert(msg);
                }
                else if ( res.code==8 )
                {
                //    忘记密码时输入的昵称，邮箱，电话不为同一用户
                    alert("不可以使用错误的用户信息哦!");
                    for (var k in fields) {
                        if (typeof res[fields[k]] == "undefined") {
                            $("#error_" + fields[k]).empty();
                        }
                    }
                }
                else {
                    //不成功，验证字段
                    for (var k in fields) {
                        if (typeof res[fields[k]] == "undefined") {
                            $("#error_" + fields[k]).empty();
                        } else {
                            $("#error_" + fields[k]).empty();
                            $("#error_" + fields[k]).append(
                                res[fields[k]]
                            );
                        }
                    }
                }
            }
        });
    });
}