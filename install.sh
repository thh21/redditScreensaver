#!/bin/bash
# ------------------------------------------------------------------
# [Thom H (https://github.com/thh21)] Reddit Screensaver Installer
#          https://github.com/thh21/redditScreensaver
#		   Creates and Installs necessary files in ~/.redditScreensaver
# 		   Sets up a cron task the to run the script each day 12 noon
# 		   Runs the script once at the end
# ------------------------------------------------------------------

PY="$(which python)"
mkdir $HOME/.redditScreensaver
cp ./redditScreensaver.py $HOME/.redditScreensaver/
cp subreddits.json $HOME/.redditScreensaver/
mkdir $HOME/.redditScreensaver/images

crontab -l > tmpcron

echo "0 12 * * * $PY $HOME/.redditScreensaver/redditScreensaver.py" >> tmpcron
crontab tmpcron
rm tmpcron

python $HOME/.redditScreensaver/redditScreensaver.py

