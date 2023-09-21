/*
* k，名称，face
* w，宽度，200
* h，高度，200
* url，上传地址
* */

function uploadface(k, w, h, url) {
    $("#upload_" + k).click(function () {
        var img = $("#file_" + k)[0].files[0];
        if (img) {
            var formData = new FormData();
            formData.append("img", img);
            $.ajax({
                url: url,
                type: "POST",
                dataType: "json",
                data: formData,
                cache: false,
                // cache: false：
                // cache 是指浏览器是否缓存 Ajax 请求的响应。
                // cache: false 表示禁用浏览器的缓存机制，确保每次发送的请求都不会从浏览器缓存中获取响应。
                // 在文件上传等需要实时数据或避免缓存数据的情况下，通常会将此选项设置为 false。
                contentType: false,
                // contentType: false：
                // contentType 是指发送到服务器的请求的数据类型。通常，Ajax 请求的默认 contentType 为 "application/x-www-form-urlencoded; charset=UTF-8"，适用于普通表单数据提交。
                // 当上传文件时，文件数据不需要设置 contentType，因此将其设置为 false 是为了让浏览器自动根据上传的内容类型设置适当的 contentType，而不是使用默认的表单数据的 contentType。
                // processData: false：
                processData: false,
                // processData: false,
                // processData 控制是否对数据进行预处理，默认为 true。
                // 当设置为 false 时，表示不希望 jQuery 对数据进行自动处理（如将对象转换为查询字符串）。
                // 在上传文件时，通常会将其设置为 false，以避免对 FormData（用于文件上传的数据格式）进行额外的处理。
                // 综上所述，这些配置选项在文件上传过程中有助于确保数据的正确处理和传输，以及避免一些潜在的问题，因此它们在文件上传的前端代码中非常常见。
                success: function (res) {
                    if (res.code == 1) {
                        var image = res.image;
                        var content1 = "<img src='/static/uploads/" + image + "' style='width: 200px;200px;'>";
                        $("#image_" + k).empty();
                        $("#image_" + k).append(content1);
                        var content2 = "<img class=\"mr-3 rounded-circle\" src='/static/uploads/" + image + "' style=\"height: 60px ;width: 60px\">";
                        $("#show_" + k).empty();
                        $("#show_" + k).append(content2);
                        $("#input_" + k).attr("value", image);
                        alert("上传成功!");
                        // location.href = window.location.href;
                    } else {
                        // console.log("上传有问题哦！")
                        alert(res.message);
                    }
                }
            });
        }
    });

}