#修饰符@inlineCallbacks剖析

[twisted](http://twistedmatrix.com/).defer的inlineCallbacks是个修饰符，其真正实现如下： 



```python
def inlineCallbacks(f):
    """
    L{inlineCallbacks} helps you write L{Deferred}-using code that looks like a
    regular sequential function. For example::
        @inlineCallbacks
        def thingummy():
            thing = yield makeSomeRequestResultingInDeferred()
            print(thing)  # the result! hoorj!
    When you call anything that results in a L{Deferred}, you can simply yield it;
    your generator will automatically be resumed when the Deferred's result is
    available. The generator will be sent the result of the L{Deferred} with the
    'send' method on generators, or if the result was a failure, 'throw'.
    Things that are not L{Deferred}s may also be yielded, and your generator
    will be resumed with the same object sent back. This means C{yield}
    performs an operation roughly equivalent to L{maybeDeferred}.
    Your inlineCallbacks-enabled generator will return a L{Deferred} object, which
    will result in the return value of the generator (or will fail with a
    failure object if your generator raises an unhandled exception). Note that
    you can't use C{return result} to return a value; use C{returnValue(result)}
    instead. Falling off the end of the generator, or simply using C{return}
    will cause the L{Deferred} to have a result of L{None}.
    Be aware that L{returnValue} will not accept a L{Deferred} as a parameter.
    If you believe the thing you'd like to return could be a L{Deferred}, do
    this::
        result = yield result
        returnValue(result)
    The L{Deferred} returned from your deferred generator may errback if your
    generator raised an exception::
        @inlineCallbacks
        def thingummy():
            thing = yield makeSomeRequestResultingInDeferred()
            if thing == 'I love Twisted':
                # will become the result of the Deferred
                returnValue('TWISTED IS GREAT!')
            else:
                # will trigger an errback
                raise Exception('DESTROY ALL LIFE')
    It is possible to use the C{return} statement instead of L{returnValue}::
        @inlineCallbacks
        def loadData(url):
            response = yield makeRequest(url)
            return json.loads(response)
    You can cancel the L{Deferred} returned from your L{inlineCallbacks}
    generator before it is fired by your generator completing (either by
    reaching its end, a C{return} statement, or by calling L{returnValue}).
    A C{CancelledError} will be raised from the C{yielde}ed L{Deferred} that
    has been cancelled if that C{Deferred} does not otherwise suppress it.
    """
    @wraps(f)
    def unwindGenerator(*args, **kwargs):
        try:
            gen = f(*args, **kwargs)
        except _DefGen_Return:
            raise TypeError(
                "inlineCallbacks requires %r to produce a generator; instead"
                "caught returnValue being used in a non-generator" % (f,))
        if not isinstance(gen, types.GeneratorType):
            raise TypeError(
                "inlineCallbacks requires %r to produce a generator; "
                "instead got %r" % (f, gen))
        return _cancellableInlineCallbacks(gen)
    return unwindGenerator
```

当你想调用任意的在Deferred中的结果, 你可以简单的用yield声明它;你的生成器会自动的继续运行，直到Deferred的结果到达可用状态。 生成器会使用生成器的‘send’方法发送	Deferred的结果, 如果结果值是失败， 抛出异常。非Deferred的事情也可能被yield包装, 并且你的生成器会继续返回相同的对象。 这意味着yield执行大致相当于MayBeDeDebug的操作。你的inlineCallbacks-enabled 生成器会返回一个结果在生成器的返回值中的 Deferred 对象（Deferred执行失败抛出异常)