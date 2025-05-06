import tkinter as tk
from tkinter import filedialog, messagebox

from torrent import Torrent
from tracker import Tracker
from peer import Peer

class TorrentClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BitTorrent Client")

        self.label = tk.Label(root, text="No torrent loaded", font=('Arial', 14))
        self.label.pack(pady=10)

        self.load_button = tk.Button(root, text="Load .torrent File", command=self.load_torrent)
        self.load_button.pack(pady=5)

        self.info_text = tk.Text(root, width=60, height=15, state='disabled')
        self.info_text.pack(padx=10, pady=10)

        self.connect_button = tk.Button(root, text="Connect to Peer", command=self.connect_to_peer, state='disabled')
        self.connect_button.pack(pady=5)

        self.torrent = None
        self.peers = []

    def load_torrent(self):
        file_path = filedialog.askopenfilename(filetypes=[("Torrent files", "*.torrent")])
        if not file_path:
            return
        try:
            self.torrent = Torrent(file_path)
            self.tracker = Tracker(self.torrent)
            self.peers = self.tracker.get_peers()

            self.info_text.config(state='normal')
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, f"Name: {self.torrent.name.decode()}\n")
            self.info_text.insert(tk.END, f"Length: {self.torrent.length} bytes\n")
            self.info_text.insert(tk.END, f"Pieces: {len(self.torrent.pieces)}\n")
            self.info_text.insert(tk.END, f"Tracker returned {len(self.peers)} peers.\n")
            self.info_text.config(state='disabled')

            self.label.config(text="Torrent loaded successfully")
            self.connect_button.config(state='normal')

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load torrent: {e}")

    def connect_to_peer(self):
        if not self.peers:
            messagebox.showwarning("No peers", "No peers found to connect.")
            return

        ip, port = self.peers[0]
        peer = Peer(ip, port)
        try:
            peer.connect(self.torrent.info_hash, '-PC0001-123456789012')
            messagebox.showinfo("Success", f"Connected to peer {ip}:{port}")
        except Exception as e:
            messagebox.showerror("Connection Failed", f"Could not connect to peer: {e}")


if __name__ == '__main__':
    root = tk.Tk()
    app = TorrentClientGUI(root)
    root.mainloop()