#! python3
# mapIt.py - Launches a map in the web browser using an address from the command line. 

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from the command line
    address = ''.join(sys.argv[1:])
else: 
    #get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)