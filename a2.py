from pynput.keyboard import Key, Controller, Listener

while True:
    keys = []
    word = ""

    a = Controller()


    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            keys.append(key.char)

        except AttributeError:
            print('special key {0} pressed'.format(
                key))


    def on_release(key):
        print('{0} released'.format(
            key))
        if key == Key.space:
            # Stop listener
            return False

    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    for key in keys:
        word += key
    a.type(string=word)
    a.type(string=' ')