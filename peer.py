import socket
import struct

class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = None

    def connect(self, info_hash, peer_id):
        self.socket = socket.socket()
        self.socket.settimeout(5)
        self.socket.connect((self.ip, self.port))

        # handshake
        pstr = b'BitTorrent protocol'
        msg = struct.pack('>B', len(pstr)) + pstr + b'\x00' * 8 + info_hash + peer_id.encode()
        self.socket.sendall(msg)
        response = self.socket.recv(68)
        if response[1:20] != pstr:
            raise Exception("Invalid handshake response")
        return True