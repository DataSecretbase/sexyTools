[CentOS7下安装并简单设置PostgreSQL笔记](https://www.cnblogs.com/think8848/p/5877076.html) 

（1）安装后会自动启动postgresql服务；但我遇到这个问题：

** The PostgreSQL server failed to start. Please check the log output:*
*2013-11-28 11:39:15 CST LOG:  could not bind IPv6 socket: Cannot assign requested address*
*2013-11-28 11:39:15 CST HINT:  Is another postmaster already running on port 5432? If not, wait a few seconds and retry.*
*2013-11-28 11:39:15 CST WARNING:  could not create listen socket for "localhost"*
*2013-11-28 11:39:15 CST FATAL:  could not create any TCP/IP sockets*

没有查到解决方案，最后把postgresql的配置文件/etc/postgresql/8.4/main/postgresql.conf修改了一下，把listen_addresses写成127.0.0.1，这样它就不会尝试去绑定ipv6的端口，绕过这一问题；



切换到 具有root权限的用户，
（1）先把文件夹 “/var/lib/pgsql/9.3/data” 的用户所属组，给postgres 用户：

进入/var/lib/pgsql/9.3目录
cd /var/lib/pgsql/9.3
chown -R postgres:postgres data

（2）把data目前的所有文件及子目录文件权限改成： rwx (0700)

chmod -R 0700 data



[CentOS 7用户并授权](https://www.linuxidc.com/Linux/2016-11/137549.htm)



留意postmaster.pid 文件 

 