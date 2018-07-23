# centos7下使用yum安装mysql

CentOS7的yum源中默认好像是没有mysql的。为了解决这个问题，我们要先下载mysql的repo源。

\1. 下载mysql的repo源

```
$ wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
```

\2. 安装mysql-community-release-el7-5.noarch.rpm包

```
$ sudo rpm -ivh mysql-community-release-el7-5.noarch.rpm
```

安装这个包后，会获得两个mysql的yum repo源：/etc/yum.repos.d/mysql-community.repo，/etc/yum.repos.d/mysql-community-source.repo。

\3. 安装mysql

```
$ sudo yum install mysql-server
```

根据步骤安装就可以了，不过安装完成后，没有密码，需要重置密码。

\4. 重置密码

重置密码前，首先要登录

```
$ mysql -u root
```

登录时有可能报这样的错：ERROR 2002 (HY000): Can‘t connect to local MySQL server through socket ‘/var/lib/mysql/mysql.sock‘ (2)，原因是/var/lib/mysql的访问权限问题。下面的命令把/var/lib/mysql的拥有者改为当前用户：

```
$ sudo chown -R openscanner:openscanner /var/lib/mysql
```

然后，重启服务：

```
$ service mysqld restart
```

接下来登录重置密码：

```
$ mysql -u root
```

```
mysql > use mysql;mysql > update user set password=password(‘123456‘) where user=‘root‘;mysql > exit;
```

5. 需要更改权限才能实现远程连接MYSQL数据库

```
可以通过以下方式来确认：
```

```
root#mysql -h localhost -uroot -p
```

```
Enter password: ******
```

```
Welcome to the MySQL monitor.   Commands end with ; or \g.
```

```
Your MySQL connection id is 4 to server version: 4.0.20a-debug
```

```
Type ‘help;’ or ‘\h’ for help. Type ‘\c’ to clear the buffer.
```

```
mysql> use mysql; (此DB存放MySQL的各种配置信息)
```

```
Database changed
```

```
mysql> select host,user from user; (查看用户的权限情况)
```

```
mysql> select host, user, password from user;
+-----------+------+-------------------------------------------+
| host       | user | password                                   |
+-----------+------+-------------------------------------------+
| localhost | root | *4ACFE3202A5FF5CF467898FC58AAB1D615029441 |
| 127.0.0.1 | root | *4ACFE3202A5FF5CF467898FC58AAB1D615029441 |
| localhost |       |                                            |
+-----------+------+-------------------------------------------+
4 rows in set (0.01 sec)
```

```
由此可以看出，只能以localhost的主机方式访问。
解决方法：
mysql> Grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;
(%表示是所有的外部机器，如果指定某一台机，就将%改为相应的机器名；‘root’则是指要使用的用户名，)
mysql> flush privileges;    (运行此句才生效，或者重启MySQL)
Query OK, 0 rows affected (0.03 sec)
再次查看。。
mysql> select host, user, password from user;
+-----------+------+-------------------------------------------+
| host       | user | password                                   |
+-----------+------+-------------------------------------------+
| localhost | root | *4ACFE3202A5FF5CF467898FC58AAB1D615029441 |
| 127.0.0.1 | root | *4ACFE3202A5FF5CF467898FC58AAB1D615029441 |
| localhost |       |                                            |
| %          | root | *4ACFE3202A5FF5CF467898FC58AAB1D615029441 |
+-----------+------+-------------------------------------------+
4 rows in set (0.01 sec)
```