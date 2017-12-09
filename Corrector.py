from pynput.keyboard import Key, Controller, Listener

# TODO: Add backspace functionality,expand database...
with open('file.txt') as f:
    d = dict(x.rstrip().split(None, 1) for x in f)  # Turning file to dictionary
while True:
    keys = []
    word = ""
    i = 1

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
    for key in keys:  # creating word
        word += key

    if word in d.keys():
        correction = d[word]
        a.press(Key.backspace.value)
        a.release(Key.backspace.value)
        while i <= len(word):
            a.press(Key.backspace.value)
            a.release(Key.backspace.value)
            i += 1
        a.type(correction)
        a.type(" ")
