import os
from datetime import datetime
import sys
import time as t
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
leaver_counter = 0
doLeave = False

def errexit(errcode, sleep):
    t.sleep(sleep)
    os._exit(errcode)

 
try:
    with open('bin\settings.json') as settings_file:
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

time = datetime.now()
log_name_a = time.strftime("%d")
log_name_b = time.strftime("%b")
log_name_c = time.strftime("%Y")
log_name_d = time.strftime("%H")
log_name_e = time.strftime("%M")
log_name_f = time.strftime("%S")

if not os.path.exists(r'chat-log'):
    os.mkdir('chat-log')

with open(r'chat-log\PORT {}; {} {} {}; {}h {}m {}s.txt'.format(SETTINGS["Port"], log_name_a, log_name_b, log_name_c, log_name_d,log_name_e,log_name_f), 'w') as file:
    file.write("Chat log for bot ran at {}h {}m {}s on {} {} {} (PORT {}):\n".format(log_name_d, log_name_e, log_name_f, log_name_a,log_name_b,log_name_c, SETTINGS["Port"]))
    file.close()

async def sendSpamMessage():
    global under_101
    if SETTINGS["SpamServer"]:
        if not under_101:
            if SETTINGS["BrightOrDim"].lower() == "bright":
                print(f"{color.Back.YELLOW}{color.Style.BRIGHT}Warning: Your message has {messageLength - 100} extra characters.")
            else:
                print(f"{color.Back.YELLOW}{color.Style.DIM}Warning: Your message has {messageLength - 100} extra characters.")
        else:
            if SETTINGS["AutomaticFormatting"]:
                await sio.emit("chat", f"{SETTINGS['SpamMessage']}".replace(".", ","))        
            else:
                await sio.emit("chat", f"{SETTINGS['SpamMessage']}")

    
if not (SETTINGS["Algorithm"].lower() == 'cluster' or SETTINGS["Algorithm"].lower() == 'yliluoma'):
    print(f"{color.Back.RED}{color.Style.BRIGHT}Error: Algorithm \"{SETTINGS['Algorithm']}\" was not found. See settings.json and change \"Algorithm\" to \"cluster\" or \"yliluoma\".")
    errexit(1,5)

if not (SETTINGS["Port"] == 5001 or SETTINGS["Port"] == 5002 or SETTINGS["Port"] == 5003 or SETTINGS["Port"] == "all"):
    print(f"{color.Back.RED}{color.Style.BRIGHT}Error: Port {SETTINGS['Port']} does not exist. See settings.json and change \"Port\" to 5001, 5002, 5003 or \"all\".")
    errexit(1,5)

if not (SETTINGS["ColourTheme"].lower() == "emerald" or SETTINGS["ColourTheme"].lower() == "fire" or SETTINGS["ColourTheme"].lower() == "ocean" or SETTINGS["ColourTheme"].lower() == "storm" or SETTINGS["ColourTheme"].lower() == "candy" or SETTINGS["ColourTheme"].lower() == "plain" or SETTINGS["ColourTheme"].lower() == "gold"):
    print(f"{color.Fore.RED}Warning: Colour Theme \"{SETTINGS['ColourTheme']}\" does not exist. See settings.json and change \"ColourTheme\" to a correct theme listed (Using plain as default).")
    print()

if not (SETTINGS["BrightOrDim"].lower() == "dim" or SETTINGS["BrightOrDim"].lower() == "bright"):
    print(f"{color.Fore.RED}Warning: \"BrightOrDim\" is not set to either \"bright\" or \"dim\". Please change \"BrightOrDim\" to either \"bright\" or \"dim\" (Using DIM as default).")
    print()

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
    if SETTINGS["BrightOrDim"].lower() == "bright":
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.LIGHTGREEN_EX}{color.Style.BRIGHT}Drawing: {image2Draw} with {img.size}")
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.LIGHTRED_EX}{color.Style.BRIGHT}Drawing: {image2Draw} with {img.size}")
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.LIGHTBLUE_EX}{color.Style.BRIGHT}Drawing: {image2Draw} with {img.size}")
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}Drawing: {image2Draw} with {img.size}")
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}Drawing: {image2Draw} with {img.size}")
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print(f"Drawing: {image2Draw} with {img.size}")
        else:
            print(f"Drawing: {image2Draw} with {img.size}")
    else:
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.LIGHTGREEN_EX}{color.Style.DIM}Drawing: {image2Draw} with {img.size}")
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.LIGHTRED_EX}{color.Style.DIM}Drawing: {image2Draw} with {img.size}")
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.LIGHTBLUE_EX}{color.Style.DIM}Drawing: {image2Draw} with {img.size}")
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}Drawing: {image2Draw} with {img.size}")
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}Drawing: {image2Draw} with {img.size}")
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print(f"Drawing: {image2Draw} with {img.size}")
        else:
            print(f"Drawing: {image2Draw} with {img.size}")

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
    if SETTINGS["BrightOrDim"].lower() == "bright":
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.BLUE}{color.Style.BRIGHT}Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print("Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "gold":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}Connection established")
            print()
        else:
            print("Connection established")
            print()
    else:
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.WHITE}{color.Style.DIM}Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.WHITE}{color.Style.DIM}Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.BLUE}{color.Style.DIM}Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print("Connection established")
            print()
        elif SETTINGS["ColourTheme"].lower() == "gold":
            print(f"{color.Fore.WHITE}{color.Style.DIM}Connection established")
            print()
        else:
            print("Connection established")
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
    global leaver_counter
    global doLeave
    doLeave = False
    """
    When we connected to the lobby we print out the current round, the number of players, the players names and their score, we also also store that info into GAME_DATA dict
    """
    log_destination = r'chat-log\PORT {}; {} {} {}; {}h {}m {}s.txt'.format(SETTINGS["Port"], log_name_a, log_name_b, log_name_c, log_name_d,log_name_e,log_name_f)
    print(f'{color.Fore.LIGHTMAGENTA_EX}This lobbies chat will be saved to {log_destination}')
    print(f'{color.Fore.LIGHTMAGENTA_EX}Notice: As of v1.92, text containing unicode or text from a username containing unicode can not be saved into the chat logs.\n')
    if SETTINGS["BrightOrDim"].lower() == "bright":
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}Lobby connected")
            print(f"{color.Fore.GREEN}{color.Style.BRIGHT}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}Lobby connected")
            print(f"{color.Fore.RED}{color.Style.BRIGHT}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}Lobby connected")
            print(f"{color.Fore.BLUE}{color.Style.BRIGHT}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}Lobby connected")
            print(f"{color.Fore.CYAN}{color.Style.BRIGHT}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}Lobby connected")
            print(f"{color.Fore.MAGENTA}{color.Style.BRIGHT}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print("Lobby connected")
            print(f"Round {data['round']} / {data['roundMax']}")
            print(f"There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "gold":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}Lobby connected")
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}There {len(data['players'])} players: ")
        else:
            print("Lobby connected")
            print(f"Round {data['round']} / {data['roundMax']}")
            print(f"There {len(data['players'])} players: ")
    else:
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.WHITE}{color.Style.DIM}Lobby connected")
            print(f"{color.Fore.GREEN}{color.Style.DIM}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.WHITE}{color.Style.DIM}There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}Lobby connected")
            print(f"{color.Fore.RED}{color.Style.DIM}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.YELLOW}{color.Style.DIM}There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.WHITE}{color.Style.DIM}Lobby connected")
            print(f"{color.Fore.BLUE}{color.Style.DIM}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.WHITE}{color.Style.DIM}There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}Lobby connected")
            print(f"{color.Fore.CYAN}{color.Style.DIM}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.YELLOW}{color.Style.DIM}There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}Lobby connected")
            print(f"{color.Fore.MAGENTA}{color.Style.DIM}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.YELLOW}{color.Style.DIM}There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print("Lobby connected")
            print(f"Round {data['round']} / {data['roundMax']}")
            print(f"There {len(data['players'])} players: ")
        elif SETTINGS["ColourTheme"].lower() == "gold":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}Lobby connected")
            print(f"{color.Fore.WHITE}{color.Style.DIM}Round {data['round']} / {data['roundMax']}")
            print(f"{color.Fore.YELLOW}{color.Style.DIM}There {len(data['players'])} players: ")
        else:
            print("Lobby connected")
            print(f"Round {data['round']} / {data['roundMax']}")
            print(f"There {len(data['players'])} players: ")

    for player in data['players']:
        if SETTINGS["BrightOrDim"].lower() == "bright":
            if SETTINGS["ColourTheme"].lower() == "emerald":
                print(f"    {color.Fore.LIGHTGREEN_EX}{player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "fire":
                print(f"    {color.Fore.LIGHTYELLOW_EX}{player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "ocean":
                print(f"    {color.Fore.LIGHTCYAN_EX}{player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "storm":
                print(f"    {color.Fore.LIGHTYELLOW_EX}{player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "candy":
                print(f"    {color.Fore.LIGHTCYAN_EX}{player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "plain":
                print(f"    {player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "gold":
                print(f"    {color.Fore.LIGHTWHITE_EX}{player['id']} = {player['name']} > {player['score']}")
            else:
                print(f"    {player['id']} = {player['name']} > {player['score']}")
        else:
            if SETTINGS["ColourTheme"].lower() == "emerald":
                print(f"    {color.Fore.GREEN}{player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "fire":
                print(f"    {color.Fore.YELLOW}{player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "ocean":
                print(f"    {color.Fore.CYAN}{player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "storm":
                print(f"    {color.Fore.YELLOW}{player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "candy":
                print(f"    {color.Fore.CYAN}{player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "plain":
                print(f"    {player['id']} = {player['name']} > {player['score']}")
            elif SETTINGS["ColourTheme"].lower() == "gold":
                print(f"    {color.Fore.WHITE}{player['id']} = {player['name']} > {player['score']}")
            else:
                print(f"    {player['id']} = {player['name']} > {player['score']}")

        if player['name'] == SETTINGS["OnlyUserName"] and SETTINGS['OnlyUser']:
            doLeave = True
            leaver_counter += (leaver_counter + 1)

    print()

    if doLeave and SETTINGS['OnlyUser'] and leaver_counter >= 3:
        print(f"{color.Back.RED}{color.Style.DIM}{color.Fore.WHITE}Avoidance: \"{SETTINGS['OnlyUserName']}\" found. Exiting lobby.")
        t.sleep(r.randint(3,5))
        await sio.disconnect()
        os._exit(1)

    GAME_DATA.update({'players' : {player['id'] : {'name': player['name'], 'score': player['score'], 'guessedWord': player['guessedWord']} for player in data['players']}})
    GAME_DATA.update({'myID': data['myID']})
    GAME_DATA.update({'round' : data['round']})

    await sio.emit("chat", f"{SETTINGS['SpamMessage']}")

@sio.on('lobbyState')
def on_lobbyState(data):
    """
    When lobby change its state, we want to show that
    """
    if SETTINGS["BrightOrDim"].lower() == 'bright':
        if SETTINGS["ColourTheme"].lower() == 'emerald':
            print(f"{color.Fore.LIGHTWHITE_EX}Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'fire':
            print(f"{color.Fore.LIGHTRED_EX}Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'ocean':
            print(f"{color.Fore.LIGHTCYAN_EX}Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'storm':
            print(f"{color.Fore.LIGHTYELLOW_EX}Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'candy':
            print(f"{color.Fore.LIGHTBLUE_EX}Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'plain':
            print(f"Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'gold':
            print(f"{color.Fore.LIGHTWHITE_EX}Lobby State: {data}")
        else:
            print(f"Lobby State: {data}")
    else:
        if SETTINGS["ColourTheme"].lower() == 'emerald':
            print(f"{color.Fore.WHITE}Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'fire':
            print(f"{color.Fore.RED}Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'ocean':
            print(f"{color.Fore.CYAN}Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'storm':
            print(f"{color.Fore.YELLOW}Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'candy':
            print(f"{color.Fore.CYAN}Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'plain':
            print(f"Lobby State: {data}")
        elif SETTINGS["ColourTheme"].lower() == 'gold':
            print(f"{color.Fore.WHITE}Lobby State: {data}")
        else:
            print(f"Lobby State: {data}")


@sio.on('lobbyCurrentWord')
def on_lobbyCurrentWord(data):
    """
    When lobby updates current word, we want to show this.
    """
    if SETTINGS["BrightOrDim"].lower() == 'bright':
        if SETTINGS["ColourTheme"].lower() == 'emerald':
            print(f"{color.Style.BRIGHT}{color.Fore.WHITE}Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'fire':
            print(f"{color.Style.BRIGHT}{color.Fore.YELLOW}Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'ocean':
            print(f"{color.Style.BRIGHT}{color.Fore.LIGHTCYAN_EX}Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'storm':
            print(f"{color.Style.BRIGHT}{color.Fore.YELLOW}Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'candy':
            print(f"{color.Style.BRIGHT}{color.Fore.LIGHTBLUE_EX}Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'plain':
            print(f"Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'gold':
            print(f"{color.Style.BRIGHT}{color.Fore.WHITE}Current Word: {data}")
            print()
        else:
            print(f"Current Word: {data}")
            print()
    else:
        if SETTINGS["ColourTheme"].lower() == 'emerald':
            print(f"{color.Style.DIM}{color.Fore.WHITE}Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'fire':
            print(f"{color.Style.DIM}{color.Fore.YELLOW}Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'ocean':
            print(f"{color.Style.DIM}{color.Fore.LIGHTCYAN_EX}Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'storm':
            print(f"{color.Style.DIM}{color.Fore.YELLOW}Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'candy':
            print(f"{color.Style.DIM}{color.Fore.LIGHTBLUE_EX}Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'plain':
            print(f"Current Word: {data}")
            print()
        elif SETTINGS["ColourTheme"].lower() == 'gold':
            print(f"{color.Style.DIM}{color.Fore.WHITE}Current Word: {data}")
            print()
        else:
            print(f"Current Word: {data}")
            print()
    


@sio.on('chat')
async def on_chat(data):
    global clear
    """
    Chat function, prints username or id of user and their message
    """
    if 'players' in GAME_DATA.keys():
        if SETTINGS["BrightOrDim"].lower() == "bright":
            if SETTINGS["ColourTheme"].lower() == "emerald":
                print(f"{color.Fore.LIGHTGREEN_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "fire":
                print(f"{color.Fore.LIGHTRED_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "ocean":
                print(f"{color.Fore.LIGHTBLUE_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "storm":
                print(f"{color.Fore.LIGHTCYAN_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "candy":
                print(f"{color.Fore.LIGHTMAGENTA_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "plain":
                print(f"{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "gold":
                print(f"{color.Fore.LIGHTYELLOW_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            else:
                print(f"{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
        else:
            if SETTINGS["ColourTheme"].lower() == "emerald":
                print(f"{color.Fore.GREEN}{color.Style.DIM}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "fire":
                print(f"{color.Fore.RED}{color.Style.DIM}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "ocean":
                print(f"{color.Fore.BLUE}{color.Style.DIM}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "storm":
                print(f"{color.Fore.CYAN}{color.Style.DIM}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "candy":
                print(f"{color.Fore.MAGENTA}{color.Style.DIM}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "plain":
                print(f"{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            elif SETTINGS["ColourTheme"].lower() == "gold":
                print(f"{color.Fore.YELLOW}{color.Style.DIM}{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
            else:
                print(f"{GAME_DATA['players'][data['id']]['name']} wrote > {data['message']}")
        
        if not GAME_DATA['players'][data['id']]['name'] == SETTINGS['BotName']:
            with open(r'chat-log\PORT {}; {} {} {}; {}h {}m {}s.txt'.format(SETTINGS["Port"], log_name_a, log_name_b, log_name_c, log_name_d,log_name_e,log_name_f), 'a') as file:
                try:
                    file.write(f"\n{GAME_DATA['players'][data['id']]['name']} >>> {data['message']}")
                    file.close()
                except UnicodeEncodeError:
                    if SETTINGS["ColourTheme"].lower() == "emerald" or SETTINGS["ColourTheme"].lower() == "ocean" or SETTINGS["ColourTheme"].lower() == "storm" or SETTINGS["ColourTheme"].lower() == "candy" or SETTINGS["ColourTheme"].lower() == "plain" or SETTINGS["ColourTheme"].lower() == "gold":
                        print(f"{color.Fore.RED}{color.Style.BRIGHT}Unicode error: Text not saved to log.")
                        file.close()
                    else:
                        print(f"{color.Fore.LIGHTBLUE_EX}{color.Style.BRIGHT}Unicode error: Text not saved to log.")
        if clear == True:
            clear = False
            t.sleep(1.4)
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
    if SETTINGS["BrightOrDim"].lower() == "bright":
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print(f"{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "gold":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}{data['name']} connected.")
        else:
            print(f"{data['name']} connected.")
    else:
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.WHITE}{color.Style.DIM}{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.WHITE}{color.Style.DIM}{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print(f"{data['name']} connected.")
        elif SETTINGS["ColourTheme"].lower() == "gold":
            print(f"{color.Fore.WHITE}{color.Style.DIM}{data['name']} connected.")
        else:
            print(f"{data['name']} connected.")


@sio.on('lobbyPlayerDisconnected')
async def on_lobbyPlayerDisconnected(data):
    global doLeave
    """
    When someone leaves the lobby, we want to know this, so this is what this function does
    It also makes the bot leave if OnlyUser is enabled
    """
    if SETTINGS["BrightOrDim"].lower() == "bright":
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print(f"{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "gold":
            print(f"{color.Fore.WHITE}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} left.")
        else:
            print(f"{GAME_DATA['players'][data]['name']} left.")
    else:
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.WHITE}{color.Style.DIM}{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.WHITE}{color.Style.DIM}{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print(f"{GAME_DATA['players'][data]['name']} left.")
        elif SETTINGS["ColourTheme"].lower() == "gold":
            print(f"{color.Fore.WHITE}{color.Style.DIM}{GAME_DATA['players'][data]['name']} left.")
        else:
            print(f"{GAME_DATA['players'][data]['name']} left.")

@sio.on('lobbyPlayerGuessedWord')
def on_lobbyPlayerGuessedWord(data):
    """
    When someone guesses a word, we want to know it, so this is what this function does
    """
    if SETTINGS["BrightOrDim"].lower() == "bright":
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.LIGHTWHITE_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.LIGHTYELLOW_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.LIGHTCYAN_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.YELLOW}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.LIGHTBLUE_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print(f"{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "gold":
            print(f"{color.Fore.LIGHTWHITE_EX}{color.Style.BRIGHT}{GAME_DATA['players'][data]['name']} the guessed word!")
        else:
            print(f"{GAME_DATA['players'][data]['name']} the guessed word!")
    else:
        if SETTINGS["ColourTheme"].lower() == "emerald":
            print(f"{color.Fore.WHITE}{color.Style.DIM}{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "fire":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "ocean":
            print(f"{color.Fore.CYAN}{color.Style.DIM}{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "storm":
            print(f"{color.Fore.YELLOW}{color.Style.DIM}{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "candy":
            print(f"{color.Fore.CYAN}{color.Style.DIM}{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "plain":
            print(f"{GAME_DATA['players'][data]['name']} the guessed word!")
        elif SETTINGS["ColourTheme"].lower() == "gold":
            print(f"{color.Fore.WHITE}{color.Style.DIM}{GAME_DATA['players'][data]['name']} the guessed word!")
        else:
            print(f"{GAME_DATA['players'][data]['name']} the guessed word!")


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
        if not SETTINGS["ExitOnTurn"]:
            GAME_DATA.update({"word": data['words'][2]})   # We always choose the third word, you can change it the way you want it to work
            if SETTINGS["BrightOrDim"].lower() == "dim":
                print(f"{color.Style.BRIGHT}I am drawing {data['words'][2]}")
            else:
                print(f"{color.Style.DIM}I am drawing {data['words'][2]}")
                await sio.emit("lobbyChooseWord", 2)
        else:
            print(f"{color.Back.LIGHTGREEN_EX}{color.Fore.LIGHTWHITE_EX}Avoidance: \"Exit on turn\" is checked. Exiting lobby...")
            t.sleep(1)
            await sio.disconnect()
            os._exit(1)


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
    if SETTINGS["Port"] == "all":
        SETTINGS["Port"] = 5001
    await sio.connect(f"wss://skribbl.io:{SETTINGS['Port']}/")
    await sio.wait()
    print(f"{color.Back.RED}{color.Style.BRIGHT}Reconnecting.")

    
if __name__ == '__main__':
    your_time = f"{log_name_a} {log_name_b} {log_name_c} :: {log_name_d}h {log_name_e}m {log_name_f}s\n"
    if SETTINGS["BrightOrDim"].lower() == 'bright':
        if SETTINGS["ColourTheme"].lower() == 'emerald':
            print(f"{color.Fore.LIGHTGREEN_EX}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.LIGHTWHITE_EX}Logging into server \"{SETTINGS['Language']}\" with the username \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'fire':
            print(f"{color.Fore.LIGHTRED_EX}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.LIGHTYELLOW_EX}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'ocean':
            print(f"{color.Fore.LIGHTBLUE_EX}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.LIGHTCYAN_EX}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'storm':
            print(f"{color.Fore.LIGHTCYAN_EX}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.LIGHTYELLOW_EX}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'candy':
            print(f"{color.Fore.LIGHTYELLOW_EX}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.LIGHTBLUE_EX}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'plain':
            print(f"{color.Fore.LIGHTWHITE_EX}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.LIGHTWHITE_EX}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'gold':
            print(f"{color.Fore.LIGHTWHITE_EX}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.LIGHTYELLOW_EX}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        else:
            print(f"{color.Fore.LIGHTWHITE_EX}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.LIGHTWHITE_EX}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
    else:
        if SETTINGS["ColourTheme"].lower() == 'emerald':
            print(f"{color.Fore.GREEN}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.WHITE}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'fire':
            print(f"{color.Fore.RED}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.YELLOW}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'ocean':
            print(f"{color.Fore.BLUE}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.CYAN}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'storm':
            print(f"{color.Fore.CYAN}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.YELLOW}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'candy':
            print(f"{color.Fore.YELLOW}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.CYAN}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'plain':
            print(f"{color.Fore.WHITE}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.WHITE}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        elif SETTINGS["ColourTheme"].lower() == 'gold':
            print(f"{color.Fore.WHITE}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.YELLOW}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
        else:
            print(f"{color.Fore.WHITE}BubbleBoiBot v1.92 programmed by KyleJamesCatterall#0989\n{your_time}")
            print(f"{color.Fore.WHITE}Logging into server \"{SETTINGS['Language']}\" with the username: \"{SETTINGS['BotName']}\" at port {SETTINGS['Port']}.")
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.close()


# Thank you for using our bot.

# [Original] Python programmed by alekxeyuk.
# [New] Python programmed by Nebulous#0989.
# [New] Batch / JSON programmed by ! [( TheGamerX )]#7912.
