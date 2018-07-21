# CentOS Docker 安装

Docker支持以下的CentOS版本：

- CentOS 7 (64-bit) 
- CentOS 6.5 (64-bit) 或更高的版本 

目前，CentOS 仅发行版本中的内核支持 Docker。

Docker 运行在 CentOS 7 上，要求系统为64位、系统内核版本为 3.10 以上。

Docker 运行在 CentOS-6.5 或更高的版本的 CentOS 上，要求系统为64位、系统内核版本为 2.6.32-431 或者更高版本。 





通过 **uname -r** 命令查看你当前的内核版本 

Docker 要求 CentOS 系统的内核版本高于 3.10 ，

```shell
[root@runoob ~]# uname -r 3.10.0-327.el7.x86_64
```

### 安装 Docker

Docker 软件包和依赖包已经包含在默认的 CentOS-Extras 软件源里，安装命令如下：

```shell
[root@runoob ~]# yum -y install docker-io
```

启动 Docker 后台服务 

```shell
[root@runoob ~]# service docker start
```

测试运行 hello-world 

```shell
测试运行 hello-world
```









## [centos7.4上安装python3及pip3](https://www.aliyun.com/jiaocheng/514730.html)