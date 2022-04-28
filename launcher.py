"""
The CerealBox toolkit: Window Launcher (v2.0) - by leToads : 4/28/22

An automation-ready command line tool for organizing windows
into predefined configurations to optimize workflow.

    Usage: python launcher.py {-a, -h} {-t|-m}
    Default flags are -a and -h.

    Examples:
    launcher.py -a    -   Display the author tag.
    launcher.py -h    -   Display the help dialog.
    launcher.py -t    -   Runs 'tall' window configuration settings
    launcher.py -m    -   Runs 'mid' window configuration settings
"""

import webbrowser as web
import win32gui as gui
import psutil
import getopt
import time
import sys
import os
import re

APPS = ['OUTLOOK', 'Spotify', 'Teams', 'Brave']

SPOT_PATH = r'C:\Users\asfarr\AppData\Roaming\Spotify\Spotify.exe'
OUTL_PATH = r'C:\Program Files (x86)\Microsoft Office\Office16\OUTLOOK.EXE'

tm_dim = [2561, 0, 853, 1400]
ol_dim = [3413, 0, 853, 1400]
sp_dim = [4260, 0, 865, 1400]
br_dim = [0, -1080, 1920, 1080]

APP_DELAY = 8
re.IGNORECASE = True

url = r''


def author():
    """Print the author ASCII signature."""
    authorart = [
"                                     88         888888888888                               88             d8'",
"                                     88              88                                    88            d8'",
"                                     88              88                                    88           \"\"",
"                                     88   ,adPPYba,  88   ,adPPYba,   ,adPPYYba,   ,adPPYb,88  ,adPPYba,",
"                                     88  a8P_____88  88  a8\"     \"8a  \"\"     `Y8  a8\"    `Y88  I8[    \"\"",
"                                     88  8PP\"\"\"\"\"\"\"  88  8b       d8  ,adPPPPP88  8b       88   `\"Y8ba,",
"                                     88  \"8b,   ,aa  88  \"8a,   ,a8\"  88,    ,88  \"8a,   ,d88  aa    ]8I",
"                                     88   `\"Ybbd8\"'  88   `\"YbbdP\"'   `\"8bbdP\"Y8   `\"8bbdP\"Y8  `\"YbbdP\"'\n\n\n",
"                     ,ad8888ba,                                                   88  88888888ba",
"                    d8\"'    `\"8b                                                  88  88      \"8b",
"                   d8'                                                            88  88      ,8P",
"                   88              ,adPPYba,  8b,dPPYba,   ,adPPYba,  ,adPPYYba,  88  88aaaaaa8P'   ,adPPYba,  8b,     ,d8",
"                   88             a8P_____88  88P'   \"Y8  a8P_____88  \"\"     `Y8  88  88\"\"\"\"\"\"8b,  a8\"     \"8a  `Y8, ,8P'",
"                   Y8,            8PP\"\"\"\"\"\"\"  88          8PP\"\"\"\"\"\"\"  ,adPPPPP88  88  88      `8b  8b       d8    )888(",
"                    Y8a.    .a8P  \"8b,   ,aa  88          \"8b,   ,aa  88,    ,88  88  88      a8P  \"8a,   ,a8\"  ,d8\" \"8b,",
"                     `\"Y8888Y\"'    `\"Ybbd8\"'  88           `\"Ybbd8\"'  `\"8bbdP\"Y8  88  88888888P\"    `\"YbbdP\"'  8P'     `Y8\n\n\n",
"       db                                      88                                                             88",
"      d88b                                     88                                                             88",
"     d8'`8b                                    88                                                             88",
"    d8'  `8b      8b,dPPYba,   8b,dPPYba,      88           ,adPPYYba,  88       88  8b,dPPYba,    ,adPPYba,  88,dPPYba,    ,adPPYba,  8b,dPPYba,",
"   d8YaaaaY8b     88P'    \"8a  88P'    \"8a     88           \"\"     `Y8  88       88  88P'   `\"8a  a8\"     \"\"  88P'    \"8a  a8P_____88  88P'   \"Y8",
"  d8\"\"\"\"\"\"\"\"8b    88       d8  88       d8     88           ,adPPPPP88  88       88  88       88  8b          88       88  8PP\"\"\"\"\"\"\"  88",
" d8'        `8b   88b,   ,a8\"  88b,   ,a8\"     88           88,    ,88  \"8a,   ,a88  88       88  \"8a,   ,aa  88       88  \"8b,   ,aa  88",
"d8'          `8b  88`YbbdP\"'   88`YbbdP\"'      88888888888  `\"8bbdP\"Y8   `\"YbbdP'Y8  88       88   `\"Ybbd8\"'  88       88   `\"Ybbd8\"'  88",
"                  88           88",
"                  88           88\n"]

    for i in authorart:
        print(i)


def helpme():
    """Print the help and usage dialog."""
    usage = ["The CerealBox toolkit: Window Launcher (v2.0) - by asFarr : 4/28/22\n",

"An automation-ready command line tool for organizing windows",
"into predefined configurations to optimize workflow.\n",

"    Usage: python launcher.py {-a, -h} {-t|-m}",
"    Default flags are -a and -h.\n",

"    Examples:",
"    launcher.py -a    -   Display the author tag.",
"    launcher.py -h    -   Display the help dialog.",
"    launcher.py -t    -   Runs 'tall' window configuration settings",
"    launcher.py -m    -   Runs 'mid' window configuration settings"]

    for i in usage:
        print(i)


def set_dimensions(hwnd, extra):
    """Configure window dimensions for predefined set of window frames"""
    if re.search(APPS[0], gui.GetWindowText(hwnd)):
        gui.MoveWindow(hwnd, ol_dim[0], ol_dim[1], ol_dim[2], ol_dim[3], True)

    if re.search(APPS[1], gui.GetWindowText(hwnd)):
        gui.MoveWindow(hwnd, sp_dim[0], sp_dim[1], sp_dim[2], sp_dim[3], True)

    if re.search(APPS[2], gui.GetWindowText(hwnd)):
        gui.MoveWindow(hwnd, tm_dim[0], tm_dim[1], tm_dim[2], tm_dim[3], True)

    if re.search(APPS[3], gui.GetWindowText(hwnd)):
        gui.MoveWindow(hwnd, br_dim[0], br_dim[1], br_dim[2], br_dim[3], True)


def main(args):
    """Main Driver - Parse CLI flags/options and run the related subprogram."""
    if not args:  # if no flags/args passed, apply defaults
        argument_list = ['-a', '-h']
    else:  # inherit flags/args list
        argument_list = args

    options = "ahtm"  # define range of possible flags
    for app in APPS:
        running = app + '.exe' in (i.name() for i in psutil.process_iter())
        if not running:
            if re.search(APPS[1], app):
                os.startfile(SPOT_PATH)
                time.sleep(APP_DELAY)
            if re.search(APPS[0], app):
                os.startfile(OUTL_PATH)
            if re.search(APPS[3], app):
                web.open_new(url)

    try:  # attempt to map flags to their corresponding arguments
        arguments, values = getopt.getopt(argument_list, options)

        # logical matching for arguments to driving logic
        for current_argument, current_value in arguments:
            if current_argument == "-a":
                author()

            if current_argument == "-h":
                helpme()

            if current_argument == "-t":
                gui.EnumWindows(set_dimensions, None)

            if current_argument == "-m":
                ol_dim[1] = ol_dim[1] + 700
                ol_dim[3] = int(ol_dim[3] / 2)
                sp_dim[1] = sp_dim[1] + 700
                sp_dim[3] = int(sp_dim[3] / 2)
                tm_dim[1] = tm_dim[1] + 700
                tm_dim[3] = int(tm_dim[3] / 2)
                gui.EnumWindows(set_dimensions, None)

    except getopt.error as err:  # if mapping fails, pass stderr through to output
        print(str(err))


if __name__ == '__main__':
    # pass main driver function args list from sys
    # start at index 1 to skip over the command call itself
    main(sys.argv[1:])
