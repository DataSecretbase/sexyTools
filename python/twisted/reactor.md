# twisted reactor 问题板块



## reactor空转时会不会消耗CPU资源？



```python
from twisted.internet import reactor
reactor.run()
```

这个地方直接把reactor运行起来，而没有往reactor里面添加事件，这样的事件循环会不会带来性能消耗。




**先简答介绍下异步编程的模式**

异步模式中客户端的核心就是最高层的循环体，

按照socket设计一异步模式
1. 使用select函数等待所有Socket，直到有一个socket有效数据到来
2. 对每个有数据需要读取的socket，从中读取数据。但仅仅只是读取有效数据，不能为了等待还没来到的数据而发生阻塞。
3. 重复前两步，直到所有的socket被关闭





如果在服务器端口固定的条件下，同步模式的客户端并不需要循环体，只需要顺序罗列三个工作函数就可以了。但是我们的异步模式的客户端必须要有一个循环体来保证我们能够同时监视所有的socket端。这样我们就能在一次循环体中处理尽可能多的数据。 

![事件循环](http://wiki.jikexueyuan.com/project/twisted-intro/images/p02_reactor-1.png)



## Reactor设计模式



Reactor，即反应堆。Reactor 的一般工作过程是首先在 Reactor 中注册（Reactor）感兴趣事件，并在注册时候指定某个已定义的回调函数（callback）；当客户端发送请求时，在 Reactor 中会触发刚才注册的事件，并调用对应的处理函数。在这一个处理回调函数中，一般会有数据**接收**、处理、**回复**请求等操作。 

![](http://daoluan.net/blog/wp-content/uploads/2013/08/reactor_pattern.png)

libevent 采用的就是 Reactor 的设计思想。其 **Reactor 的中心思想是众所周知的 I/O 多路复用**：select,poll,epoll,kqueue 等.libevent 精彩的将定时事件，信号处理，I/O 事件结合在在一起，也就是说用户同时在 Reactor 中注册上述三类事件。遗憾的是，libevent 不支持多线程，也就是说它同步处理请求，导致不能处理大量的请求；这样并不是说 Reactor 实现的网络库都不支持多线程，而是 libevent 本身的原因，我们也可以通过修改让 ilbevent 支持多线程，并发处理多个请求。 