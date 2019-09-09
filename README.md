Disclaimer No.1: VirusTotal states, "57/58 scanners, including Avast, AVG, McAfee, Norton, claim that this is malware free. The only scanner that claims virus is obsecure, and claims it is adware, more than likely due to spamming.


Disclaimer No.2: There is a differance between a potentially unwanted program (PUP) and malware.


Disclaimer No.3: Quiet.exe is only used if `hidden` option is enabled in the `loopAll.config` file in the exec folder. If `hidden` option is not enabled you can remove `quiet.exe`.


# BubbleBoiBot v1.7
This bot is a complete remake of alekxeyuk's original Python bot that adds countless new features along with fixing other features to make them more user friendly.


# Features:
- 100% Free and Opensource at GitHub.
+ You can run eighteen bots per computer.
- You can customize settings easily within the settings.json file.
+ Automatic drawing of custom images with two optional algorithms; cluster or yliluoma.
- Automatic reconnection when kicked so you can leave the bot running without constantly monitoring it.
+ .bat support so you can run all eighteen bots from a single click without taking up the entire screen.
- Optional automatic spam that avoids muting.
+ Optional spam formatting that converts any fullstops (periods) into commas for easy link spamming.
- Optional automatic searching for users with a specified username.
+ Seven colour themes for the bot console.
- A community discord with over seventy members including support channels and support bots (ModMail).


# How to install the bot:
1. Download Python 3.7.4 here: https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe

2. When installing Python 3.7.4, check the, "Install to PATH", checkbox then click, "Custom installation". Check every box and leave the default save location as default (Do not click browse!)

3. On this GitHub page, click the green, "Clone or download." Button and then click, "Download as ZIP." Then, extract the ZIP file somewhere on your computer. You will need to come to this file to run the bot, so save it somewhere rememerable.

4. Do `windows + s` and type in the search, "Windows power shell". Right click it and then click, "Run as administrator."

5. In the windows shell, enter the following command:
```
pip install websockets aiohttp python-socketio requests Pillow numpy commentjson colorama
```
6. To run the bot, head to the BubblyBoiBot folder (not the ZIP, the folder you extracted) and click the `loopAll.bat` file.


**Thank you for installing the bot! We'd be even more thankful if you joined our discord server from the URL inside the file. You can use the discord server for support with installation and discussion with brand new friends.**
(We also have many great discord bots in our server!)


# How to customize the bot (loopAll.config):
In the `loopAll.config` file (Inside the exec folder), you will find the following options: `hidden`, `delay`, `devSkip` and `startTimes`. `hidden` is set to false by default. Setting it to true will cause the bot windows to become hidden to the user outside of the task manager. Leaving it as false will set the bot windows to open minimized. `delay` sets how long the delay is between each bot starting. The default value is 1. `devSkip` simply stops any bots from running when using the `loopAll.bat` file. It is set to false by default and is only really used when testing the simple interface of the `loopAll.bat` program. Finally, `startTimes` sets how many bots will open on each of the three Skribbl.io ports (port5001, port5002, port5003) when running `loopAll.bat`. The default is 6. From testing, it appears the maximum is also six bots per port (Meaning at optimal time and without any errors, you can run up to eighteen bots on one computer).


# How to customize the bot:
Open the `settings.json` file with your text editor and customize the bot with the following options:

`"ColourTheme": "plain"`: You can change this to either `emerald`, `fire`, `ocean`, `storm`, `candy`, `gold` or `plain`.

`"BrightOrDim": "dim"`: You can change this to either `bright` or `dim`, which will affect how bright the bot text is.

`"BotName": "BubblyBoiBot"` You can change the bot name when connection to a server here.

`"Port": 5001` You do not have to change this unless you're using private games.

`"Join": ""` To join a private game, add the code here (The string of characters found after the '?' in the server link). You'll have to test each port to see if it works.

`"Language": "English"` Select what servers you wish to join (i.e Join the English servers).

`"RandomAvatar": false` If this is set to false the avatar will be transparent. If set to true, your avatar will be random.

`"Shuffle": false` Draw the image randomly as opposed to moving up or down the image. Don't get this confused with "RandomImage".

`"SpamServer": true` Set this to true if you want to automatically spam a server.

`"SpamMessage": "REPLACE THIS TEXT WITH THE TEXT YOU WANT TO SPAM"`: Set this to your spam message. Do not use 100+ characters.

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
This error means either; You are running too many bots one port or the server the bot tried to connect to was full. Solution: If the problem is caused by running more than six bots on one port, close any excessive bots on that port. There isn't exactly a solution to cause B other than, "Try again later".

`ValueError: operands could not be broadcast together with shapes (150, 200) and (150, 200, 3)` You must use JPG/JPEG images.

Please report any errors you get to PotassiumSnek#6853. If I get the error commonly, I will add it to this list.
# Thank You, PotassiumSnek#6853 (That's my discord).
# Join our community discord: https://discord.gg/38n5TYK
