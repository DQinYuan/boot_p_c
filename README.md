# boot_p_c

进入该目录，然后执行以下命令

```
python start_p_c.py
```

然后就在后台启动四个JVM，分别是一个Consumer和三个Provider（small、medium和large），日志不会在控制台中打印，而是会在目录中生成相应的日志文件。不过因为Provider和Consumer是固定由官方提供的，所以这些日志其实也没什么用。通过`jps`可以验证确实已经在后台启动了。

因为启动的这些JVM都是启动它的控制台的子进程，当你想关闭这些JVM时，只需要退出启动它的控制台就可以了。
