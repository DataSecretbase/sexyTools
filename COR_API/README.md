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
