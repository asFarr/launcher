"""
Launcher v3.0 by Alex Farr
Written: 07/12-13/22
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

app_list = []
path_list = []
delay_list = []
remote_dims = []
local_dims = []


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


def loadcfg():
    # Attempt to load any YAML files in /config
    config_set = []
    for filename in os.listdir("config"):
        with open(os.path.join("config", filename), mode="rt", encoding="utf-8") as config:
            config_set.append(yaml.safe_load(config))

    for entry in config_set:
        app_list.append(entry["application"]["name"])
        path_list.append(entry["application"]["path"])
        delay_list.append(entry["load-delay"])
        remote_dims.append(entry["remote-dimensions"])
        local_dims.append(entry["local-dimensions"])


def appstart(passed_path, passed_delay):  # TODO: Currently broken
    runlist = []
    for app in app_list:
        runlist.append(app + '.exe' in (i.name() for i in ps.process_iter()))
        print(app + '.exe' in (i.name() for i in ps.process_iter()))
        # print(runlist)
        print(app)
        # print(app)
        for runcheck in runlist:
            if runcheck is True:
                if re.search(app_list[0], app):
                    print("success")
                    # os.startfile(passed_path)
                    time.sleep(passed_delay)


def windowresize(name, dim_list):
    #  TODO: If Brave do different stuff, and if Steam do different stuff
    #   otherwise take window name input, find the window, and resize it to input dims
    print(name)
    print(dim_list)

    hwnd = gui.GetForegroundWindow()
    gui.MoveWindow(hwnd, dim_list["X-Origin"], dim_list["Y-Origin"], dim_list["Width"], dim_list["Height"], True)

"""def steam():
    
    # Check to see if Steam is running, open it if not, then resize and move it.
    # Check if Friends List is open, open it if not, using image recognition on menus.
    

    running = "steam.exe" in (i.name() for i in ps.process_iter())
    if not running:
        os.startfile(STEAM_PATH)
        time.sleep(STEAM_DELAY)

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
        gui.MoveWindow(friends_window, sf_dim[0], sf_dim[1], sf_dim[2], sf_dim[3], True)"""


def main(args):
    """Main Driver - Parse CLI flags/options and run the related subprogram."""
    loadcfg()
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
                appstart(path_list[0], delay_list[0])

            if current_argument == "-w":  # -Workstation app launch Mode
                print("workstation flag")
                print("needs to write coding/development and documenation "
                      "app names and filepaths to name-path dictionary")
                print("then needs to call launch check method to iterate through dictionary and launch apps")

            if current_argument == "-s":  # -Server (Homelab) app launch Mode
                print("homelab flag")
                print("needs to write homelab site URLs and browser filepath to name-path dictionary")
                print("then needs to call launch check method to iterate through dictionary and launch apps")
                windowresize(app_list[0], local_dims[0])

    except getopt.error as err:  # if mapping fails, pass stderr through to output
        print(str(err))


if __name__ == '__main__':
    main(sys.argv[1:])
