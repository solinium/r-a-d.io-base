#!/usr/bin/env python3

from os import system
from os import environ
from sys import exit
from sys import platform
from time import sleep
from requests import get
from datetime import timedelta


def getPlatform():

    global win
    global unix
    global darwin
    if platform.startswith('linux') == (True) or (
        platform.startswith('darwin')) == (True) or (
            platform.startswith('freebsd')) == (True) or (
                platform.startswith('cygwin')) == (True) or (
                    platform.startswith('riscos')) == (True) or (
                        platform.startswith('atheos')) == (True) or (
                            platform.startswith('os2')) == (True):
                                unix = (True)
                                win = (False)
    elif platform.startswith('win') == (True):
        unix = (False)
        win = (True)

    if platform.startswith('darwin') == (True):
        darwin = (True)
    else:
        darwin = (False)

    global isTravis
    isTravis = 'TRAVIS' in environ

    global updateTime
    try:
        if environ['frequency'] != (""):
            updateTime = environ['updatetime']
            updateTime = int(updateTime)
    except (KeyError):
        updateTime = (5)

    global openThreadstr
    global openThreadbool
    try:
        if environ['openthread'] != (""):
            openThreadstr = environ['openthread']
            if openThreadstr == ("true"):
                openThreadbool = (True)
            else:
                openThreadbool = (False)
    except (KeyError):
        openThreadbool = (False)

    global updateFrequencyFunction
    updateFrequencyFunction = (100)


def getAPI():

    apiurl = ("https://r-a-d.io/api")
    useragent = ("Mozilla/5.0")
    apiraw = get(url=apiurl, headers={'User-agent': useragent})

    global api
    api = apiraw.json()

    global djName
    djName = api['main']['dj']['djname']

    global djImage
    djImage = api['main']['dj']['djimage']

    global djDescription
    djDescription = api['main']['dj']['djtext']

    global isAfkStream
    isAfkStream = api['main']['isafkstream']

    global threadUrl
    threadUrl = api['main']['thread']

    global listeners
    listeners = api['main']['listeners']

    global songTitle
    songTitle = api['main']['np']

    global requesting
    requesting = api['main']['requesting']

    global startTime
    startTime = api['main']['start_time']

    global endTime
    endTime = api['main']['end_time']

    global currentTime
    currentTime = api['main']['current']


def functionAPI():

    if isAfkStream == (True):
        global isAfkStreamStr
        isAfkStreamStr = ("Automated Stream")

    global isThreadUp
    if threadUrl != (""):
        if threadUrl != ("none"):
            if djName != ("Hanyuu-sama"):
                isThreadUp = (True)
            else:
                isThreadUp = (False)
        else:
            isThreadUp = (False)
    else:
        isThreadUp = (False)


def getSongLength():

    global songLengthSeconds
    songLengthSeconds = (endTime - startTime)

    readableSongLength = str(
        timedelta(seconds=songLengthSeconds))

    tempSongLength = readableSongLength[2:3]

    global songLength
    if tempSongLength == (0):
        songLength = readableSongLength[2:7]
    else:
        songLength = readableSongLength[3:7]


def getSongTimeLeft():

    global songcTimeLeft
    songcTimeLeft = endTime - currentTime

    readableSongcTimeLeft = str(
        timedelta(seconds=songcTimeLeft))

    tempSongcTimeLeft = readableSongcTimeLeft[2:3]

    if tempSongcTimeLeft == (0):
        formattedSongcTimeLeft = readableSongcTimeLeft[2:7]
    else:
        formattedSongcTimeLeft = readableSongcTimeLeft[3:7]

    formattedSongcTimeLeft = ("%s/%s") % (
        formattedSongcTimeLeft, songLength)

    global songTimeLeft
    songTimeLeft = formattedSongcTimeLeft


def getSongTimeCurrent():

    global currentSongcTime
    currentSongcTime = (songLengthSeconds - songcTimeLeft)

    readableCurrentSongcTime = str(
        timedelta(seconds=currentSongcTime))

    tempCurrentSongcTime = readableCurrentSongcTime[2:3]

    global currentSongTime
    if tempCurrentSongcTime == (0):
        currentSongTime = readableCurrentSongcTime[2:7]
    else:
        currentSongTime = readableCurrentSongcTime[3:7]

    currentSongTime = ("%s/%s") % (
        currentSongTime, songLength)


def hybridTimer():

    global timerMax
    global timerCurrentSeconds
    global tempTitle

    timerCurrentSeconds = currentSongcTime
    timerMax = songLengthSeconds
    tempTitle = songTitle

    clear()

    print("Press ctrl+c to exit.")

    if openThreadbool == (True):
        print()
        if isThreadUp == (False):
            print("Sorry, thread is not up.")
        else:
            print("Opening thread...")
            if unix == (True):
                if darwin == (True):
                    system('open %s' % (threadUrl))
                else:
                    system('xdg-open %s' % (threadUrl))
            elif win == (True):
                system('cmd /c start %s' % (threadUrl))

    sleep(3)

    clear()
    trueBool = (True)
    if (isTravis != (True)):
        while (trueBool == (True)):
            if (timerCurrentSeconds % updateTime) == (
                0) or timerCurrentSeconds == (
                    timerMax) or tempTitle != (
                        songTitle):
                            updateAPI()
            else:
                timerCurrentSeconds = (timerCurrentSeconds + 1)

            timerCurrentReadable = str(
                timedelta(seconds=timerCurrentSeconds))

            timerCurrentTemp = timerCurrentReadable[2:3]

            if timerCurrentTemp == (0):
                timerCurrent = timerCurrentReadable[2:7]
            else:
                timerCurrent = timerCurrentReadable[3:7]

            timerCurrent = ("%s/%s") % (
                timerCurrent, songLength)

            clear()

            print(songTitle)
            print(timerCurrent)
            print()
            print("DJ: %s" % (djName))

            if isAfkStream == (True):
                print(isAfkStreamStr)

            print()
            print("Listeners: %s" % (listeners))

            sleep(1)

    # travis section
    else:
        while (trueBool == (True)):
            if (timerCurrentSeconds % updateTime) == (
                0) or timerCurrentSeconds == (
                    timerMax) or tempTitle != (
                        songTitle):
                            updateAPI()
            else:
                timerCurrentSeconds = (timerCurrentSeconds + 1)

            timerCurrentReadable = str(
                timedelta(seconds=timerCurrentSeconds))

            timerCurrentTemp = timerCurrentReadable[2:3]

            if timerCurrentTemp == (0):
                timerCurrent = timerCurrentReadable[2:7]
            else:
                timerCurrent = timerCurrentReadable[3:7]

            timerCurrent = ("%s/%s") % (
                timerCurrent, songLength)

            clear()

            print(songTitle)
            print(timerCurrent)
            print()
            print("DJ: %s" % (djName))

            if isAfkStream == (True):
                print(isAfkStreamStr)

            print()
            print("Listeners: %s" % (listeners))

            trueBool = (False)


def updateAPI():

    getAPI()
    getSongLength()
    getSongTimeLeft()
    getSongTimeCurrent()

    global timerMax
    global timerCurrentSeconds
    global tempTitle

    timerCurrentSeconds = currentSongcTime
    timerMax = songLengthSeconds
    tempTitle = songTitle

    if (timerCurrentSeconds % 100) == (0):
        functionAPI()


def clear():

    if unix == (True):
        system('clear')
    elif unix == (False):
        if win == (True):
            system('cls')
        else:
            system('clear')
    else:
        print("Error - Unix not true or false. Please report this.")


def start():

    getPlatform()
    updateAPI()
    functionAPI()
    hybridTimer()


try:
    if __name__ == ("__main__"):
        start()
        clear()

except (KeyboardInterrupt):
    clear()
    exit(0)
