import socket
import struct


def main():
    connection = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, proto=768)
    while True:
        raw_data, address = connection.recvfrom(65536)
        dest_mac, src_mac, proto, data = ethernet_frame(raw_data)
        print(dest_mac)
        print(src_mac)
        print(proto)
        print(data)
        print("="*50)


def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack("!6s6sH", data[:14])
    return get_mac_address(dest_mac), get_mac_address(src_mac), socket.htons(proto), data[14:]

def get_mac_address(byte_address):
    bytes_str = map('{:02x}'.format, byte_address)
    address = ':'.join(bytes_str).upper()
    return address

main()
