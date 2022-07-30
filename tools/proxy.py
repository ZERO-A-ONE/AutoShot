import os
import subprocess

proxy_dir = "/etc/proxychains4.conf"  # Proxychains配置文件路径


# 修改Proxychains的代理配置，仅限Socks5代理
def changeproxy(ip, port, user, passwd):
    if not os.path.exists(proxy_dir):
        print("[-] proxy_dir not exist")
        return
    print("[+] Proxy IP: ", ip)
    print("[+] Proxy IP: ", port)
    print("[+] Proxy IP: ", user)
    print("[+] Proxy IP: ", passwd)
    line_context = []
    line_num = 0
    rindex = 0
    for line in open(proxy_dir):
        line_context.append(line)
        if '[ProxyList]' in line:
            rindex = line_num
        line_num = line_num + 1
    print("[+] File Lines: ", line_num)
    # print(line_context)
    # print(line_context[rindex])
    proxy_str = "socks5 " + ip + " " + port + " " + user + " " + passwd

    if os.path.exists(proxy_dir):
        cmd = "cp " + proxy_dir + " " + proxy_dir + '.bk'
        result = subprocess.check_output(cmd, shell=True)
        os.remove(proxy_dir)

    # 以写的方式打开文件，如果文件不存在，就会自动创建
    file_write_obj = open(proxy_dir, 'w')
    for index in range(rindex + 1):
        file_write_obj.writelines(line_context[index])
        file_write_obj.write('\n')
    file_write_obj.writelines(proxy_str)
    file_write_obj.write('\n')
    file_write_obj.close()


# alias pc=proxychains4
def startguacd():
    '''
    cmd = "exec bash"
    result = subprocess.check_output(cmd, shell=True)
    cmd = "alias pc=proxychains4"
    result = subprocess.check_output(cmd, shell=True)
    cmd = "source ~/.profile"
    result = subprocess.check_output(cmd, shell=True)
    '''
    #   首先kill掉已经存在的guacd服务，重启guacd服务
    cmd = "ps -aux | grep 'guacd'"
    print("[CMD]: ", cmd)
    ps_result = subprocess.check_output(cmd, shell=True)
    ps_result = ps_result.decode('utf8')
    # print(ps_result)
    lines = ps_result.split('\n')
    process = ""
    flag = True
    for line in lines:
        if 'guacd -b 0.0.0.0 -l 4822' in line:
            print("[+] Find Process: ", line)
            process = line
            flag = False
            break
    if flag:
        print("[+] Don't Find Process: ", line)
    else:
        pid = ""
        process = process.split(' ')
        for strs in process:
            if strs.isdigit():
                print("[+] Find PID: ", strs)
                pid = strs
                break
        # 终结进程
        cmd = "sudo kill " + pid
        kill_result = subprocess.check_output(cmd, shell=True)
        kill_result = kill_result.decode('utf8')
        print("[CMD]: ", cmd)
        print(kill_result)

    cmd = "proxychains4 guacd -b 0.0.0.0 -l 4822"
    guacd_result = subprocess.check_output(cmd, shell=True)
    guacd_result = guacd_result.decode('utf8')
    print("[CMD]: ", cmd)
    print(guacd_result)


def setproxy(ip, port, user, passwd):
    changeproxy(ip, port, user, passwd)
    startguacd()
