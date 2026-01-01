from authentification import request, auth
from keywords import *
# the main programm opens
name = request()

print('''\n▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖    ▗▄▄▄▖▗▄▖     ▗▖  ▗▖▗▄▄▖  ▗▄▖  ▗▄▄▖
▐▌ ▐▌▐▌   ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌         █ ▐▌ ▐▌    ▐▛▚▞▜▌▐▌ ▐▌▐▌ ▐▌▐▌
▐▌ ▐▌▐▛▀▀▘▐▌   ▐▌   ▐▌ ▐▌▐▌  ▐▌▐▛▀▀▘      █ ▐▌ ▐▌    ▐▌  ▐▌▐▛▀▘ ▐▌ ▐▌ ▝▀▚▖
▐▙█▟▌▐▙▄▄▖▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖      █ ▝▚▄▞▘    ▐▌  ▐▌▐▌   ▝▚▄▞▘▗▄▄▞▘
                                                                          ''')

print("print help to list comands")
print()

keywords(name)
