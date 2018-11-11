# flairbot
Flair bot used on /r/jailbreak and /r/iOSthemes.

On rjailbreak.com/flair (also [open source](https://github.com/rjailbreak/website-flair)), you can set your user flair (the text that comes after your username) by generating a message which is sent to this bot. This script just reads those messages from the bot's inbox and assigns the user the pre-approved flair on their selected subreddit.

## Requirements

 - praw==4.4.0
 - Python 2.7.15 (Pretty sure it will work for all 2.7)
