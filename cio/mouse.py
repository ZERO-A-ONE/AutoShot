def sendmouse(x: int, y: int, flag: int, client):
    """
    :param x:   鼠标移动到的x轴
    :param y:   鼠标移动到的y轴
    :param flag:    鼠标按压模式，0为松开（纯移动），1为按下
    :return:
    """
    x_len = len(str(x))
    y_len = len(str(y))
    f_len = len(str(flag))
    instruction = '5.mouse,'
    instruction = instruction + str(x_len) + "." + str(x) + ","
    instruction = instruction + str(y_len) + "." + str(y) + ","
    instruction = instruction + str(f_len) + "." + str(flag) + ";"
    client.send(instruction)
    print("[+] send mouse instruction: ", instruction)

