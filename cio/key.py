def key2sym(key):
    # https://www.cl.cam.ac.uk/~mgk25/ucs/keysymdef.h
    # https://github.com/glyptodon/guacamole-client/
    # blob/6b24394c9bab758362bbe3e5d4bb0715052944df/
    # guacamole-common-js/src/main/webapp/modules/Keyboard.js
    key_list = {}
    # Command
    key_list['meta'] = 65511  # win
    key_list['Alt'] = 65513
    key_list['Enter'] = 65293
    key_list['pageup'] = 65365
    if key not in key_list:
        if 32 <= ord(key) <= 127:
            return ord(key)
    else:
        return key_list[key]


def sendkey(keysym: int, flag: int, client):
    key_len = len(str(keysym))
    instruction = '3.key,' + str(key_len) + '.' + str(keysym) + ',1.' + str(flag) + ';'
    client.send(instruction)
    print("[+] send key instruction: ", instruction)

def inputkey(keysym: int, client):
    key_len = len(str(keysym))
    instruction = '3.key,' + str(key_len) + '.' + str(keysym) + ',1.' + str(1) + ';'
    client.send(instruction)
    instruction = '3.key,' + str(key_len) + '.' + str(keysym) + ',1.' + str(0) + ';'
    client.send(instruction)
    print("[+] input a key: ", str(keysym))