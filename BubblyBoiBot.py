import os
import sys
import json
import time
import string
import asyncio
import socketio
import requests
import colorama as color
import commentjson
import hitherdither
from io import BytesIO
import random as r
from PIL import Image, ImageDraw, ImageFont

color.init(autoreset="true")

clear = True


def errexit(errcode, sleep):
    time.sleep(sleep)
    os._exit(errcode)

 
try:
    with open('settings.json') as settings_file:
        SETTINGS = commentjson.load(settings_file)
        messageLength = len(SETTINGS["SpamMessage"])
except Exception as e:
    print(f"{color.Back.RED}{color.Style.BRIGHT}Error: Loading json file.")
    print(e)
    errexit(1,5)


if len(SETTINGS["SpamMessage"]) > 100:
    under_101 = False
else:
    under_101 = True


async def sendSpamMessage():
    global under_101
    if SETTINGS["SpamServer"]:
        if not under_101:
            print(f"{color.Back.YELLOW}{color.Style.BRIGHT}Warning: Your message has {messageLength - 100} extra characters.")
        else:
            if SETTINGS["AutomaticFormatting"]:
                    await sio.emit("chat", f"{SETTINGS['SpamMessage']}".replace(".", ","))
            else:
                    await sio.emit("chat", f"{SETTINGS['SpamMessage']}")

    
if not (SETTINGS["Algorithm"].lower() == 'cluster' or SETTINGS["Algorithm"].lower() == 'yliluoma'):
    print(f"{color.Back.RED}{color.Style.BRIGHT}Error: Algorithm \"{SETTINGS['Algorithm']}\" was not found. See settings.json and change \"Algorithm\" to \"cluster\" or \"yliluoma\".")
    errexit(1,5)

if not (SETTINGS["Port"] == 5001 or SETTINGS["Port"] == 5002 or SETTINGS["Port"] == 5003):
    print(f"{color.Back.RED}{color.Style.BRIGHT}Error: Port {SETTINGS['Port']} does not exist. See settings.json and change \"Port\" to 5001, 5002 or 5003.")
    errexit(1,5)

if len(sys.argv) == 2:
    """
    U can set port using command line
    """
    SETTINGS['Port'] = sys.argv[1]


GAME_DATA = {'died': False}
sio = socketio.AsyncClient(logger=False, reconnection=True)  # U can turn logger True, if u need to catch events that are not described in current version of program


"""
Game palette
"""
palette = hitherdither.palette.Palette(
    [0xFFFFFF, 0x000000, 0xC1C1C1, 0x4C4C4C,
     0xEF130B, 0x740B07, 0xFF7100, 0xC23800,
     0xFFE400, 0xE8A200, 0x00CC00, 0x005510,
     0x00B2FF, 0x00569E, 0x231FD3, 0x0E0865,
     0xA300BA, 0x550069, 0xD37CAA, 0xA75574, 
     0xA0522D, 0x63300D]
)


async def dither(word):
    if (SETTINGS["RandomImage"]):
        path = "images/"
        files = os.listdir(path)
        index = r.randrange(0, len(files))
        image2Draw = files[index]
    else:
        image2Draw = SETTINGS["ImageToDraw"]


    img = Image.open("images/" + image2Draw)
    img = img.resize((int(275), int(150)))
    print(f"{color.Back.GREEN}Drawing: {image2Draw} with {img.size}")
    if SETTINGS["Algorithm"].lower() == 'cluster':
        img_dithered = hitherdither.ordered.cluster.cluster_dot_dithering(img, palette, [1, 1, 1], 4)
        return img_dithered
    elif SETTINGS["Algorithm"].lower() == 'yliluoma':
        img_dithered = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(img, palette, order=8)
        return img_dithered


def GenRandomLine(length=8, chars=string.ascii_letters):
    """
    Generate random line
    """
    return ''.join([r.choice(chars) for i in range(length)])


@sio.on('connect')
async def on_connect():
    """
    On connection to the lobby we must introduce ourselves
    """
    print(f"{color.Back.GREEN}{color.Style.BRIGHT}Connection established")
    print()
    if (SETTINGS["RandomAvatar"]):
        num1 = r.randint(1, 5)
        num2 = r.randint(1, 5)
        num3 = r.randint(1, 5)
        num4 = r.randint(1, 5)
    else:
        num1 = -1
        num2 = -1
        num3 = -1
        num4 = -1

    await sio.emit('userData' , {"name": SETTINGS['BotName'], "code":"", "avatar": [num1, num2, num3, num4], "join": SETTINGS['Join'], "language": SETTINGS['Language'], "createPrivate": False})
    del num1,num2,num3,num4


@sio.on('lobbyConnected')
async def on_lobbyConnected(data):
    global clear
    """
    When we connected to the lobby we print out the current round, the number of players, the players names and their score, we also also store that info into GAME_DATA dict
    """
    print(f"{color.Fore.GREEN}{color.Style.BRIGHT}Lobby connected")
    print(f"{color.Fore.YELLOW}Round {data['round']} / {data['roundMax']}")
    print(f"{color.Fore.MAGENTA}{color.Style.DIM}There {len(data['players'])} players: ")

    doLeave = False
    for player in data['players']:
        print(f"    {color.Style.DIM}{player['id']} = {player['name']} > {player['score']}")

        if player['name'] == SETTINGS["OnlyUserName"] and SETTINGS['OnlyUser']:
            doLeave = True

    print()

    if not doLeave and SETTINGS['OnlyUser']:
        print(f"{color.Back.GREEN}Info: Leaving because {SETTINGS['OnlyUserName']} was not found.")
        await sio.disconnect()
        os._exit(1)

    GAME_DATA.update({'players' : {player['id'] : {'name': player['name'], 'score': player['score'], 'guessedWord': player['guessedWord']} for player in data['players']}})
    GAME_DATA.update({'myID': data['myID']})
    GAME_DATA.update({'round' : data['round']})

    if SETTINGS["SpamServer"]:
        await sendSpamMessage()


@sio.on('lobbyState')
def on_lobbyState(data):
    """
    When lobby change its state, we want to show that
    """
    print(f"{color.Back.WHITE}{color.Fore.BLACK}Lobby State: {data}")


@sio.on('lobbyCurrentWord')
def on_lobbyCurrentWord(data):
    """
    When lobby updates current word, we want to show this.
    """
    print(f"{color.Style.BRIGHT}Current Word: {data}")
    print()


@sio.on('chat')
async def on_chat(data):
    global clear
    """
    Chat function, prints username or id of user and their message
    """
    if 'players' in GAME_DATA.keys():
        print(f"{color.Style.DIM}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
        if clear == True:
            clear = False
            time.sleep(1.4)
            await sendSpamMessage()
            clear = True
    else:
        print(f"{color.Style.DIM}{data['id']} wrote > {data['message']}")


@sio.on('lobbyPlayerConnected')
async def on_lobbyPlayerConnected(data):
    """
    When someone enters the lobby, we want to know this, so this is what this function does
    """
    GAME_DATA['players'].update({data['id'] : {'name': data['name'], 'score': data['score'], 'guessedWord': data['guessedWord']}})
    print(f"{color.Fore.GREEN}{color.Style.DIM}{data['name']} connected.")


@sio.on('lobbyPlayerDisconnected')
async def on_lobbyPlayerDisconnected(data):
    """
    When someone leaves the lobby, we want to know this, so this is what this function does
    It also makes the bot leave if OnlyUser is enabled
    """
    print(f"{color.Fore.RED}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} left.")
    if SETTINGS["OnlyUser"] and GAME_DATA['players'][data]['name'] == SETTINGS["OnlyUserName"]:
        await sio.eio.disconnect(True)
        time.sleep(2)
        await start_server()


@sio.on('lobbyPlayerGuessedWord')
def on_lobbyPlayerGuessedWord(data):
    """
    When someone guesses a word, we want to know it, so this is what this function does
    """
    print(f"{color.Fore.CYAN}{GAME_DATA['players'][data]['name']} the guessed word!")


@sio.on('drawCommands')
def on_drawCommands(data):
    """
    Here can be your logic to work with draw data that we get from lobby, u can use kivy to easily draw that
    """
    pass


@sio.on('disconnect')
async def on_disconnect():
    """
    When we disconnected from server we need explicitly call eio.disconnect or Sio would stuck in forever wait loop
    """
    print(f"{color.Back.RED}Disconnected from server")
    await sio.eio.disconnect(True)


@sio.on('kicked')
def on_kicked():
    """
    The lobby can kick us, we can't do anything about it, at least I have no idea
    """
    print(f"{color.Back.RED}The lobby kicked us!")
    GAME_DATA['died'] = True


@sio.on('lobbyChooseWord')
async def on_lobbyChooseWord(data):
    """
    When the lobby says that someone can choose a word, we check that it is us
    """
    if data['id'] == GAME_DATA["myID"]:
        GAME_DATA.update({"word": data['words'][2]})   # We always choose the third word, you can change it the way you want it to work
        print(f"{color.Style.BRIGHT}I am drawing {data['words'][2]}")
        if SETTINGS["AnnounceWord"]:
            await sio.emit("chat", f"The actual word is: {data['words'][2]}.")
        await sio.emit("lobbyChooseWord", 2)


def image_optimize(img, x_size, y_size):
    """
    Pixels to line, optimization
    Not perfect but it works fast and good enough
    """
    draw_data_y = []
    draw_data_x = []
    img_x, img_y = img.size

    """
        THIS DRAWS FROM TOP TO BOTTOM FROM LEFT TO RIGHT
    """
    for x in range(x_size, img_x*x_size, x_size):
        color = img.getpixel((int(x/x_size), 0))
        color_start = 0
        for y in range(0, img_y*y_size, y_size):
            if img.getpixel((int(x/x_size), int(y/y_size))) != color:
                draw_data_y.append([[0, color, y_size, x, color_start, x, y]])
                color = img.getpixel((int(x/x_size), int(y/y_size)))
                color_start = y
            if y == img_y*y_size-y_size:
                draw_data_y.append([[0, img.getpixel((int(x/x_size), int(color_start/y_size))), y_size, x, color_start, x, y]])

    """
        THIS DRAWS FROM LEFT TO RIGHT FROM TOP TO BOTTOM
    """
    for y in range(y_size, img_y*y_size, y_size-1):
        color = img.getpixel((0, int(y/y_size)))
        color_start = 0
        for x in range(0, img_x*x_size, x_size):
            if img.getpixel((int(x/x_size), int(y/y_size))) != color:
                draw_data_x.append([[0, color, y_size, color_start, y, x, y]])
                color = img.getpixel((int(x/x_size), int(y/y_size)))
                color_start = x
            if x == img_x*x_size-x_size:
                draw_data_x.append([[0, img.getpixel((int(color_start/x_size), int(y/y_size))), y_size, color_start, y, x, y]])
    """
    Counting lines, that are not white
    """
    x = 0
    for line in draw_data_x: 
        if line[0][1] != 0:
            x += 1
    y = 0
    for line in draw_data_y:
        if line[0][1] != 0:
            y += 1

    print('y = ', y, 'x = ', x)
    """
    Depending on the size of the operations, we choose what will be more efficient to draw
    """
    if x > y:
        r.shuffle(draw_data_y) if SETTINGS['Shuffle'] else False
        return draw_data_y
    else:
        r.shuffle(draw_data_x) if SETTINGS['Shuffle'] else False
        return draw_data_x


@sio.on('lobbyPlayerDrawing')
async def on_lobbyPlayerDrawing(data):
    """
    When lobby says that someone is drawing and that one is us, we draw
    """
    if data == GAME_DATA["myID"]:
        img = await dither(GAME_DATA['word'])                           # Image Dither
        for line in image_optimize(img, SETTINGS['X'], SETTINGS['Y']):  # Optimization for fast draw here, 3 and 5 are sizes of pixels for x drawing and y drawing, changing them u can make image bigger or smaller
            if line[0][1] != 0:                                         # We loop through image
                await sio.emit('drawCommands', line)                    # Draw line


async def start_server():
    await sio.connect(f"wss://skribbl.io:{SETTINGS['Port']}/")
    await sio.wait()
    print(f"{color.Back.RED}{color.Style.BRIGHT}Et tu, Brute?")

    
if __name__ == '__main__':
    print(f"{color.Fore.GREEN}Logging in server \"{SETTINGS['Language']}\" with name \"{SETTINGS['BotName']}\".")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.close()


# Thank you for using our bot.

# Original bot created by alekxeyuk.
# Spam intergration and eighteen bot running created by PotassiumSnek#6853.
# .bat support, exec and .config created by ! [( TheGamerX )]#7912.
# Discord community server managed by PotassiumSnek#6853, ! [( TheGamerX )]#7912 and Kittler#4652
