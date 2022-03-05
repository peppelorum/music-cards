#!/usr/bin/env python
#from readtest import *
import re
from CardList import CardList
from Reader import Reader
import sys
import subprocess
import os
import time

reader = Reader()
cardList = CardList()

print('Ready: place a card on top of the reader')

while True:
    card = reader.readCard()
    try:
        print('Read card', card)
        plist = cardList.getPlaylist(card)
        print('Playlist', plist)
        if plist != '':
            subprocess.check_call( ["./haplaylist.sh %s" % plist], shell=True)
        list(range(10000))       # some payload code
        time.sleep(0.2)    # sane sleep time of 0.1 seconds
    except OSError as e:
        print("Execution failed:")
        list(range(10000))       # some payload code
        time.sleep(0.2)    # sane sleep time of 0.1 seconds

