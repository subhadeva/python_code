# Revision   : 1.0
# 
# Description: Python code to access outlook using win32com throught
#              ctypes UI.
#

import win32com.client
import ctypes


CANCEL = 2
YES = 6
NO = 7

def main():
 try:
  result = ctypes.windll.user32.MessageBoxW(0, "Enter whether you want to check the last mail", "LAST_MAIL", 3)
  if result == YES:
   outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
   inbox = outlook.GetDefaultFolder(6) 
   messages = inbox.Items
   message = messages.GetLast()
   body_content = message.body
   ctypes.windll.user32.MessageBoxW(0, body_content, "LATEST_MAIL", 1 )
  if result == NO:    
   print("No need to retrieve the last mail")
  if result == CANCEL:
   print("Previous operation cancelled")
 except WindowsError as win_err:
   print("Error !!:\n{}".format(win_err))

if __name__ == "__main__":
	main()
