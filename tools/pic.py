import os.path

import cv2


def video2pic(video, picture_dir, picture, time):
    video_path = os.path.join(video)
    picture_path = os.path.join(picture_dir, picture) + ".jpg"
    print("[+] VIDEO PATH: ", video_path)
    print("[+] PICTURE PATH: ", picture_path)
    try:
        vc = cv2.VideoCapture(video_path)  # 读取视频
        video_width = int(vc.get(cv2.CAP_PROP_FRAME_WIDTH))  # 视频宽度
        video_height = int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 视频高度
        vc.set(cv2.CAP_PROP_POS_MSEC, 1000 * time)  # 设置读取位置，1000毫秒
        rval, frame = vc.read()  # 读取当前帧，rval用于判断读取是否成功
        if rval:
            cv2.imwrite(picture_path, frame)  # 将当前帧作为图片保存到 cover_path
        else:
            print("读取失败")
    except Exception as e:
        pass


if __name__ == '__main__':
    video = "../xx.guac.m4v"
    pic = "../test"
    video2pic(video, pic, 21)
    video2pic(video, pic, 30)
