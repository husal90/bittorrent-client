import hashlib
from bencode import bdecode, bencode

class Torrent:
    def __init__(self, file_path):
        with open(file_path, 'rb') as f:
            self.meta = bdecode(f.read())
        self.info = self.meta[b'info']
        self.info_hash = hashlib.sha1(bencode(self.info)).digest()
        self.piece_length = self.info[b'piece length']
        self.pieces = [self.info[b'pieces'][i:i+20] for i in range(0, len(self.info[b'pieces']), 20)]
        self.name = self.info[b'name']
        self.length = self.info.get(b'length', 0)