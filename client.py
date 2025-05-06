from torrent import Torrent
from tracker import Tracker
from peer import Peer


def main():
    torrent = Torrent('ubuntu.torrent')
    tracker = Tracker(torrent)
    peers = tracker.get_peers()

    print(f"Found {len(peers)} peers")

    if peers:
        ip, port = peers[0]
        peer = Peer(ip, port)
        if peer.connect(torrent.info_hash, '-PC0001-123456789012'):
            print(f"Connected to peer {ip}:{port}")


if __name__ == '__main__':
    main()