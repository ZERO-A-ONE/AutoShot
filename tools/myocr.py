import easyocr

def pic2word(picture):
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(picture)
    word = ""
    for i in result:
        word = i[1]
        print(word)
    return word

if __name__ == '__main__':
    pic2word("../image/19.jpg")