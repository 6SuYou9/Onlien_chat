// 背景代码瀑布的实现
window.onload=function(){
    var canvas=document.getElementById("canvas");
    var context=canvas.getContext("2d");
    var W=window.innerWidth;
    var H=window.innerHeight;
    canvas.width=W;
    canvas.height=H;
    var fontSize=20;
    //显示字体大小
    var colunms=Math.floor(W/fontSize);
    var drops=[];
    for(var i=0;i<colunms;i++){
        drops.push(0);
    }
    var str="9876543210abcdefghijklmnopqrstuvwxyz";
    //javascript html5 canvas 显示元素
    function draw(){
        context.fillStyle="rgba(0,0,0,0.05)";
        context.fillRect(0, 0, W, H);
        context.font = "700 "+fontSize+"px 华文新魏"
        context.fillStyle ="#0000ff";
        context.shadowcolor ="yellow";
        context.shadowBlur = 10;
        context.shadowOffsetX = 10100;
        context.shadowOffsetY = 10100;

        //1accf9 字体颜色
        for(var i=0;i<colunms;i++){
            var index=Math.floor(Math.random()*str.length);
            var x=i*fontSize;
            var y=drops[i]*fontSize;
            context.fillText(str[index], x, y);
            if (y>=canvas.height && Math.random()>0.99) {
                drops[i]=0;
            }
            drops[i]++;
        }
    };
    function randColor(){
        var r =Math.floor(Math.random() * 256);
        var g =Math.floor(Math.random() * 256);
        var b =Math.floor(Math.random() * 256);
        return"rgb("+r+","+g+","+b+")";
    }
    draw();
    setInterval(draw,20);
    //速度
};

