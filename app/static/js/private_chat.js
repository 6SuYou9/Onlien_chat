$(document).ready(function () {
    //1.定义长连接
    var conn = null;
    //2.获取昵称，头像
    var name = $("#input_name").val();
    var face = $("#input_face").val();
    var user_id = parseInt($("#input_userid").val());
    // console.log(typeof(user_id))
    // 以下从页面url获取friend_id
    // 获取当前页面的 URL
    var currentURL = window.location.href;
   // 使用 URL 对象解析 URL
    var url = new URL(currentURL);
    // 获取 friend_id 参数的值
    var friend_id = url.searchParams.get("friend_id");
    // console.log(friend_id)
    // 追加聊天消息框
    function append_msg(name, data) {
        var html = "";
        if (data.code == 2) {
            if (name == data.name) {
                //代表我自己
                html += "<div class=\"row\">";
                html += "<div class=\"col-md-3\"></div>";
                html += "<div class=\"col-md-9\">";
                html += "<div class=\"media\">";
                html += "<div class=\"media-body\">";
                html += "<h6 class=\"user-nickname text-right text-dark\">" + "[" + data.dt + "]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + data.name + "</h6>";
                html += "<div class=\"alert alert-success\" role=\"alert\">";
                html += data.content;
                html += "</div>";
                html += "</div>";
                html += "<img class=\"ml-3 rounded-circle\" style='width: 60px;height: 60px;' src=\"" + data.face + "\">";
                html += "</div></div></div>";
            }
            else {
                html += "<div class=\"row\">";
                html += "<div class=\"col-md-9\">";
                html += "<div class=\"media\">";
                html += "<img class=\"mr-3 rounded-circle\" style='width: 60px;height: 60px;' src=\"" + data.face + "\">";
                html += "<div class=\"media-body\">";
                html += "<h6 class=\"user-nickname text-dark\">" + data.name + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[" + data.dt + "]</h6>";
                html += "<div class=\"alert alert-info\" role=\"alert\">";
                html += data.content;
                html += "</div>";
                html += "</div>";
                html += "</div></div>";
                html += "<div class=\"col-md-3\"></div>";
                html += "</div>";
            }
        }
        // console.log("html----------------",html);
        $("#chat-list").append(html);
        SyntaxHighlighter.highlight();
        $("#chat-list").scrollTop($("#chat-list").scrollTop() + 9999999);
    }

    // 更新UI函数
    function update_ui(event) {
        console.log("收到消息要更新了==============")
        // console.log(event);
        var data = event.data;
        data = JSON.parse(data);
        console.log("sender:",data.user_id,"receiver:",data.friend_id)
        console.log(((data.user_id==friend_id)&&(data.friend_id==user_id)))
        console.log(((data.user_id==user_id)&&(data.friend_id==friend_id)))
        if(((data.user_id==friend_id)&&(data.friend_id==user_id)) || ((data.user_id==user_id)&&(data.friend_id==friend_id))){
            append_msg(name, data);
            console.log("update_ui===========data.friend_id==friend_id||data.friend_id==user_id",data.friend_id,friend_id)
            // append_msg(name, data);
        }else {
            console.log("update_ui===========",data.friend_id,friend_id)
            // append_msg(name, data);
        }
    }

    //3.定义连接
    function connect() {
        //之前连接没有断开先将其断开
        disconnect();
        var transports = [
            "websocket", "xhr-streaming",
            "iframe-eventsoure", "iframe-htmlfile",
            "xhr-polling", "iframe-xhr-polling",
            "jsonp-polling"
        ];
        // conn = new WebSocket("ws://" + window.location.host + "/websocket", transports);
        conn = new WebSocket("ws://127.0.0.1:8000/websocket")
        //客户端发起连接
        conn.onopen = function () {
            data = {}
            data.friend_id=friend_id
            $.ajax({
                url: "/msg/",
                type: "POST",
                data:data,
                dataType: "json",
                success: function (res) {
                    if(res.code==1){ // 说明删除完好友跳转到了privatehtml界面

                    }else {
                        var msg_data = res.data;
                        for (var k in msg_data) {
                            append_msg(name, msg_data[k]);
                    }
                    }
                }
            });
        };
        //双向通信
        conn.onmessage = function (event) {
            // console.log(event);
            // console.log(e);
            update_ui(event);
        };
        //关闭连接
        conn.onclose = function () {
            conn = null;
        }
    }

    //4.断开连接
    function disconnect() {
        if (conn != null) {
            conn.close();
            conn = null;
        }
    }

    if (conn == null) {
        connect();
    } else {
        disconnect();
    }

    // 获取表单数据
    function getFormData() {
        var arr = $("#form-data").serializeArray();
        var obj = {};
        $.map(arr, function (n, i) {
            obj[n['name']] = n['value'];
        });
        return obj
    }

    $("#send_msg").click(function () {
        var msg_data = getFormData();
        if (msg_data.content) {
            msg_data.code = 2;
            if (friend_id){
                msg_data.friend_id = friend_id
                msg_data.user_id = user_id
            }
            ue.setContent('');
            // console.log(msg_data);
            conn.send(JSON.stringify(msg_data));
            console.log("发送消息了==============")
        } else {
            alert("发送消息不能为空!");
        }
    });


});
