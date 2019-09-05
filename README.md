Disclaimer No.1: VirusTotal states, "57/58 scanners, including Avast, AVG, McAfee, Norton, claim that this is malware free. The only scanner that claims virus is obsecure, and claims it is adware, more than likely due to spamming.


Disclaimer No.2: There is a differance between a potentially unwanted program (PUP) and malware.


Disclaimer No.3: Quiet.exe is only used if `hidden` option is enabled in the `loopAll.config` file in the exec folder. If `hidden` option is not enabled you can remove `quiet.exe`.


# BubbleBoiBot
This bot is a remake of a bot created by alekxeyuk that adds an easier command line interface, the ability to easily run eighteen bots at the same time and adds an easier spam configuration.


# Features:
- 18 Bots per computer, easily managed via a .bat file.
- Customizable features in both `BubblyBoiBot.py` and `loopAll.config`.
- Auto-Spam (Now takes use of file handling to make customization even easier (As of 5th September 2019)!
- Auto-Drawing that uses an image search to search custom keywords.
- Auto-Reconnect so you can leave the bot running without worrying about kicks.
- Random Avatar selector to stop suspiscion.


# How to install the bot:
1. Download Python 3.7.4 here: https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe

2. When installing Python 3.7.4, check the, "Install to PATH", checkbox then click, "Custom installation". Check every box and leave the default save location as default (Do not click browse!)

3. On this GitHub page, click the green, "Clone or download." Buton and then click, "Download as ZIP." Then, extract the ZIP file somewhere on your computer. You will need to come to this file to run the bot, so save it somewhere rememerable.

4. Do `windows + s` and type in the search, "Windows power shell". Right click it and then click, "Run as administrator."

5. In the windows shell, enter the following command:
```
pip install websockets aiohttp python-socketio requests Pillow google_images_download numpy
```
6. To run the bot, head to the BubblyBoiBot folder (not the ZIP, the folder you extracted) and click the `loopAll.bat` file.


# Thank you for installing the bot! We'd be even more thankful if you joined our discord server from the URL inside the file. You can use the discord server for support with installation and discussion with brand new friends.
(We also have many great discord bots!)


# How to customize the bot (loopAll.config):
In the `loopAll.config` file (Inside the exec folder), you will find the following options: `hidden`, `delay`, `devSkip` and `startTimes`. `hidden` is set to false by default. Setting it to true will cause the bot windows to become hidden to the user outside of the task manager. Leaving it as false will set the bot windows to open minimized. `delay` sets how long the delay is between each bot starting. The default value is 1. `devSkip` simply stops any bots from running when using the `loopAll.bat` file. It is set to false by default and is only really used when testing the simple interface of the `loopAll.bat` program. Finally, `startTimes` sets how many bots will open on each of the three Skribbl.io ports (port5001, port5002, port5003) when running `loopAll.bat`. The default is 6. From testing, it appears the maximum is also six bots per port (Meaning at optimal time and without any errors, you can run up to eighteen bots on one computer).

# How to customize the bot (BubblyBoiBot.py + spam.txt):
Line 17: `SETTINGS = {'port': '5001', 'join': '', 'language': 'English', 'x': 3, 'y': 4, 'shuffle': True}`                                 `'port': 'x'` This can be used to determine whether the bot runs on port5001, 5002 or 5003 when not being ran from any of the .bat files. `'join': ''` Put a private game key (the string of characters after the `?` in the game link) to join a private game. Test each port!
`'language': 'x'` You can set which language servers the bot will join here (i.e English will join the English servers).
`'x': 'num', 'y': 'num'` I have no idea what this does. Don't touch it unless you know what you're doing.
`shuffle: x` I'd suggest leaving this to True.

Line 67: `arguments = {"keywords": "dick", "limit":10, "print_urls":False, 'no_download':True, 'safe_search':True, 'exact_size':'355,294', 'type': 'photo', 'format': 'jpg'}`                                                                               `"keywords": "dick"` Dick is the default value. This is what word(|s) the bot will search for in google images to draw.                 `"limit:10"` You can leave this as 10.
`"print_urls"` You can leage this as False.
`"no_download": x` Set to True by default, determines whether your image will be downloaded to a folder within the project.
`'safe_search': x` Will safe search by on when the bot searches for keyword specified in `"keywords": "x"`.
`'exact_size': 'w','h'` What exact size of image will the bot search for on Google Images using the keyword in `"keywords: "x"`.
`'type': 'x'` What type of picture will the bot search for on Google Images. I'd reccomend `'type': 'clipart'`. Default is photo.
`'format': 'x'` I'd suggest leaving this as jpg.

Line 107: `await sio.emit('userData' , {"name": "BubblyBoiBot", "code":"", "avatar": [num1, num2, num3, num4], "join": SETTINGS['join'], "language": SETTINGS['language'], "createPrivate": False})` `"name": "x"` This can be used to change the name of the bot when it joins the server. `"code:""` You can leave this blank. `"avatar": [num1, num2, num3, num4]` This is used to set your avatar. Set all as -1 to look invisible. Set all as a number for its relative avatar. Leave all as num1, num2, num3 and num4 for a random avatar.


# How to turn off auto-spam:
Open `spam.txt` and leave line one completely blank.


# How to stop the bot from giving the word before drawing:
Go to Line 219 and put a `#` in front of it to cancel it out.


# Common Errors:
```
connection established.
disconnected from server.
disconnected from server.
```
This error means either; You are running too many bots one port or the server the bot tried to connect to was full. Solution: If the problem is caused by running more than six bots on one port, close any excessive bots on that port. There isn't exactly a solution to cause B other than, "Try again later".

`Error: NoneType has no size attribute` This error means either; The image searched for by the bot doesn't work or you messed the code up somewhere. Solution: If caused by search, change the keyword you used. Remember to make `'exact_size': 'w', 'h'` the same size as the image you wanted from Google Images. If caused by messing up the code, try extracting the bot from the ZIP file again to completely redo any changes to the BubblyBoiBot.py file, or try `Ctrl+Z`ing out of it.

# Thank You, PotassiumSnek#6853 (That's my discord).
# Join our community discord: https://discord.gg/38n5TYK
