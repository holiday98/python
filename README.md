# 目标

    将指定的公钥复制到远程机器的authorized_keys文件中，从而实现主控机器至远程服务器的无密码登录【key登录】。

# 运行环境
    CentOS  7.1.1503     
    Python 2.7.5
    Python模块 paramiko

# 文件
    batch_key.py
	主程序文件，执行方法：python  batch_key.py
    conf/iplist.txt
	目标机器信息，格式  10.1.1.1    22    root     password  
    /root/.ssh/id_rsa.pub 
    本机的公钥文件，会将其中的内容追加到目标机器/root/.ssh/authorized_keys 文件中
