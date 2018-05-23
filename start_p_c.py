import subprocess


#以下为官方运行参数
start_consumer = "java -jar \
                       -Xms1G \
                       -Xmx1G \
                       -Dlogs.dir=./consumer_logs \
                       mesh-consumer.jar"
					   
start_small_provider = "java -jar \
                             -Xms1G \
                             -Xmx1G \
                             -Ddubbo.protocol.port=20889 \
                             -Ddubbo.application.qos.enable=false \
                             -Dlogs.dir=./small_logs \
                             mesh-provider.jar"

start_medium_provider = "java -jar \
                              -Xms2G \
                              -Xmx2G \
                              -Ddubbo.protocol.port=20890 \
                              -Ddubbo.application.qos.enable=false \
                              -Dlogs.dir=./medium_logs \
                              mesh-provider.jar"
							  
start_large_provider = "java -jar \
                             -Xms3G \
                             -Xmx3G \
                             -Ddubbo.protocol.port=20891 \
                             -Ddubbo.application.qos.enable=false \
                             -Dlogs.dir=./large_logs \
                             mesh-provider.jar "
							 
def async_run(cmd, filename):
    subprocess.Popen(cmd, stdout=open(filename + '.out', 'w'), stderr=open(filename + '.err', 'w'), shell=True)


async_run(start_consumer, "consumer")
async_run(start_small_provider, "small_provider")
async_run(start_medium_provider, "medium_provider")
async_run(start_large_provider, "large_provider")

#将运行该脚本的命令行窗口关闭即可关闭 脚本启动的那几个jvm

