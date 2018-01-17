# 跨域请求第三方API指北

- ajaxAPI.js & getshanbei_voc.php 

  这里使用的API为扇贝网查询单词和查询句子的API，我想使用AJAX在前端异步刷新查询单词。但是扇贝网的API是设置的不允许跨域访问的，也没有提供jsonp形式的返回。所以这里使用PHP下载扇贝网的接口将得到扇贝网的json数据保存为字符串。然后前端异步调用这个本机PHP接口，在AJAX的statechange函数里面对得到的字符串数据解析为JSON数据供使用。

  ​

  AJAX使用原生js（JQUERY方法更新）

  ​

  **HINT** PHP请求接口文件务必与前端同域	

----

一下是一些科普

## 跨域的背景

> 1.为了安全我们的浏览器有同源策略。使我们不方便跨域访问。
> 2.出于种种原因我们就是要跨域访问。
> 3.前辈们通过钻空子想出来的方法，和后来新的API等都让我们能够跨域访问。

关键字：同源策略、跨域访问。



1. JSONP (do it)
2. window.name + iframe (unnecessary)
3. hash + iframe (unnecessary)
4. postMessage (do it)
5. CORS (do it)
6. WebSockets(do it)





Django的CSRF



## JSONP

JSONP(JSON with Padding)是一个非官方的协议，它允许在服务器端集成Script tags返回至客户端，通过javascript callback的形式实现跨域访问（这仅仅是JSONP简单的实现形式）。

**3、如何使用JSONP？**

下边这一DEMO实际上是JSONP的简单表现形式，在客户端声明回调函数之后，客户端通过script标签向服务器跨域请求数据，然后服务端返回相应的数据并动态执行回调函数。

```html
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />  
<script type="text/javascript">  
    function jsonpCallback(result) {  
        //alert(result);  
        for(var i in result) {  
            alert(i+":"+result[i]);//循环输出a:1,b:2,etc.  
        }  
    }  
    var JSONP=document.createElement("script");  
    JSONP.type="text/javascript";  
    JSONP.src="http://crossdomain.com/services.php?callback=jsonpCallback";  
    document.getElementsByTagName("head")[0].appendChild(JSONP);  
</script>  
```

```PHP
<?php  
  
//服务端返回JSON数据  
$arr=array('a'=>1,'b'=>2,'c'=>3,'d'=>4,'e'=>5);  
$result=json_encode($arr);  
//echo $_GET['callback'].'("Hello,World!")';  
//echo $_GET['callback']."($result)";  
//动态执行回调函数  
$callback=$_GET['callback'];  
echo $callback."($result)";  
```

**Jsonp原理：** 
首先在客户端注册一个callback, 然后把callback的名字传给服务器。
此时，服务器先生成 json 数据。
然后以 javascript 语法的方式，生成一个function , function 名字就是传递上来的参数 jsonp.
最后将 json 数据直接以入参的方式，放置到 function 中，这样就生成了一段 js 语法的文档，返回给客户端。
客户端浏览器，解析script标签，并执行返回的 javascript 文档，此时数据作为参数，传入到了客户端预先定义好的 callback 函数里.（动态执行回调函数）

**使用JSON的优点在于：**

- 比XML轻了很多，没有那么多冗余的东西。
- JSON也是具有很好的可读性的，但是通常返回的都是压缩过后的。不像XML这样的浏览器可以直接显示，浏览器对于JSON的格式化的显示就需要借助一些插件了。
- 在JavaScript中处理JSON很简单。
- 其他语言例如PHP对于JSON的支持也不错。



##html5 postMessage解决跨域消息传递

html5引入的message的API可以更方便、有效、安全的解决跨域数据传递.



##CORS跨域资源共享

1. 服务器

   服务器端对于CORS的支持，主要就是通过设置Access-Control-Allow-Origin来进行的。如果浏览器检测到相应的设置，就可以允许Ajax进行跨域的访问。

2. PHP：只需要使用如下的代码设置即可。

   ```PHP
   <?php  
    header("Access-Control-Allow-Origin:*");  
   ```

   ​

