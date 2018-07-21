#twisted reactor 问题板块

##reactor空转时会不会消耗CPU资源？

```python
from twisted.internet import reactor
reactor.run()
```

这个地方直接把reactor运行起来，而没有往reactor里面添加事件，这样的事件循环会不会带来性能消耗。


![事件循环](http://wiki.jikexueyuan.com/project/twisted-intro/images/p02_reactor-1.png)

异步模式中客户端的核心就是最高层的循环体，

按照socket设计一异步模式
1. 使用select函数等待所有Socket，直到有一个socket有效数据到来
2. 对每个有数据需要读取的socket，从中读取数据。但仅仅只是读取有效数据，不能为了等待还没来到的数据而发生阻塞。
3. 重复前两步，直到所有的socket被关闭

