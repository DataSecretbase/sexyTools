# competition
DB组的比赛项目工具集合 大仓库收录自开发的工具，插件。



- hotkeyVimPluginSetup.sh

  VIM的插件包一件安装脚本，spf13配置 [spf13常用插件介绍](http://vim.spf13.com/)

- crontab 

  crond是linux下用来周期性的执行某种任务或等待处理某些事件的一个守护进程，与windows下的计划任务类似，当安装完成操作系统后，默认会安装此服务工具，并且会自动启动crond进程，crond进程每分钟会定期检查是否有要执行的任务，如果有要执行的任务，则自动执行该任务。

  [crontab 命令CheatSheet](https://www.cnblogs.com/peida/archive/2013/01/08/2850483.html)

- delfine.sh

  脚本作用是定时删除某个文件夹下的文件，请搭配crontab使用

- Meltdown-exploit

  检测服务器的Intel cpu硬件是否还有 meltdown漏洞， 目前linux内核版本4.15 -rc4才加装补丁 

  查看内核版本 uname -a 

  查看cpu 型号    cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c

  查看cpu所有信息 cat /proc/cpuinfo

- 环境配置  

  开发环境配置 HINTs[收录问题解决方案]请注明你的配置环境（格式 系统+软件版本）

- COR_API

  跨域请求API解决方案与用例，可供参考。
