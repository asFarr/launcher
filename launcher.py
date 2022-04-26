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

import win32gui as gui
import re

APPS = ['Brave', 'Outlook', 'Spotify', 'Teams', 'PyCharm']

SPOT_PATH = r''
OUTL_PATH = r''
TEAM_PATH = r''

PC_DIM = [0, 0, 1280, 1400]
TM_DIM = [2561, 0, 853, 1400]
OL_DIM = [3413, 0, 853, 1400]
SP_DIM = [4260, 0, 865, 1400]


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


def set_dimensions(hwnd, extra):
    if re.search(APPS[1], gui.GetWindowText(hwnd)):
        gui.MoveWindow(hwnd, OL_DIM[0], OL_DIM[1], OL_DIM[2], OL_DIM[3], True)

    if re.search(APPS[2], gui.GetWindowText(hwnd)):
        gui.MoveWindow(hwnd, SP_DIM[0], SP_DIM[1], SP_DIM[2], SP_DIM[3], True)

    if re.search(APPS[3], gui.GetWindowText(hwnd)):
        gui.MoveWindow(hwnd, TM_DIM[0], TM_DIM[1], TM_DIM[2], TM_DIM[3], True)


def main():
    gui.EnumWindows(set_dimensions, None)


if __name__ == '__main__':
    main()