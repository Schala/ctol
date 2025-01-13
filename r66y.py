from enum import IntEnum
import socket
import sys

class Character(IntEnum):
	CRONO = 1
	MARLE = 2
	LUCCA = 3
	FROG = 4
	ROBO = 5
	AYLA = 6
	MAGUS = 7

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.connect((sys.argv[1], 12345))
	sock.sendall(f"1#0#{Character.FROG}".encode("utf-8"))
