"""
The CerealBox toolkit: Window Launcher (v1.0) - by leToads : 3/1/22

An automation-ready command line tool for organizing windows
into predefined configurations to optimize workflow.

    Usage: python launcher.py {-a, -h} {-t|-m}
    Default flags are -a and -h.

    Examples:
    launcher.py -a    -   Display the author tag.
    launcher.py -h    -   Display the help dialog.
    launcher.py -t    -   Runs 'tall' window configuration settings
    launcher.py -m    -   Runs 'mid' window configuration settings

Example function for application control:

def application_launch(args):

    running = APPLICATIONS[index] + '.exe' in (i.name() for i in psutil.process_iter())
    if not running:
        os.startfile(APPLICATION_LAUNCH_PATH)
        time.sleep(APPLICATION_LAUNCH_DELAY)
    hwnd = gui.FindWindow(WindowHandle, WindowName)
    for arg in args:
        if arg == "-t":
            gui.MoveWindow(hwnd, APPLICATION_DIMENSION[0], APPLICATION_DIMENSION[1],
                            APPLICATION_DIMENSION[2], APPLICATION_DIMENSION[3], True)
        elif arg == "-m":
            gui.MoveWindow(hwnd, APPLICATION_DIMENSION[0], APPLICATION_DIMENSION[1] + 700,
                            APPLICATION_DIMENSION[2], int(APPLICATION_DIMENSION[3] / 2), True)
"""

import getopt
import sys
import pyautogui as ag
import psutil
import os
import win32con
import win32gui as gui
import time
import selenium

APPS = ['Brave', 'OUTLOOK', 'Spotify', 'Teams', 'PyCharm']

SPOT_PATH = r''
OUTL_PATH = r''
TEAM_PATH = r''

SPOT_DELAY = 3
OUTL_DELAY = 4
TEAM_DELAY = 7

PC_DIM = [0, 0, 1280, 1400]
TM_DIM = [2561, 0, 853, 1400]
OL_DIM = [3413, 0, 853, 1400]
SP_DIM = [4260, 0, 865, 1400]

ag.PAUSE = 0.5
ag.FAILSAFE = True


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
    usage = ["The CerealBox toolkit: Window Launcher (v1.0) - by leToads : 3/1/22\n",

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


def launch_cleanup(args):
    """Resize and move Pycharm launcher.py session if open."""
    running = APPS[4] + '.EXE' in (i.name() for i in psutil.process_iter())
    if not running:
        pass
    hwnd = gui.FindWindow('SunAwtFrame', None)
    for arg in args:
        if arg == "-t":
            gui.MoveWindow(hwnd, PC_DIM[0], PC_DIM[1], PC_DIM[2], PC_DIM[3], True)
        elif arg == "-m":
            gui.MoveWindow(hwnd, PC_DIM[0] + 2561, PC_DIM[1], PC_DIM[2], int(PC_DIM[3] / 2), True)


def brave_launch():  # Not implemented yet, switching to Selenium
        # brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    time.sleep(3)
    hwnd = gui.GetForegroundWindow()
    gui.MoveWindow(hwnd, 0, -1080, 800, 600, True)
    gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)


def email_launch(args):
    """Check to see if E-mail is running, open it if not, then resize and move it. """
    running = APPS[1] + '.EXE' in (i.name() for i in psutil.process_iter())
    if not running:
        os.startfile(OUTL_PATH)
        time.sleep(OUTL_DELAY)
    hwnd = gui.FindWindow('rctrl_renwnd32', "Inbox - Alex.Farr@ung.edu - Outlook")
    for arg in args:
        if arg == "-t":
            gui.MoveWindow(hwnd, OL_DIM[0], OL_DIM[1], OL_DIM[2], OL_DIM[3], True)
        elif arg == "-m":
            gui.MoveWindow(hwnd, OL_DIM[0], OL_DIM[1] + 700, OL_DIM[2], int(OL_DIM[3] / 2), True)


def spotify_launch(args):
    """Check to see if Spotify is running, open it if not, then resize and move it. """
    running = APPS[2] + '.exe' in (i.name() for i in psutil.process_iter())
    if not running:
        os.startfile(SPOT_PATH)
        time.sleep(SPOT_DELAY)
    hwnd = gui.FindWindow(None, "Spotify Premium")
    for arg in args:
        if arg == "-t":
            gui.MoveWindow(hwnd, SP_DIM[0], SP_DIM[1], SP_DIM[2], SP_DIM[3], True)
        elif arg == "-m":
            gui.MoveWindow(hwnd, SP_DIM[0], SP_DIM[1] + 700, SP_DIM[2], int(SP_DIM[3] / 2), True)


def teams_launch(args):
    """Check to see if Spotify is running, open it if not, then resize and move it. """
    running = APPS[3] + '.exe' in (i.name() for i in psutil.process_iter())
    if not running:
        os.startfile(TEAM_PATH)
        time.sleep(TEAM_DELAY)
    hwnd = gui.GetForegroundWindow()
    for arg in args:
        if arg == "-t":
            gui.MoveWindow(hwnd, TM_DIM[0], TM_DIM[1], TM_DIM[2], TM_DIM[3], True)
        elif arg == "-m":
            gui.MoveWindow(hwnd, TM_DIM[0], TM_DIM[1] + 700, TM_DIM[2], int(TM_DIM[3] / 2), True)


def main(args):
    """Main Driver - Parse CLI flags/options and run the related subprogram."""
    if not args:  # if no flags/args passed, apply defaults
        argument_list = ['-a', '-h']
    else:  # inherit flags/args list
        argument_list = args

    options = "ahtm"  # define range of possible flags

    try:  # attempt to map flags to their corresponding arguments
        arguments, values = getopt.getopt(argument_list, options)

        # logical matching for arguments to driving logic
        for current_argument, current_value in arguments:
            if current_argument == "-a":
                author()

            if current_argument == "-h":
                helpme()

            if (current_argument == "-m") | (current_argument == "-t"):
                #brave_launch()
                email_launch(args)
                spotify_launch(args)
                teams_launch(args)
                launch_cleanup(args)

    except getopt.error as err:  # if mapping fails, pass stderr through to output
        print(str(err))
    return 0


if __name__ == '__main__':
    # pass main driver function args list from sys
    # start at index 1 to skip over the command call itself
    main(sys.argv[1:])
