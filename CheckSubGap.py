import urllib.request
import json
import pyperclip
import time
import configparser
from pynput.keyboard import Key, Controller

config = configparser.ConfigParser()
config.sections()
config.read('ApiKey.SECRET.ini')
key = config['api']['key']


def get_subs_for_user(username):
    youtuber_data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + key).read()

    return format(int(json.loads(youtuber_data)["items"][0]["statistics"]["subscriberCount"]))

def get_subgap():
    pewdiepie_subs = get_subs_for_user("pewdiepie")
    tseries_subs = get_subs_for_user("tseries")
    subgap = ((int(pewdiepie_subs) - (int(tseries_subs))))
    return subgap

def send_subgap_update():
    try:
        current_gap = get_subgap()
        print(current_gap)
        if current_gap < 3000 :
            pyperclip.copy("The gap between PewDiePie and T-Series is currently: " + format(str(current_gap)))
            keyboard = Controller()
            keyboard.press(Key.ctrl)
            keyboard.press("v")
            keyboard.release(Key.ctrl)
            keyboard.release("v")
            time.sleep(1)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        time.sleep(20 * 60)
        send_subgap_update()
    except urllib.error.URLError:
        time.sleep(20 * 60)
        send_subgap_update()


send_subgap_update()

