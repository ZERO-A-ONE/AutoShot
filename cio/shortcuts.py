import time

from cio import key


def winScmd(client):
    win_key = key.key2sym('meta')
    x_key = key.key2sym('x')
    a_key = key.key2sym('a')
    # start console
    key.sendkey(win_key, 1, client)
    time.sleep(0.01)
    key.sendkey(x_key, 1, client)
    time.sleep(0.01)
    key.sendkey(x_key, 0, client)
    time.sleep(0.01)
    key.sendkey(win_key, 0, client)
    time.sleep(0.1)
    key.sendkey(a_key, 1, client)
    key.sendkey(a_key, 0, client)
    print("[+] Start a CMD")
    time.sleep(0.1)


def winclose(client):
    alt_key = key.key2sym('Alt')
    f4_key = 65473
    key.sendkey(alt_key, 1, client)
    time.sleep(0.1)
    key.sendkey(f4_key, 1, client)
    time.sleep(0.1)
    key.sendkey(f4_key, 0, client)
    time.sleep(0.1)
    key.sendkey(alt_key, 0, client)
    time.sleep(0.1)
    print("[+] Windows Close CMD")
    time.sleep(0.1)
