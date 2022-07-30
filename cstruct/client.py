from guacamole.client import GuacamoleClient


class MyClient:
    def __init__(self, guac_ip: str, guac_port: int, hostname: str, port: int, username: str, password: str, connect_type: str):
        self.guac_ip = guac_ip  # guac server ip
        self.guac_port = guac_port  # guac server prot
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.connect_type = connect_type
        self.client = ""
        if self.connect_type == "rdp":
            self.client = self.RDPConnect()

    def RDPConnect(self):
        client = GuacamoleClient(self.guac_ip, self.guac_port)
        protocol = self.connect_type
        hostname = self.hostname
        port = self.port
        ignore_cert = 'true'
        disable_audio = 'true'
        video = ["wav"]
        image = ["image/png", "image/jpeg"]
        timezone = ["America/New_York"]
        VERSION_1_3_0 = 'VERSION_1_3_0'
        username = self.username
        password = self.password
        console = 'true'
        width = '1920'
        height = '1080'
        dpi = '300'

        client.handshake(protocol=protocol, hostname=hostname, port=port,
                         ignore_cert=ignore_cert, disable_audio=disable_audio,
                         video=video,
                         image=image,
                         timezone=timezone,
                         VERSION_1_3_0=VERSION_1_3_0,
                         username=username, password=password,
                         console=console, width=width, height=height, dpi=dpi
                         )

        return client
