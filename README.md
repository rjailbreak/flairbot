# flairbot
Flair bot used on /r/jailbreak and /r/iOSthemes.

We have a [custom php](http://rjailbreak.com/flair) (boo, I know, this was written 4+ years ago) which generates a message that is sent to this bot. This script just reads those messages from its inbox and assigns the user the pre-approved flair on their selected subreddit.

## Requirements

 - praw==4.4.0
 - Python 2.7.15 (Pretty sure it will work for all 2.7)
