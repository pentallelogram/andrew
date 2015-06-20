# Andrew Lewis

<h1>Summary</h1>
This repo contains custom exploits that I have written or modified from proof of concept exploits.

Cesar_FTP.py - a buffer overflow exploit, modified by me.

Ricoh_FTP.py - a buffer overflow exploit, modified by me.

realvnc.py - an authentication bypass attack on RealVNC 4.1.1 & 4.1.0, written by me.

Soritong_MP3.py - Soritong MP3 v1.0 SEH exploit, written by me with help from corelan.be.

FreeFloat_FTP.py - Free Float FTP v1.0 simple buffer overflow tested on Windows XP Pro SP3, written by me with help from fuzzysecurity.com.

DVD_X_Player - DVD X Player 5.5 Professional SEH buffer overflow. Creates a malicous .plf file that must be ran in a debugger since the SEH overflow vulnerability is behind a standard buffer overflow without SEH. Tested on Windows XP Pro SP3. Written by me with help from fuzzysecurity.com.

Kolibri_HTTP.py - Kolibri Webserver v2.0 (2008-10-15) tested on Windows XP Pro SP3. Buffer overflow uses a small egg hunter to find large (743 byte) x86/alpha_mixed encoded shellcode. Written by Andrew Lewis with help from fuzzysecurity.com.

Trilogic_Media_Player.py - Trilogiv Media Player 8 contains a Unicode SEH based buffer overflow tested on Windows XP Pro SP3. This script creates evil.m3u which will create a shell on port 9988. Written by Andrew Lewis with help from fuzzysecurity.com.

Mini_Stream_MP3.py - Mini-stream RM-MP3 Converter Version 3.1.2.1.2010.03.30, Buffer Overflow tested on Windows 7 Professional SP1. Uses ROP as DEP mitigation to pop calc.exe. Written by Andrew Lewis with help from fuzzysecurity.com.

IE_v7.html - A heap spray buffer overflow for Internet Explorer v7 and earlier. Tested on Windows XP SP3 x86. Written by Andrew Lewis with help from fuzzysecurity.com.

CommuniCrypt.html - A heap spray buffer overflow for CommuniCrypt Mail on IE6 and 7, overwrites SEH handlers. Written by Andrew Lewis with help from Corelan.be.