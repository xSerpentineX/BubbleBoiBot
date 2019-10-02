# BubbleBoiBot v1.72
This bot is a complete remake of alekxeyuk's original Python bot that adds countless new features along with fixing other features to make them more user friendly. You can view any disclaimers at the bottom of this text.


# Features:
- 100% Free and Opensource at GitHub.
+ You can run eighteen bots per computer.
- You can customize settings easily within the `settings.json` file.
+ Automatic drawing of custom images with two algorithms; cluster (fast, low quality) or yliluoma (slow, high quality).
- Automatic reconnection when kicked so you can leave the bot running without constantly monitoring it.
+ .bat support so you can run all eighteen bots from a single click without taking up the entire screen.
- Optional automatic spam that avoids muting.
+ Optional spam formatting that converts any fullstops (periods) into commas for easy link spamming.
- Optional automatic searching for users with a specified username.
+ Seven colour themes for the bot console.
- Our discord server got removed and old discount account got terminated. RIP.
+ A simple bat GUI on starting to make it easier to use.


# How to install the bot:
1. Download Python 3.7.4 here: https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe

2. When installing Python 3.7.4, check the, "Install to PATH", checkbox then click, "Custom installation". Check every box and leave the default save location as default (Do not click browse!)

3. Download the bot at the releases tab: https://github.com/TheLoveableBananaNoodle/BubbleBoiBot/releases. If you don't do this, GitHub will convert the ANSI to UTF-8 and it will cause the .bat GUI to look as though it has been corrupted.

4. Do `windows + s` and type in the search, "Windows power shell". Right click it and then click, "Run as administrator."

5. In the windows shell, enter the following command:
```
pip install websockets aiohttp python-socketio requests Pillow numpy commentjson colorama
```
6. To run the bot, head to the BubblyBoiBot folder (not the ZIP, the folder you extracted) and click the `launcher.bat` file.


**Thank you for installing the bot!**


# How to customize the bot:
Open the `settings.json` file with your text editor and customize the bot with the following options:

`"ColourTheme": "plain"`: You can change this to either `emerald`, `fire`, `ocean`, `storm`, `candy`, `gold` or `plain`.

`"BrightOrDim": "bright"`: You can change this to either `bright` or `dim`, which will affect how bright the bot text is.

`"BotName": "BubblyBoiBot"` You can change the bot name when connection to a server here.

`"Port": 5001` You do not have to change this unless you're using private games.

`"Join": ""` To join a private game, add the code here (The string of characters found after the '?' in the server link). You'll have to test each port to see if it works.

`"Language": "English"` Select what servers you wish to join (i.e Join the English servers).

`"RandomAvatar": false` If this is set to false the avatar will be transparent. If set to true, your avatar will be random.

`"Shuffle": false` Draw the image randomly as opposed to moving up or down the image. Don't get this confused with "RandomImage".

`"SpamServer": true` Set this to true if you want to automatically spam a server.

`"SpamMessage": "Replace this text with spam text."`: Set this to your spam message. Do not use 100+ characters.

`"AutomaticFormatting": false`: Use this if you want to automatically convert all fullstops (periods) into commans.

`"RandomImage": false` Select a random image from the `images` folder.

`"ImageToDraw": ""` If "RandomImage" is false, specify the image here. Image must be in the `images` folder.

`"Algorithm": "cluster" or "yliluoma"`: Set the drawing algorithm to either cluster or yliluoma.

`"AnnounceWord": false`: If "AnnounceWord" is true, the bot will announce the real word to chat before drawing. If false, it will not.

`"OnlyUser": false` Enable the automatic searching feature.

`"OnlyUserName": "yourusernamehere"` Specify which username to search for.


All files in the `images` folder must be images.
Image names are case and symbol sensitive and you must include the file extension.
Images must be JPG/JPEG/BMP.


# Common Errors:
```
connection established.
disconnected from server.
disconnected from server.
```
This error means a number of different things. Either the servers are full, which can be solved easily by waiting or joining a different language; You're running too many bots on one port, which can be solved easily by closing some bots on one port; or the skribbl.io website has targetted your PC on suspicion (this happens a lot when you use the bot to search for users) which can be solved by using a VPN. ProtonVPN would be a good VPN to use for this.

`ValueError: operands could not be broadcast together with shapes (150, 200) and (150, 200, 3)` You must use JPG/JPEG images.

Please report any errors you get to Catterall#6723. If I get the error commonly, I will add it to this list.


# Disclaimers
- Disclaimer No.1: VirusTotal states, "57/58 scanners, including Avast, AVG, McAfee, Norton, claim that this is malware free. The only scanner that claims virus is obsecure, and claims it is adware, more than likely due to spamming.


- Disclaimer No.2: There is a differance between a potentially unwanted program (PUP) and malware.


- Disclaimer No.3: Quiet.exe is only used if `hidden` option is enabled in the `config.ini` file in the exec folder. If `hidden` option is not enabled you can remove `quiet.exe`.


# Thank You, Catterall#6723 (That's my discord).
