# django使用https

使用 runserver 是不能使用 https 的

解决办法:使用 runserver_plus

步骤:

　　1.安装:

　　　　pip3 install django-extensions 
　　　　pip3 install django-werkzeug-debugger-runserver 
　　　　pip3 install pyOpenSSL

　　2.修改setting.py中的INSTALLED_APPS

```python
INSTALLED_APPS = (...
    ........
    'werkzeug_debugger_runserver',
    'django_extensions',
    ........
)
```

　　3.启动方式

```shell
python3 manage.py runserver-plus 0.0.0.0:8000 \
--cert /etc/pki/libvirt-spice/server-cert \
--key /etc/pki/libvirt-spice/server-key
```
