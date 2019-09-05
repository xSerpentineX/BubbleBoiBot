import sys
import json
import time
import string
import asyncio
import socketio
import requests
import hitherdither
from io import BytesIO
from random import choice, randint, shuffle
from PIL import Image, ImageDraw, ImageFont
import google_images_download
import random as r

clear = True

SETTINGS = {'port': '5001', 'join': '', 'language': 'English', 'x': 3, 'y': 4, 'shuffle': True}
# Port: Skribbl.io has three ports; 5001, 5002 and 5003. Each port can have six bots on one machine, meaning 18 bots per machine at an optimal time.
# Join: Join can be used if you wish to use private games. Put the code after the "?" in the link. A game randomly has either 5001, 5002 or 5003, so each port must be tested.
# Language: What servers you want to be on. English is default.
# x,y: Ignore this.
# Shuffle: Ignore this.

if len(sys.argv) == 2:
    """
    U can set port using command line
    """
    SETTINGS['port'] = sys.argv[1]
    
GAME_DATA = {'died': False}
sio = socketio.AsyncClient(logger=False, reconnection=True)  # U can turn logger True, if u need to catch events that are not described in current version of program
response = google_images_download.googleimagesdownload()     # For this program to work u need modified google_images_download module

# Read spam.txt file
f = open("spam.txt")
text2spam = f.readline()
f.close()

# Check text2spam Variable
if len(text2spam.replace("%random", str(r.randint(0, 99)))) > 100:
    print("Warning: Text file is longer than 100 characters")
    print()

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
    """
    Here we are creating list of arguments for googleimagesdownload module,
    then we get response that is a list of links to images,
    then we trying to get working link for working image,
    then we load it into memory and dither it using cluster_dot_dithering algorithm
    """
    #img = Image.new('RGB', (800, 600), (255, 255, 255))
    #d = ImageDraw.Draw(img)
    #d.text((10, 10), f'TesT TesT', fill=(0, 0, 0), font=ImageFont.truetype("v_Compacta_Blk_BT_v1.5.ttf", 85))
    
    arguments = {"keywords": "dick", "limit":10, "print_urls":False, 'no_download':True, 'safe_search':True, 'exact_size':'355,294', 'type': 'photo', 'format': 'jpg'}
    # keywords: Change this to whatever picture you want. This is the word it searches in google images.
    # limit: Ignore.
    # print_urls: Ignore.
    # no_download: Do you wish to download the image into the downloads folder? (Not the computer download folder, the bot's download folder).
    # Safe_Search: Will it use safe_search (for some reason, dick doesn't matter).
    # Exact Size: Put the size of the image you found on google here. Pain in the arse since Google removed its search by image filter.
    # Type: What type of image. Also a pain in the arse since Google removed its cartoon and other types from the type filters.
    # Format: Ignore.
    
    for link in response.download(arguments):  
        try:
            with Image.open(BytesIO(requests.get(link, timeout = 5).content)) as img:
                img = img.resize((int(200), int(150)))                                                              # Here you can change end size of image, but don't forget to also change pixel draw size in parent function
                print(img.size)
                img_dithered = hitherdither.ordered.cluster.cluster_dot_dithering(img, palette, [1, 1, 1], 4)       # Here you can change dither algo, yliluoma is much much better in quality but it is very very slow
                #img_dithered = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(img, palette, order=8)
                return img_dithered
        except:
            print("broke")

def GenRandomLine(length=8, chars=string.ascii_letters):
    """
    Generate random line
    """
    return ''.join([choice(chars) for i in range(length)])

async def sendSpamMessage():
    await sio.emit("chat", text2spam.replace("%random", str(r.randint(0, 99))))

@sio.on('connect')
async def on_connect():
    """
    On connection to the lobby we must introduce ourselves
    """
    print('connection established')
    num1 = r.randint(1, 5)
    num2 = r.randint(1, 5)
    num3 = r.randint(1, 5)
    num4 = r.randint(1, 5)
    await sio.emit('userData' , {"name": "BubblyBoiBot", "code":"", "avatar": [num1, num2, num3, num4], "join": SETTINGS['join'], "language": SETTINGS['language'], "createPrivate": False})
    # Name: What the username will be in the server.
    # Code: No Idea what this does to be honest.
    # Avatar: Set to -1 for blank, set to num1-4 for random.
    # Ignore the rest, it's coming from line 16.


@sio.on('lobbyConnected')
async def on_lobbyConnected(data):
    global clear
    """
    When we connected to the lobby we print out the current round, the number of players, the players names and their score, we also also store that info into GAME_DATA dict
    """
    print("Lobby Connected")
    print(f"round {data['round']} / {data['roundMax']}")
    print(f"there {len(data['players'])} players : ")
    for player in data['players']:
        print(f"{player['id']} = {player['name']} > {player['score']}")
    GAME_DATA.update({'players' : {player['id'] : {'name': player['name'], 'score': player['score'], 'guessedWord': player['guessedWord']} for player in data['players']}})
    GAME_DATA.update({'myID': data['myID']})
    GAME_DATA.update({'round' : data['round']})
    """
    Here u can send your welcoming message to the chat, a max of 100 characters per line, u can however use anything, emojis or even special characters
    """
    # These are the messages sent when the bot first joins a server.
    for x in range(0, 2):
        await sendSpamMessage()

@sio.on('lobbyState')
def on_lobbyState(data):
    """
    When lobby change its state, we want to show that
    """
    print(f"Lobby State = {data}")

@sio.on('lobbyCurrentWord')
def on_lobbyCurrentWord(data):
    """
    When lobby updates current word, we want to show that
    """
    print(f"Current Word = {data}")

@sio.on('chat')
async def on_chat(data):
    global clear
    """
    Chat function, prints username or id of user and their message
    """
    if 'players' in GAME_DATA.keys():
        print(f"{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
        if clear == True:
            clear = False
            time.sleep(1.4)
            # This is the message that will be spammed.
            await sendSpamMessage()
            clear = True
    else:
        print(f"{data['id']} wrote > {data['message']}")

@sio.on('lobbyPlayerConnected')
async def on_lobbyPlayerConnected(data):
    """
    When someone enters the lobby, we want to know this, so this is what this function does
    """
    GAME_DATA['players'].update({data['id'] : {'name': data['name'], 'score': data['score'], 'guessedWord': data['guessedWord']}})
    print(f"player connected -> {data['name']}")

@sio.on('lobbyPlayerDisconnected')
async def on_lobbyPlayerDisconnected(data):
    """
    When someone leaves the lobby, we want to know this, so this is what this function does
    """
    print(f"player left -> {GAME_DATA['players'][data]['name']}")

@sio.on('lobbyPlayerGuessedWord')
def on_lobbyPlayerGuessedWord(data):
    """
    When someone guesses a word, we want to know it, so this is what this function does
    """
    print(f"player guessed word -> {GAME_DATA['players'][data]['name']}")

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
    print('disconnected from server')
    await sio.eio.disconnect(True)

@sio.on('kicked')
def on_kicked():
    """
    The lobby can kick us, we can't do anything about it, at least I have no idea
    """
    print('You either die a hero or you live long enough to see yourself become the villain')
    GAME_DATA['died'] = True

@sio.on('lobbyChooseWord')
async def on_lobbyChooseWord(data):
    """
    When the lobby says that someone can choose a word, we check that it is us
    """
    if data['id'] == GAME_DATA["myID"]:
        GAME_DATA.update({"word": data['words'][2]})   # We always choose the third word, you can change it the way you want it to work
        print(f"I am drawing {data['words'][2]}")
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
        shuffle(draw_data_y) if SETTINGS['shuffle'] else False
        return draw_data_y
    else:
        shuffle(draw_data_x) if SETTINGS['shuffle'] else False
        return draw_data_x

@sio.on('lobbyPlayerDrawing')
async def on_lobbyPlayerDrawing(data):
    """
    When lobby says that someone is drawing and that one is us, we draw
    """
    if data == GAME_DATA["myID"]:
        print("My Time Has Come")
        img = await dither(GAME_DATA['word'])                           # Image Dither
        for line in image_optimize(img, SETTINGS['x'], SETTINGS['y']):  # Optimization for fast draw here, 3 and 5 are sizes of pixels for x drawing and y drawing, changing them u can make image bigger or smaller
            if line[0][1] != 0:                                         # We loop through image
                await sio.emit('drawCommands', line)                    # Draw line


async def start_server():
    await sio.connect(f"wss://skribbl.io:{SETTINGS['port']}/")
    await sio.wait()
    print('Et tu, Brute?')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.close()


# Thank you for using our bot.

# Original bot created by alekxeyuk.
# Spam intergration and eighteen bot running created by PotassiumSnek#6853.
# .bat support, exec and .config created by ! [( TheGamerX )]#7912.
# Discord community server managed by PotassiumSnek#6853, ! [( TheGamerX )]#7912 and Kittler#4652
