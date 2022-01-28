from pynput import keyboard

def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    print('Key pressed' + k)

def on_release(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    print('Key released' + k)

listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys