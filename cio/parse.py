from cio import key


# 将一个指令解析为guacd识别代码
def parC2K(command: str):
    ksym_list = []
    for ch in command:
        ksym_list.append(key.key2sym(ch))
    print("[+] parse a command : ", command)
    ksym_list.append(key.key2sym('Enter'))
    print("[+] this keysym list: ", ksym_list)
    return ksym_list


if __name__ == '__main__':
    commands = ["ipconfig", "whoami"]
    for command in commands:
        parC2K(command)
