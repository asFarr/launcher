# launcher
Simple window control tool using flag and argument parsing for command line automation. 

This tool is constrained to a windows environment due to it's usage of win32gui. 
It is also currently hardcoded to configure a selection of windows that I used for testing the concept. 
I will be starting my third pass over this project soon, one of the features I intend to add is a yaml file for settings configuration before runtime.
The abstractions required over my current solution will more or less require another entire redesign of the project to implement, 
but once completed it should make the tool usable by others without the significant modification of the main script that is currently required. 
