"""
	Use the same techniques such as (but not limited to):
	1) Sockets
	2) File I/O
	3) raw_input()

	from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "wattsamp.net" # IP address here
port = 1337 # Port here

global_prompt = "> "
dir = ""

def execute_cmd(cmd, prompt):
	"""
		Sockets: https://docs.python.org/3/library/socket.html
		How to use the socket s:

		# Establish socket connection
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))

		Reading:

			data = s.recv(1024)     # Receives 1024 bytes from IP/Port
			print(data)             # Prints data

		Sending:

 			s.send("something to send\n")   # Send a newline \n at the end of your command
	"""
	if cmd == "help":

		print("shell, pull <remote-path> <local-path>, help, quit, exit")
	elif cmd == "shell":

		int exit = 0

		global_prompt = "/" + global_prompt

		while exit = 0:

			inner_cmd = input(global_prompt)

			print("\n")

			if inner_cmd = = ("exit" || "quit"):

				exit = 1
			else:

				execute_cmd(inner_cmd, global_prompt)

			print("\n")

		global_prompt = "> "

	else:

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))

		time.sleep(1)


		data = s.recv(1024)


		s.send(cmd)

		time.sleep(1)

		data = s.recv(1024)
		print(data)


if __name__ == '__main__':
	int exit = 0

	while exit == 0:

		cmd = input(global_prompt)

		print("\n")

		if cmd == ("exit" || "quit"):

			exit = 1
		else:

			execute_cmd(cmd, global_prompt)

		print("\n")
