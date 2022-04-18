from paramiko import SSHClient
from scp import SCPClient
import argparse

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('remote_addr', type=str)
    parser.add_argument('root_password', type=str)
    args = parser.parse_args()

    ssh = SSHClient()
    ssh.connect(args.remote_addr, username='root', password=args.root_password)

    scp = SCPClient(ssh.get_transport())
    scp.put('create_profile.sh')

    ssh.exec_command('chmod a+x ./create_profile.sh')
    ssh.exec_command('./create_profile.sh')

    scp.put('src', recursive=True)
    scp.put('volatility', recursive=True)
    scp.put('MakeFile')
    scp.put('make_load_unload.sh')

    ssh.exec_command('chmod a+x ./make_load_unload.sh')
    ssh.exec_command('./make_load_unload.sh')
    scp.close()

if __name__ == '__main__':
    main()

