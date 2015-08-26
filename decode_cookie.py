#!/usr/bin/env python
# The MIT License (MIT)
# 
# Copyright (c) 2015 Vincent Ruijter
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
import sys

def parse_cookie(cookie):
	try:
		hex_pip = cookie.split('ffff')[1]
		hex_ip = hex_pip.split('o')[0]

		if (len(hex_ip) > 8) or (len(hex_ip) < 8):
			print("[-] This does not seem to be a valid cookie value.")
			sys.exit(1)

		port = hex_pip.split('o')[1]

	except IndexError as e:
		print("[-] Error parsing the value: %s" %e)
		sys.exit(1)
	
	return decode_ip(hex_ip, port)

def decode_ip(hex_ip, port):
	id = 2
	decoded_ip = []
	try:
		for i in range(0, len(hex_ip), 2):
			if id == len(hex_ip):
				decoded_ip.append(str(int(hex_ip[i:id], 16)))
				break
			decoded_ip.append(str(int(hex_ip[i:id], 16))+'.')
			id = id+2
	
	except ValueError as e:
		print("[-] Something wrong with the HEX values: %s" %e)
		sys.exit(1)		

	return ''.join(decoded_ip)+":%s" %port
	
def main():
	try:
		print("[+] Value decoded: %s"% parse_cookie(sys.argv[1]))
	except IndexError:
		print("[-] Please specify a value")

if __name__=='__main__':
	main()
