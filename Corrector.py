from pynput.keyboard import Key, Controller, Listener

# TODO: Add backspace functionality,expand database...
d = {}
with open("wordlist.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[key] = val  # Turning file to dictionary
while True:
    keys = []
    word = ""
    i = 1

    controller_object = Controller()  # init keyboard manager object


    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(key.char))  # log key pressed to console
            keys.append(key.char)
            # If key entered is special i.e not alphanumeric print special key
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
            if key == Key.backspace:
                if keys:
                    keys.pop()


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
    word = word.join(keys)  # concat keys into word

    if word in d.keys():  # check if word exists in dictionary
        correction = d[word]  # fetch correction from dict
        for i in range(len(word) + 1):  # delete entire word and space
            controller_object.press(Key.backspace.value)
            controller_object.release(Key.backspace.value)
        controller_object.type(correction)  # write correction and space
        controller_object.type(" ")
