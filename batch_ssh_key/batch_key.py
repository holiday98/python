#!/usr/bin/python
# -*- coding: utf-8 -*-  
import sys
import os
import paramiko

id_rsa_pub = '/root/.ssh/id_rsa.pub'

<<<<<<< .mine
id_rsa_pub = '/root/.ssh/id_rsa.pub1'

if not id_rsa_pub:
||||||| .r166944
id_rsa_pub = '/root/.ssh/id_rsa.pub1'

if not  id_rsa_pub:
=======
if not os.path.isfile(id_rsa_pub):
>>>>>>> .r166998
    logger.info('id_rsa.pub Does not exist!')
    sys.exit(0)

    
def up_key(host,port,user,passwd):
    try:
        s = paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	s.connect(host, port, user, passwd,timeout=5)

        t = paramiko.Transport((host, port))
        t.connect(username=user, password=passwd)
        sftp =paramiko.SFTPClient.from_transport(t)

        print 'create Host:%s .ssh dir......' %host
        s.exec_command('mkdir ~/.ssh/')
        print 'upload id_rsa.pub to Host:%s......' %host
        sftp.put(id_rsa_pub, "/tmp/temp_key")
        s.exec_command('cat /tmp/temp_key >> ~/.ssh/authorized_keys && rm -rf /tmp/temp_key')
        print 'host:%s@%s auth success!\n' %(user, host)
        s.close()
        t.close()
    except Exception, e:
        import traceback
        traceback.print_exc()
        try:
            s.close()
            t.close()
        except:
            pass

def run():
    for line in open('conf/iplist.txt'):
        line = line.strip('\n')
        host,port,user,passwd = line.split()
        up_key(host, int(port), user, passwd)

if __name__ == '__main__':
    run()
