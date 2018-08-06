# DJANGO-数据迁移出现问题的解决方法

没错，我被一个不知道在哪的错误折腾了一下午。最后用了最简单粗暴的解决方法。

1.先把 app 下的 migrations 文件夹下的除了 __init__.py 的文件全部删完

2.删除最外侧的 db.sqlite3 文件

3.手打以下三句话

```shell
python3 manage.py sqlmigrate your_app_name 0001
python3 manage.py makemigrations 
python3 manage.py migrate
```

再次运行，问题解决！

P.S. 这么做会删掉超级管理员的数据，记得重新创建