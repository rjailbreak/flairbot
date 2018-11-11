import praw, urllib, json

USERNAME=''
USER_AGENT=''

print "||===============================Starting flairbot.py===============================||"

url = "https://raw.githubusercontent.com/rjailbreak/flairbot/master/data.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data

IOSTYPE = data.versions
subNames = data.subreddits

DEVICES = dict()
DEVICES.update(data.devices.iPad)
DEVICES.update(data.devices.iPhone)
DEVICES.update(data.devices.iPod)

def main():
    global USERNAME
    global USER_AGENT
    r = praw.Reddit(USERNAME, user_agent=USER_AGENT)
    print 'Searching Inbox.'
    pms = r.inbox.unread(mark_read=True, limit=100)
    for pm in pms:
        if not pm.author:
            pm.mark_read()
            print "User was deleted"
            continue
        pauthor = pm.author
        pbody = pm.body
        psubject = pm.subject
        if psubject == "Flair Request":
            arr = pbody.split("\n")
            error = 0
            device = ""
            ios = ""
            sub = 3
            # device
            try:
                if arr[0].startswith("0"):
                    value = int(arr[0][1:])
                    device = DEVICETYPE[str(value)]
                else:
                    error = 1
                if arr[1].startswith("1"):
                    value = int(arr[1][1:])
                    if value != 0:
                        device += ", "
                        ios = "iOS " + IOSTYPE[value]
                else:
                    error = 1
                if arr[2].startswith("2"):
                    sub = int(arr[2][1:])
            except:
                error = 1
            if error == 1:
                pauthor.message('Flair Rejected on /r/jailbreak',
                                ('You edited something in the message before sending or ' +
                                 'something went wrong. Please try again.'))
                print "Flair rejected: " + device + ios
            else:
                flairText = device + ios
                if sub != 0:
                    try:
                        r.subreddit(subNames[sub]).flair.set(
                            redditor=pauthor.name, text=flairText, css_class="flair-default")
                        subText = "/r/" + subNames[sub]
                    except Exception:
                        print "Author deleted"
                        pm.mark_read()
                        continue
                else:
                    r.subreddit('jailbreak').flair.set(redditor=pauthor.name,
                                                       text=flairText, css_class="flair-default")
                    r.subreddit('iOSThemes').flair.set(redditor=pauthor.name,
                                                       text=flairText, css_class="flair-default")
                    subText = "/r/jailbreak and /r/iOSthemes"
                pauthor.message('Flair Approved', 'Your subreddit flair, "' + flairText +
                                '" on ' + subText + ' has been approved. Thank you for using ' +
                                '/u/JailbreakFlairBot which was created by /u/ibbignerd.')
                print "Approved flair, \"" + flairText + "\" for " + pauthor.name + " on " + subText
            pm.mark_read()
        else:
            pm.mark_read()
    print "Done!"


if __name__ == '__main__':
    main()
