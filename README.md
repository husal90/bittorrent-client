# Simple BitTorrent Client

A lightweight, Python-based BitTorrent client that implements the core functionality of the BitTorrent protocol. This client allows you to load and parse torrent files, connect to trackers, and interact with peers in the BitTorrent network.

## Features

- Parse and decode `.torrent` files
- Connect to trackers to obtain peer lists
- Establish connections with peers using the BitTorrent protocol
- User-friendly graphical interface for easy interaction
- Implementation of Bencode encoding/decoding

## Project Structure

- **bencode.py**: Implementation of the Bencode encoding/decoding used in BitTorrent
- **torrent.py**: Class for parsing and handling torrent metadata
- **tracker.py**: Communication with BitTorrent trackers
- **peer.py**: Handles peer connections and protocol messaging
- **client.py**: Command line interface for the BitTorrent client
- **gui.py**: Graphical user interface for the BitTorrent client

## Installation

### Prerequisites

- Python 3.6 or higher
- Tkinter (for GUI)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/husal90/bittorrent-client.git
   cd bittorrent-client
   ```

2. Run the client:
   - For command line interface:
     ```
     python client.py
     ```
   - For graphical interface:
     ```
     python gui.py
     ```

## Usage

### Command Line Interface

The command line interface is designed for simple testing and demonstration:

```python
python client.py
```

This will try to load a default torrent file named 'ubuntu.torrent' and connect to its first available peer.

### Graphical Interface

The GUI provides a more user-friendly way to interact with the client:

1. Run `python gui.py`
2. Click "Load .torrent File" and select a torrent file
3. Once loaded, information about the torrent will be displayed
4. Click "Connect to Peer" to establish a connection with one of the available peers

## Technical Details

### Technologies and Programming Languages

This project is developed using:

- **Python 3**: The entire codebase is written in Python, leveraging its simplicity and extensive standard library
- **Socket Programming**: Used for low-level network communications with peers
- **Tkinter**: Python's standard GUI toolkit for creating the graphical user interface
- **urllib**: Python's URL handling module for HTTP requests to trackers
- **hashlib**: For cryptographic hash functions, particularly SHA-1 for info hash generation
- **struct**: For binary data packing and unpacking in the peer protocol

### BitTorrent Protocol Implementation

This client implements the core aspects of the BitTorrent protocol:

- **Bencode**: A serialization format used to encode and decode BitTorrent data
- **Tracker Protocol**: Communication with trackers using HTTP to obtain peer lists
- **Peer Protocol**: Establishing connections with peers including the BitTorrent handshake

### Bencode Format

Bencode is a simple encoding used in the BitTorrent protocol for encoding and decoding data. It supports:

- Strings: `<length>:<string>`
- Integers: `i<number>e`
- Lists: `l<bencoded values>e`
- Dictionaries: `d<bencoded key><bencoded value>...e`

## Future Improvements

- Implement piece downloading and file assembly
- Add support for multiple simultaneous peer connections
- Implement seeding capabilities
- Add download progress tracking and visualization
- Support for magnet links

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The BitTorrent protocol specification
- The Python community for excellent networking libraries
