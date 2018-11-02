import praw

print "||===============================Starting flairbot.py===============================||"

DEVICETYPE = {'200': 'iPad 1st gen',
              '201': 'iPad 2',
              '202': 'iPad 3rd gen',
              '203': 'iPad 4th gen',
              '204': 'iPad 5th gen',
              '205': 'iPad 6th gen',
              '206': 'iPad Air',
              '207': 'iPad Air 2',
              '208': 'iPad Pro 12.9',
              '209': 'iPad Pro 9.7',
              '210': 'iPad Pro 12.9, 2nd gen',
              '211': 'iPad Pro 10.5',
              '212': 'iPad Pro 12.9, 3rd gen',
              '213': 'iPad Pro 11',
              '214': 'iPad mini',
              '215': 'iPad mini 2',
              '216': 'iPad mini 3',
              '217': 'iPad mini 4',
              '300': 'iPhone 1st gen',
              '301': 'iPhone 3G',
              '302': 'iPhone 3GS',
              '303': 'iPhone 4',
              '304': 'iPhone 4S',
              '305': 'iPhone 5',
              '306': 'iPhone 5C',
              '307': 'iPhone 5S',
              '308': 'iPhone 6',
              '309': 'iPhone 6 Plus',
              '310': 'iPhone 6s',
              '311': 'iPhone 6s Plus',
              '312': 'iPhone SE',
              '313': 'iPhone 7',
              '314': 'iPhone 7 Plus',
              '315': 'iPhone 8',
              '316': 'iPhone 8 Plus',
              '317': 'iPhone X',
              '318': 'iPhone XR',
              '319': 'iPhone XS',
              '320': 'iPhone XS Max',
              '400': 'iPod touch 1st gen',
              '401': 'iPod touch 2nd gen',
              '402': 'iPod touch 3rd gen',
              '403': 'iPod touch 4th gen',
              '404': 'iPod touch 5th gen',
              '405': 'iPod touch 6th gen'
              }
IOSTYPE = ["", "1.0", "1.0.1", "1.0.2", "1.1", "1.1.1", "1.1.2", "1.1.3", "1.1.4", "1.1.5", "2.0",
           "2.0.1", "2.0.2", "2.1", "2.1.1", "2.2", "2.2.1", "3.0", "3.0.1", "3.1", "3.1.1",
           "3.1.2", "3.1.3", "3.2", "3.2.1", "3.2.2", "4.0", "4.0.1", "4.0.2", "4.1", "4.2",
           "4.2.1", "4.3", "4.3.1", "4.3.2", "4.3.3", "4.3.4", "4.3.5", "5.0", "5.0.1", "5.1",
           "5.1.1", "6.0", "6.0.1", "6.0.2", "6.1", "6.1.1", "6.1.2", "6.1.3", "6.1.4", "6.1.5",
           "6.1.6", "7.0", "7.0.1", "7.0.2", "7.0.3", "7.0.4", "7.0.5", "7.0.6", "7.1", "7.1.1",
           "7.1.2", "8.0", "8.1", "8.1.1", "8.1.2", "8.1.3", "8.2", "8.3", "8.4", "8.4.1", "9.0",
           "9.0.1", "9.0.2", "9.1", "9.2", "9.2.1", "9.3", "9.3.1", "9.3.2", "9.3.3", "9.3.4",
           "9.3.5", "10.0.1", "10.0.2", "10.0.3", "10.1", "10.1.1", "10.2", "10.2.1", "10.3",
           "10.3.1", "10.3.2", "10.3.3", "11.0", "11.0.1", "11.0.2", "11.0.3", "11.1", "11.1.1", 
           "11.1.2", "11.2", "11.2.1", "11.2.2", "11.2.5", "11.2.6", "11.3", "11.3.1", "11.4 beta", "11.4", "11.4.1", "12.0", "12.0.1", "12.1", "12.1.1 beta"
           ]

subNames = {0: "jailbreak and iOSThemes",
            1: "jailbreak",
            2: "iOSThemes"}


def main():

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
