
# The Cerealbox toolkit: Window Launcher v3.0 
by: Alex Farr\
`Release Dates: v1: 01/18/21, v2: 04/28/22, v3: 07/12/22`

---
### v3 Changelog

- YAML Config files have been added under `/config`, config ingest has been implemented in `def loadcfg():`.\
    Config is loaded iteratively by a for loop based on the number of files present in `/config`. \
    Each config file is expected to conform to the schema: 
  ```
    - application
      - name
      - path
    - load-delay
    - local-dimensions
      - n-window_instances
    - remote-dimensions
      - n-window_instances
    - comments
    ```

- -t and -m have been replaced by `-l` and `-r` in the flag parser. 
- Updated usage guide printed by `help` function to reflect the new flag options. 
    
#### TODO:
- Add full named flags in addition to single letter flags.
- `-l` and `-r` need to be fully documented, and new control logic needs to be built. 
- Refactor `def appstart()` function to handle being called with the app list flags `-g`, `-s`, and `-w`. \
`def appstart()` has been refactored to `def appstart(passed_path, passed_delay)`, initial tests are using `-g`. \
Logic needs to be reworked, does not correctly detect Brave being open during testing.

---

### v2 Documentation

An automation-ready command line tool for launching and organizing windows into predefined
configurations to optimize workflow.

This tool is constrained to a Windows environment due to its usage of win32gui. 

It is also currently hardcoded to configure a selection of windows that I used for testing
the concept.

```
    Usage: python launcher.py {-a, -h} {-t|-m}
        Default flags are -a and -h.

    Examples:
    launcher.py -a    -   Display the author tag.
    launcher.py -h    -   Display the help dialog.
    launcher.py -t    -   Runs 'tall' window configuration settings
    launcher.py -m    -   Runs 'mid' window configuration settings
```

v2 Changelog:

Default browser launch support and resizing system left in place, webbrowser module used within launch support to open URL in new tab. 

Updated help and usage flag output, as well as top comments. 

Added function comment for set_dimensions.

Chose to remove Teams launch support, and rely on OS boot to kick off Teams since it's a parasite inside of Windows already. Should be fine. 

Merging back into master branch after this. 

Known Issues:
Spotify must not be playing any media in order to be targeted successfully.

Brave AppLaunch always fails runtime check and opens a new browser tab.

Brave AppLaunch will move and resize all currently open Brave windows.

---

### v1 Documentation

This script is built specifically for my personal desktop, and is designed to open and organize
applications that I always want in the same place. Due to this fact, it employs constants which
correspond to the relative window positions required on my specific resolution and configuration.

Other dependencies than those imported here are required for execution of this script.
When installing dependencies through pip, follow this order for optimal results:
opencv-python, Pillow, pyautogui, pywin32, psutil

'psutil' is used to check the process tree for an instance of the application and stores the result
in the boolean 'running'. If the boolean is False, then os.startfile is used to call the binaries
from the qualified paths stored in the associated constants, where 'time' is used to delay further
script execution based on predefined constants to allow for the processes to load fully.

```python
DSCRD_DELAY = int(sec)  # used to control how long script execution pauses while loading Discord.
STEAM_DELAY = int(sec)  # used to control how long script execution pauses while loading Steam.
```

```python
DSCRD_PATH = r'__path__'  # fully qualified filepath for Discord binaries, usually in AppData Local.
STEAM_PATH = r'__path__'  # fully qualified filepath for Steam binaries, usually in ProgramFiles.
```

'win32gui' is used to grab the COM Object for the window handler associated with each application,
based on their window title information. Once each handler is found, it is manipulated according
to the dimensions specified in the following constant arrays.

```python
DI_DIM = [x_loc, y_loc, width, height]  # location and dimensions for Discord chat.
ST_DIM = [x_loc, y_loc, width, height]  # location and dimensions for Steam Games list.
SF_DIM = [x_loc, y_loc, width, height]  # location and dimensions for Steam Friends list.
```

'pyautogui' is used if the COM Object for Steam Friends List cannot be found. It references the
contents of `/imgsrc` in order to locate and navigate through the top menu of the Steam Games list
to open the Friends List according to an image-matching confidence value defined in CONF.

`CONF = float(0-1)` -- used to control the accuracy restrictions on the image recognition phase.
Lower than .4 appears to regularly produce false-positives, and higher than `.6 - .7` seems
unable to locate references in screen space.

Also, on a final note, for the script not to fail in various places the following two configs
must be met:

`Steam -> View -> Small Mode` (might make this an image recognition check at some point)
Discord must be on friends list, no specific user or server chat may be pulled up.
