# AutoShot

- Author：ZERO-A-ONE
- Date：2022-07-22

本项目主要依赖于Guacd，实现对于RDP、SSH、VNC等协议的自动执行命令和截图工作

目前的工具测试环境：

- Ubuntu 20.04

- Ubuntu 18.04

## 0x1 环境配置

### 1.1 编译安装Guacd

我们首先需要安装一些依赖环境

```bash
sudo apt-get -y install build-essential libcairo2-dev libossp-uuid-dev libavcodec-dev libavformat-dev libavutil-dev \
libswscale-dev freerdp2-dev libpango1.0-dev libssh2-1-dev libtelnet-dev libvncserver-dev libpulse-dev libssl-dev \
libvorbis-dev libwebp-dev libwebsockets-dev freerdp2-x11 libtool-bin ghostscript dpkg-dev wget crudini libc-bin
```

```bash
sudo apt install build-essential libcairo2-dev libjpeg-turbo8-dev \
    libpng-dev libtool-bin libossp-uuid-dev libvncserver-dev \
    freerdp2-dev libssh2-1-dev libtelnet-dev libwebsockets-dev \
    libpulse-dev libvorbis-dev libwebp-dev libssl-dev \
    libpango1.0-dev libswscale-dev libavcodec-dev libavutil-dev \
    libavformat-dev
```

然后可以从官方的GitHub中获取到最新的源码

```
https://github.com/apache/guacamole-server
```

然后解压源码

```bash
tar -xzf guacamole-server-1.4.0.tar.gz
cd guacamole-server-1.4.0
```

然后生成configure文件

```bash
autoreconf -fi
```

生成编译配置信息

```bash
./configure --with-systemd-dir=/etc/systemd/system --enable-allow-freerdp-snapshots
```

然后进行编译

```bash
make -j
```

最后进行安装

```bash
sudo make install
```

重新加载配置

```bash
ldconfig
```

查找进程

```bash
ps -aux | grep 'guacd
```

杀掉进程，重新绑定

```bash
guacd -b 0.0.0.0 -l 4822
```

### 1.2 Python依赖包

本项目主要依赖于以下第三方包

- opencv-python

安装依赖包

```bash
$ pip3 install opencv-python
```

### 1.3 依赖软件

代理功能依赖于proxychain

```bash
$ sudo apt-get install -y proxychains4
```

安装完之后可以找到`/etc/proxychains.conf`或`/etc/proxychains4.conf`文件进行修改

## 0x2 使用

在main文件里有最简单的使用示例，新建一个Project对象，并执行即可完成任务

```python
commands = ['ipconfig', 'clear', 'whoami', 'clear', 'exit']
new = project.MyProject(guac_ip='x.x.x.x', guac_port=4822, hostname='x.x.x.x', port=3389, username='Administrator', password='xxxxxxxx', connect_type='rdp', commands=commands, machine='Windows', s5_ip='xxxxxx', s5_port='1081', s5_usr='xxx', s5_passwd='12345')
# 执行任务
new.execom()
```

本项目依赖于root权限，运行时请执行

```bash
$ sudo python3 main.py
```

## 0x3 常见问题

### 3.1 opencv安装问题

在安装包`cv2`时如果遇到报错如下：

```
Collecting opencv
  Could not find a version that satisfies the requirement opencv (from versions: )
No matching distribution found for opencv
```

先尝试使用apt包管理器安装opencv

```bash
$ sudo apt install python-opencv -y
```

然后更新pip

```bash
$ pip install --upgrade pip
$ pip3 install --upgrade pip
```

再次尝试安装

```bash
$ pip install opencv-python
$ pip3 install opencv-python
```

### 3.2 Ubuntu搭建Socks5代理

安装脚本

```bash
wget --no-check-certificate  https://raw.githubusercontent.com/kingchun/socks5-install-for-gost/main/socks5_install.sh && bash socks5_install.sh
```

查看状态

```bash
systemctl status gost #查看状态
systemctl start gost #启动
systemctl stop gost #停止
```

