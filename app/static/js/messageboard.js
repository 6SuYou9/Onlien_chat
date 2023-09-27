$(document).ready(function () {
    var name = $("#input_name").val();
    var face = $("#input_face").val();

    function append_msg(name, data) {
        var html = "";
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
        // console.log("html----------------",html);
        $("#chat-list").prepend(html);
        SyntaxHighlighter.highlight();
        // $("#chat-list").scrollTop($("#chat-list").scrollTop() + 9999999);
    }

    $("#send_msg").click(function () {
        var data = $("#form-data").serialize();
        ue.setContent('');
        // console.log(data);
        // console.log(typeof (data))
        $.ajax({
            url: "/messageboard.html",
            type: "POST",
            data: data,
            dataType: "json",
            success: function (res) {
                if (res.code==1){
                    data = JSON.parse(res.data);
                    // alert("留言成功！");
                    // window.location = window.location.href
                    append_msg(data.name,data);

                    // console.log(typeof (data));   // object
                    // console.log(data.name,data);
                }else if (res.code==2){
                    alert("您今天已经发送过留言了！");
                }
                else{
                    alert("留言不能为空！");
                }

            }
        });
    });
})

