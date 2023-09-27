/*
* 处理用户好友申请
* friendname: 好友名称
* num: 1 同意  2 拒绝
*
* */
function FriendRequest(friend, num, way) {
    if (way == "Apply") {
        var data = {
            friendname: friend,
            num: num,
            way: way
        }
    } else if (way == "Delete") {
        var data = {
            friend_id: friend,
            way: way
        }
    }
    $.ajax({
        url: "/showapply.html",
        data: data,
        dataType: "json",
        type: "POST",
        success: function (res) {
            if (res.code == 1) {
                //状态code：1表示成功！  好友申请处理成功
                location.href = window.location.href;
            }else if (res.code==2){    // 删除好友成功
                location.href = '/privatechat.html';
            }else if (res.code == 0) {  // 不成功
                alert("好友申请出现错误，请重试!")
            } else if (res.code == 3) {
                alert("删除好友出现错误，请重试!")
            }
        }
    });
}


// 点击同意按钮
$('.approve-btn').click(function () {
    // 获取按钮上存储的好友 ID
    var friendName = $(this).data('friend-name');

    // 执行同意申请操作，使用 friendId 来确定操作的目标好友
    FriendRequest(friendName, 1, "Apply");
});

// 点击拒绝按钮
$('.reject-btn').click(function () {
    // 获取按钮上存储的好友 ID
    var friendName = $(this).data('friend-name');

    // 执行拒绝申请操作，使用 friendId 来确定操作的目标好友
    FriendRequest(friendName, 2, "Apply");
});

// 点击删除好友按钮
$('.delete-btn').click(function () {
    // 获取按钮上存储的好友 ID
    var friend_id = $(this).data('delete-id');

    // 执行拒绝申请操作，使用 friendId 来确定操作的目标好友
    FriendRequest(friend_id, 2, "Delete");
});