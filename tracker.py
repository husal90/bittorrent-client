import urllib.parse
import urllib.request
from bencode import bdecode

class Tracker:
    def __init__(self, torrent):
        self.torrent = torrent

    def get_peers(self):
        url = self.torrent.meta[b'announce'].decode()
        params = {
            'info_hash': self.torrent.info_hash,
            'peer_id': '-PC0001-123456789012',
            'port': 6881,
            'uploaded': 0,
            'downloaded': 0,
            'left': self.torrent.length,
            'compact': 1
        }
        full_url = url + '?' + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
        with urllib.request.urlopen(full_url) as response:
            data = response.read()
            return self.parse_peers(bdecode(data)[b'peers'])

    def parse_peers(self, peer_data):
        peers = []
        for i in range(0, len(peer_data), 6):
            ip = '.'.join(str(b) for b in peer_data[i:i+4])
            port = int.from_bytes(peer_data[i+4:i+6], 'big')
            peers.append((ip, port))
        return peers