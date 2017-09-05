import time
import json

from slackclient import SlackClient
log = open("data",'a')
token = "your key here"# found at https://api.slack.com/web#authentication
sc = SlackClient(token)
if sc.rtm_connect():
        while True:
                xline = sc.rtm_read()
                time.sleep(1)
                try:
                    jline = json.load(xline[0])
                except:
                    continue
                print jline
                print type(jline)
                #log.write(str(xline))
else:
    print "Connection Failed, invalid token?"
