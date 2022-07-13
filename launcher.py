"""
Launcher v3.0 by Alex Farr
Written: 07/12/22
"""

import re
import os
import sys
import time
import getopt
import psutil as ps
import pyautogui as ag
import win32gui as gui
import webbrowser as web
import yaml
try:
    from yaml import load, CSafeLoader as SafeLoader

except ImportError:
    from yaml import load, SafeLoader

# Script initialization

ag.PAUSE = 0.25
CONF = .5
re.IGNORECASE = True

# Load specified configuration files

with open("config/brave_config.yaml", mode="rt", encoding="utf-8") as config0:
    brave_cfg = yaml.safe_load(config0)

BRAVE_DELAY = brave_cfg["load-delay"]
BRAVE_PATH = brave_cfg["application"]["path"]

br_dim = []
for val in brave_cfg["dimensions_games"].values():
    br_dim.append(val)

with open("config/discord_config.yaml", mode="rt", encoding="utf-8") as config1:
    dscrd_cfg = yaml.safe_load(config1)

DSCRD_DELAY = dscrd_cfg["load-delay"]
DSCRD_PATH = dscrd_cfg["application"]["path"]

di_dim = []
for val in dscrd_cfg["dimensions_games"].values():
    di_dim.append(val)

with open("config/obsidian_config.yaml", mode="rt", encoding="utf-8") as config2:
    obsd_cfg = yaml.safe_load(config2)

OBSD_DELAY = obsd_cfg["load-delay"]
OBSD_PATH = obsd_cfg["application"]["path"]

ob_dim = []
for val in obsd_cfg["dimensions_games"].values():
    ob_dim.append(val)

with open("config/spotify_config.yaml", mode="rt", encoding="utf-8") as config3:
    spot_cfg = yaml.safe_load(config3)

SPOT_DELAY = spot_cfg["load-delay"]
SPOT_PATH = spot_cfg["application"]["path"]

sp_dim = []
for val in spot_cfg["dimensions_games"].values():
    sp_dim.append(val)

with open("config/steam_config.yaml", mode="rt", encoding="utf-8") as config4:
    steam_cfg = yaml.safe_load(config4)

STEAM_DELAY = steam_cfg["load-delay"]
STEAM_PATH = steam_cfg["application"]["path"]

sg_dim = []
for val in steam_cfg["dimensions_games"].values():
    sg_dim.append(val)
sf_dim = []
for val in steam_cfg["dimensions_friends"].values():
    sf_dim.append(val)


app_list = [dscrd_cfg["application"]["name"],
            brave_cfg["application"]["name"],
            obsd_cfg["application"]["name"],
            spot_cfg["application"]["name"],
            steam_cfg["application"]["name"]]


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
    usage = ["\nThe CerealBox toolkit: Window Launcher (v3.0) - by asFarr : 7/12/22\n",
             "An automation-ready command line tool for organizing windows",
             "into predefined configurations to optimize workflow.\n",

             "    Usage: python launcher.py {-a, -h} {-g|-s|-w} {-l|-r}",
             "    Default flags are -a and -h.\n",

             "    Examples:\n",

             "Information Flags:",
             "    launcher -a    -   Display the author tag.",
             "    launcher -h    -   Display the help dialog.\n",

             "Application Flags",
             "    launcher -g    -   Run Gaming Mode.",
             "    launcher -s    -   Run Server Dashboard Mode.",
             "    launcher -w    -   Run Workstation Mode.\n",

             "Screen Context Flags",
             "    launcher -l    -   Use Local Screen Context.",
             "    launcher -r    -   Use Remote Screen Context."]

    for i in usage:
        print(i)


def appstart():
    for app in app_list:
        running = app + '.exe' in (i.name() for i in ps.process_iter())
        if not running:
            if re.search(app_list[0], app):
                os.startfile(OBSD_PATH)
                time.sleep(OBSD_DELAY)
            if re.search(app_list[1], app):
                os.startfile(SPOT_PATH)
                time.sleep(SPOT_DELAY)
            if re.search(app_list[2], app):
                os.startfile(DSCRD_PATH)
                time.sleep(DSCRD_DELAY)
            if re.search(app_list[3], app):
                os.startfile(STEAM_PATH)
                time.sleep(STEAM_DELAY)
            if re.search(app_list[4], app):
                os.startfile(BRAVE_PATH)
                time.sleep(BRAVE_DELAY)


def discord():
    """Check to see if Discord is running, open it if not, then resize and move it. """
    running = "Discord.exe" in (i.name() for i in ps.process_iter())
    if not running:
        os.startfile(DSCRD_PATH)
        time.sleep(DSCRD_DELAY)
    hwnd = gui.FindWindow(None, app_list[0])
    gui.MoveWindow(hwnd, di_dim[0], di_dim[1], di_dim[2], di_dim[3], True)


def steam():
    """
    Check to see if Steam is running, open it if not, then resize and move it.
    Check if Friends List is open, open it if not, using image recognition on menus.
    """

    running = "steam.exe" in (i.name() for i in ps.process_iter())
    if not running:
        os.startfile(STEAM_PATH)
        time.sleep(STEAM_DELAY)

    steam_window = gui.FindWindow(None, app_list[4])
    gui.MoveWindow(steam_window, sg_dim[0], sg_dim[1], sg_dim[2], sg_dim[3], True)

    if gui.FindWindow(None, "Friends List") == 0:
        x_loc, y_loc, width, height = ag.locateOnScreen(
            r'imgsrc\steammenus.png', grayscale=True, confidence=CONF)
        x_loc, y_loc = ag.locateCenterOnScreen(
            r'imgsrc\friends.png', grayscale=True,
            region=(x_loc, y_loc, width, height), confidence=CONF)
        ag.moveTo(x_loc, y_loc)
        ag.click(clicks=1, interval=0, button='left')
        x_loc, y_loc, width, height = ag.locateOnScreen(
            r'imgsrc\friendsmenu.png', grayscale=True, confidence=CONF)
        x_loc, y_loc = ag.locateCenterOnScreen(
            r'imgsrc\friendslist.png', grayscale=True,
            region=(x_loc, y_loc, width, height), confidence=CONF)
        ag.moveTo(x_loc, y_loc)
        ag.click(clicks=1, interval=0, button='left')
        friends_window = gui.FindWindow(None, "Friends List")
        gui.MoveWindow(friends_window, sf_dim[0], sf_dim[1], sf_dim[2], sf_dim[3], True)
    else:
        friends_window = gui.FindWindow(None, "Friends List")
        gui.MoveWindow(friends_window, sf_dim[0], sf_dim[1], sf_dim[2], sf_dim[3], True)


def main(args):
    """Main Driver - Parse CLI flags/options and run the related subprogram."""
    if not args:  # if no flags/args passed, apply defaults
        argument_list = ['-a', '-h']
    else:  # inherit flags/args list
        argument_list = args

    options = "ahrlgws"  # define range of possible flags

    try:  # attempt to map flags to their corresponding arguments
        arguments, values = getopt.getopt(argument_list, options)

        # logical matching for arguments to driving logic
        for current_argument, current_value in arguments:
            if current_argument == "-a":  # -Author Dialog
                author()

            if current_argument == "-h":  # -Help Dialog
                helpme()

            if current_argument == "-r":  # -Remote orientation Mode
                print("remote flag")
                print("needs to write window dimension values for remote window orientation to dim variables")
                print("then needs to run dim setting logic, or call function that does")

            if current_argument == "-l":  # -Local orientation Mode
                print("local flag")
                print("needs to write window dimension values for local window orientation to dim variables")
                print("then needs to run dim setting logic, or call function that does")

            if current_argument == "-g":  # -Gaming app launch Mode
                print("gaming flag")
                print("needs to write gaming app names and filepaths to name-path dictionary")
                print("then needs to call launch check method to iterate through dictionary and launch apps")

            if current_argument == "-w":  # -Workstation app launch Mode
                print("workstation flag")
                print("needs to write coding/development and documenation "
                      "app names and filepaths to name-path dictionary")
                print("then needs to call launch check method to iterate through dictionary and launch apps")

            if current_argument == "-s":  # -Server (Homelab) app launch Mode
                print("homelab flag")
                print("needs to write homelab site URLs and browser filepath to name-path dictionary")
                print("then needs to call launch check method to iterate through dictionary and launch apps")

    except getopt.error as err:  # if mapping fails, pass stderr through to output
        print(str(err))


if __name__ == '__main__':
    main(sys.argv[1:])
