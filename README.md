# Reddit Screensaver

A simple python script that will pull down images from different subreddits each day of the week. Desinged to be used to poplate a directory of images for OS X screensaver slideshows.

This script is designed to work best with the [SFW Porn Network](https://www.reddit.com/r/sfwpornnetwork/wiki/network) as it only supports statically linked images or none albumed imgur links.

## Installation

### Automatic
- Set up the script
	- Download zip, extract and run install.sh. 
- Set the screensaver source directory
	- Go to system preferences -> desktop & screensaver -> screensaver. 
	- Choose a slideshow screensaver
	- For source choose folder **~/.redditScreensaver/images**

This will install file in $HOME/.redditScreensaver, set up a cron task to run the program each day at 12 noon and run the script once to populate the file.

### Manual

- Create directory structure **~/.redditScreensaver/images**
- Copy *rdditScreensaver.py* and *subreddits.json* to **~/.redditScreensaver**
- schedule *redditScreensaver.py to run each day whith cron or automator or something
- Set the screensaver source directory (*see autmatic installation instrutions*)

## Customisation

Subreddits for each day are taken from the *subreddits.json* file. You can change add and remove these as desired. The basic structure is shown below where *pages* is a list of the subreddits you wish to use, this can be one or many and *type* is the type of page. 

```
	"monday":{
		"type":"r", 
		"pages":[
			"earthporn",
			"spaceporn"
		]
	},
```

The script supports normal subreddits or multisubreddits

`"type":"r"`

e.g.
> https://www.reddit.com/r/earthporn
or 
> https://www.reddit.com/r/earthporn+spaceporn

The Script also supports user saved lists e.g.
for 
> https://www.reddit.com/user/gremy0/m/sfwpornnetwork

`"type":"user"`

and

`"pages":["gremy0/m/sfwpornnetwork"]`

The default subreddits.json file has examples of each of these.

