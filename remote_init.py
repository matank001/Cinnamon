from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
import argparse

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
    stdin, stdout, stderr =  ssh.exec_command('./create_profile.sh')
    print(stdout.readlines())
    scp.get(r'profile', recursive=True)

    
    scp.put('make_load_unload.sh')

    stdin, stdout, stderr = ssh.exec_command('chmod a+x ./make_load_unload.sh')
    stdin, stdout, stderr = ssh.exec_command('./make_load_unload.sh')
    scp.close()

if __name__ == '__main__':
    main()

