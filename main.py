from cstruct import project

if __name__ == '__main__':
    commands = ['ipconfig', 'clear', 'whoami', 'clear', 'exit']
    # guac_ip 填入运行本机本地IP
    # hostname 填入目标机器
    # username 目标机器用户
    # password 目标机器密码
    # connect_type 远程链接类型，目前仅支持RDP
    # commands 要执行的指令
    # machine 机器类型
    # s5_xx socks5代理配置
    new = project.MyProject(guac_ip='127.0.0.1', guac_port=4822,
                            hostname='x.x.x.x', port=3389,
                            username='x.x.x.x', password='x.x.x.x',
                            connect_type='rdp', commands=commands, machine='Windows',
                            s5_ip='x.x.x.x', s5_port='1081', s5_usr='x.x.x.x', s5_passwd='12345')
    # 执行任务
    new.execom()
