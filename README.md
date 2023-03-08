 # Basic Keylogger 
 
 The purpose of this project is to demonstrate how simple a keylogger could be and how an attacker could utilitze such scripts to spy and log a victims inputs throughout their day.
 
 # What is a Keylogger?
 
 Keyloggers are softwares, Although they could be hardwares aswell, that are designed to record and log every keystroke made on a computer or IoT device. It allows attackers to secrety monitor the activities of the user and to obtain sensitive information such as social media accounts, Banking information, Identity information and etc. These keyloggers could be uploaded to a victims computer by attaching a script to another file which may automatically download this script without any terminal or cmd opening or automatically deploy its payload with the actual keylogger script. 
 
 Although keyloggers are very simple and could be dealt with by setting proper permissions to how much libraries or programs have access to your hardware, it could be attached to a program that requires such permissions to operate. A simple way to deal with such problem is to not run "sudo" command for every program or command aswell as avoiding unnecessary "Run as Adminsitrator" for suspicious files.
 
 
 # Libraries used:
- os
  - To iterate through *nix files
- import pyxhook
  - To create stroke hooks for keyboard inputs
- threading
- datetime
  - To add timestamps to our logs
- logging 
  - To log the changes to the files
 
 ## Disclaimer

This project is intended for educational and testing purposes. Any misuse or misconfiguration of this code should not be held liable against me.
While this program can not directly affect your files, use at your own discretion.
Another thing to mention is that, this project was mainly developed for linux structure however it could also be used in windows too. If you chose to use it on windows, change the os.system command and import win32 libraries to execute codes in cmd in the background.

# Getting Started

## Prerequisites
- Python 3.8+
- Git

## Git Installation
Download the git installer from [Git](https://git-scm.com/downloads) follow the installation steps to install git on your device. If you are using linux, use the following inside terminal:
```
git --version 
```
If the output shows git with a version, then skip Git installation section as you already have git installed

If git was not installed, do the following
```
sudo apt-get update; sudo apt-get install git -y
```
or if you are using Arch based distro :
```
sudo pacman -Sy git
```

## Cloning this repository
Use the following command to clone this repository
```
git clone https://github.com/kasra-sal/Basic-Keylogger.git
```
# Demo 

https://user-images.githubusercontent.com/118489496/223849214-c5f5a99c-0c38-471d-8756-3e3bf96ff749.mp4


