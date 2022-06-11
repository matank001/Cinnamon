from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('remote_addr', type=str)
    parser.add_argument('root_username', type=str, default='root')
    parser.add_argument('root_password', type=str)
    args = parser.parse_args()

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(args.remote_addr, username=args.root_username , password=args.root_password)

    scp = SCPClient(ssh.get_transport())
    scp.put('create_profile.sh')

    scp.put('src', recursive=True)
    scp.put('volatility', recursive=True)

    stdin, stdout, stderr = ssh.exec_command('chmod a+x ./create_profile.sh')
    stdin, stdout, stderr =  ssh.exec_command('./create_profile.sh {0}'.format(args.root_password))
    
    if stdout.channel.recv_exit_status() is 0:
        print("Success in creating the profile")
    
    scp.get(r'profile', recursive=True)

    
    scp.put('make_load_unload.sh')

    stdin, stdout, stderr = ssh.exec_command('chmod a+x ./make_load_unload.sh')
    stdin, stdout, stderr = ssh.exec_command('./make_load_unload.sh {0}'.format(args.root_password))
    
    if stdout.channel.recv_exit_status() is 0:
        print("Success in running the module")    
    scp.close()
    
    profile_name = "".join([args.remote_addr.replace('.', '_'), args.root_username])

    os.system('cp profile/*_profile.zip volatility/volatility/plugins/overlays/linux/{0}.zip'.format(profile_name))
    print('run this -> python2 volatility/vol.py -l {0}::2325 --profile=Linux{1}x64 linux_pslist'.format(args.remote_addr, profile_name))

if __name__ == '__main__':
    main()

