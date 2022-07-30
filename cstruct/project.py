from datetime import datetime
import os.path
import time
from cio import shortcuts, parse, key
from cstruct import client
from tools import pic
from tools import proxy
result_dir = "./result"


class MyProject:
    def __init__(self, guac_ip: str, guac_port: int, hostname: str, port: int, username, password, connect_type,
                 commands, machine,
                 s5_ip, s5_port, s5_usr, s5_passwd):
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
        # 代理连接
        self.s5_ip = s5_ip  # 项目的代理IP
        self.s5_port = s5_port  # 项目的代理端口
        self.s5_usr = s5_usr
        self.s5_passwd = s5_passwd
        # 设置Socks5代理
        proxy.setproxy(self.s5_ip, self.s5_port, self.s5_usr, self.s5_passwd)
        # 建立Guacd连接
        new = client.MyClient(guac_ip, guac_port, hostname, port, username, password, connect_type)
        self.client = new.client
        # 参数信息保存
        self.guac_ip = guac_ip    # 项目的Guacd Server IP
        self.guac_port = guac_port
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.connect_type = connect_type
        self.guac_ip = guac_ip
        self.commands = commands  # ['ipconfig', 'clear'，'whoami', 'clear']
        self.time_list = []
        self.machine = machine  # 'Windows' or 'Linux'
        self.res_dir = os.path.join(result_dir, hostname)
        if not os.path.exists(self.res_dir):
            os.makedirs(self.res_dir)
        self.guac_dir = os.path.join(self.res_dir, hostname)
        self.video_dir = os.path.join(self.res_dir, hostname + ".m4v")
        self.picture_dir = os.path.join(self.res_dir, "screenshot")
        if not os.path.exists(self.picture_dir):
            os.makedirs(self.picture_dir)
        self.printall()

    def printall(self):
        print("[guac_ip] : ", self.guac_ip)
        print("[guac_port] : ", str(self.guac_port))
        print("[hostname] : ", self.hostname)
        print("[port] : ", str(self.port))
        print("[username] : ", self.username)
        print("[password] : ", self.password)
        print("[connect_type] : ", self.connect_type)
        print("[commands] : ", self.commands)
        print("[machine] : ", self.machine)

    def startshell(self):
        if self.machine == 'Windows':
            shortcuts.winScmd(self.client)
        if self.machine == 'Linux':
            pass

    def execom(self):
        with open(self.guac_dir, mode='w', encoding='utf-8') as f:
            a = datetime.now()
            sync_num = 0
            while True:
                if sync_num == 20:
                    break
                instruction = self.client.receive()
                f.writelines(instruction)
                #print(instruction)
                if "4.sync" in instruction:
                    sync_num = sync_num + 1
                else:
                    sync_num = 0

            # 开启控制台
            self.startshell()
            time.sleep(4)

            for command in self.commands:
                comsym = parse.parC2K(command)
                for ksym in comsym:
                    time.sleep(0.5)
                    # sleept = sleept + 0.5
                    key.inputkey(ksym, self.client)
                for i in range(10):
                    time.sleep(0.5)
                    # sleept = sleept + 0.5
                    key.inputkey(key.key2sym('pageup'), self.client)
                time.sleep(0.5)
                b = datetime.now()
                sec = (b - a).seconds
                self.time_list.append(sec)
                print("[+] ", command, ": ", sec)

                sync_num = 0
                while True:
                    if sync_num == 30:
                        break
                    instruction = self.client.receive()
                    f.writelines(instruction)
                    # print(instruction)
                    if "4.sync" in instruction:
                        sync_num = sync_num + 1
                    else:
                        sync_num = 0

            # 关闭当前RDP会话开启的CMD窗口
            shortcuts.winclose(self.client)
            time.sleep(2)

            sync_num = 0
            while True:
                if sync_num == 50:
                    break
                instruction = self.client.receive()
                f.writelines(instruction)
                # print(instruction)
                if "4.sync" in instruction:
                    sync_num = sync_num + 1
                else:
                    sync_num = 0

            time.sleep(2)

            os.system('guacenc -s 1920x1080 -r 60000000 ' + self.guac_dir)
            for index in range(len(self.time_list)):
                if self.commands[index] != 'clear':
                    pic.video2pic(self.video_dir, self.picture_dir, self.commands[index], self.time_list[index])
