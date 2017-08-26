# OSMC-Contro-Panel
## Introduction

Hello guys, this is my guide to an OSMC-Control-Panel, which allows you to control your music with your easy-to-build Control-Panel. After you built it, you're able to Play/Pause a song, let the previous or the next song play and even change the volume up and down.

This is a private project shared for everyone who wants to build a Mulitmedia-Device for your living room or anywhere else. You need at least a little knowledge about electronics.I used a Windows Computer during the project. It is not tested for Mac in Linux system. Most of the time the downloadable software can be used on Mac, too. Linux has different software or has the software you need already integrated.

This project is exentdable as you wish. If you want to build also button for controlling the menu of OSMC itself, there will be a extension of this guide soon.

## What you need

* Raspberry Pi 3 Model B with an Power Supply Unit ([link](https://www.reichelt.de/Single-board-computer/RASP-3-ALL-IN/3/index.html?ACTION=3&LA=2&ARTICLE=167080&GROUPID=6666&artnr=RASP+3+ALL+IN&SEARCH=%252A) to a Raspberry Pi Set)
* microSD Card (at least 8GB)
* Solderless Breadboard (I've used the Ever-Muse Electronic MB-102)
* five Push Buttons
* jumper wires
* NOOBS (New Out Of the Box Software) for an easy OSMC installation
* OSMC Distribution
* Keyboard, Mouse, Monitor for the Raspberry Pi
* Laptop/Computer (Windows)
* SD Formatter
* PuTTY

### Optional:

* GPIO T-adapter plate (It's an adapter for the GPIO pins, which you can plug onto the Breadboard . You see easier, where to plug in the buttons)
* GPIO rainbow Cable (Connection wire from GPIO pins to the T-adapter plate)
* **DIY Starter Kit:** This is a Complete Kit that contains hardware parts like the wires, push buttons, GPIO T-adapter plate or the GPIO rainbow Cable. There're many different Starter Kits available but [here](https://www.amazon.de/Raspberry-Handbuch-Steckbrett-K%C3%BChlk%C3%B6rper-Komponenten/dp/B01MDJPGAZ) I have the link of the Starter Kit I use.  

For a test we use also:
* one LED
* one 100 Ohm resistor

## Preparing the microSD

First of all you need to format your microSD, so that you can be sure that the microSD Card has no files on it.  
I use [SD Card Formatter](https://www.sdcard.org/downloads/formatter_4/index.html) for this. Just click on the link and download it. The program is nearly self-explanatory. Select the card you want to format and then press 'Format'.

After you've done this, we have to install NOOBS onto the microSD Card. Download the .zip [here](https://www.raspberrypi.org/downloads/noobs/). It doesn't matter if you either install NOOBS or NOOBS Lite, because you need Internet Access to download and install OSMC anyway.

Once you've donwloaded the NOOBS zip file, you'll need to extract the files from the .zip. You can use a tool like [7-Zip](http://7-zip.org/download.html).  
Then copy the extracted files onto the SD Card, but every file each, not as one folder.

## First boot
Before you boot your Raspberry Pi, make sure you've plugged the microSD Card, a Keyboard, Mouse and Monitor to it. If you've checked everything you can plug in the Power Supply Unit and the Raspberry Pi will start.

On the first boot, it will display a window in which you can connect the Raspberry Pi to your Wifi Network. You can also plug in a LAN-Cable, which makes the process easier. After that you can see serveral distributions (Operating Systems) which you can install. Select OSMC and let it install.

After installation it'll start the system and you are nearly ready to do your own things with OSMC. Select your Location and Timezone. Don't change your Hostname.  
Now your ready to explore OSMC!

## Accessing the command line via SSH

There're two ways to access the command line
* A local console login, using a connected keyboard
* Logging in over the network via SSH using client on a Windows system.

In order to work and test scripts easier we'll use the second way.
First we need to install an SSH Client on your Computer called [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).  
Linux and OS X users should have an SSH Client already. 

Next we need the IP address of the Rapsberry Pi. You can find your device's IP address in the OSMC Settings:   
Settings-> System Info -> Network

Run PuTTY and enter the IP address of your device and click 'Ok'. When prompted, enter osmc for both username and password.
You are now in the command line of your OSMC distribution.

For more information and a Tutorial for Linux/OS X click [here](https://osmc.tv/wiki/general/accessing-the-command-line/).


## Install RPi.GPIO

The first thing we have to do in the command line is to install the RPi.GPIO module. You need to install it in order to work with the GPIO pins.  
Put this commands each  into the command line:

```bash
$ sudo su
# apt-get update
# apt-get install python-pip python-dev gcc
# pip install rpi.gpio
```
It may showed some warnings but it will be sucessfully installed .

### RPi.GPIO 
To get to known with GPIO pins, here is useful picture of the GPIO pins and their labels.  
![GPIO pin](https://github.com/OliverD2000/OSMC-Control-Panel/blob/master/images/RPi3_GPIOs.png)


Use this picture if you want to connect hardware to the pins.

### RPi.GPIO Test

Now we're going to Test if the RPi.GPIO module was installed right.
We will build this circuit:  
[pin 39] --- [jumper] --- [-LED+] --- [jumper] --- [R100ohm] --- [jumper] --- [pin 40]

Type into the command line (line after line):

```bash
$ sudo su
# python
>>> import RPi.GPIO as GPIO
>>> GPIO.setmode(GPIO.BOARD)
>>> GPIO.setup(40, GPIO.OUT)
>>> GPIO.output(40, 1)
>>> GPIO.output(40, 0)
>>> GPIO.cleanup()
>>> exit()
```
When you type GPIO.output(40, 1), the LED will light up. GPIO.output(40, 0) shuts down the LED.  
If that worked for you, you can go further in this guide.  
If not then check your circuit and your code once again.

## Building the actual circuit
Finally we can build the actual circuit. It looks like this.

![Circuit](https://github.com/OliverD2000/OSMC-Control-Panel/blob/master/images/circuit%20diagram.png)

Make sure you connect every button to one GPIO pin that is free to use and to a 'Ground' pin.  
If you look on the picture from the paragraph 'RPi.GPIO' you can see that there are some pins, that have a certain function.
You have to use the ones that are not marked red or yellow and on the other side of the button the 'Ground' pin.  
So one not marked pin and one 'Ground' pin

The circuit isn't that complicated because you don't need a difficult circuit here.

## Python scripts

After being done with building the circuit, we have to write the python scripts.
In this repository is every python script you need for your Control-Panel.  
You can either donwload them on your Raspberry Pi and place them in **'/home/osmc/'** or you write them yourself by using the integrated text editor **'Nano'**.

The first way is easy and is already explained. The second way is also not that hard to do.  
In your command line type:
```bash
$ sudo su
# nano /home/osmc/example.py
```

Put for 'example.py' every name in that you want. Just make sure that it is ending with '.py'.  
Now you've opened a python script in the file editor 'Nano'.  You can write into this file one code which is in this repository. For every script that is in this repository (right now there are five) you need to make a new python script with:
```bash
$ sudo su
# nano /home/osmc/example.py
```

When you've wrote one code into one script you can save that code with **CTRl+X** and press enter if you don't want to change the name of the script.
After this, you have to change the file permissions. Type:
```bash
# chmod +x /home/osmc/*.py
```

If you want to test the script, type into the command line:
```bash
#  python /home/osmc/example.py
```

If the button does what it should do, then you go on with this guide.

## Run scripts on startup

To let the script run on startup, in order to use it right after you started OSMC, we need to change the rc.local file. 
It is a shell script that is run when the system is started up. Type this code to open the file:
```bash
$ sudo su
# nano /etc/rc.local
```
You'll see something like this:
```shell
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

exit 0
```
Then put into this script the following code before 'exit 0' and after '# By default this script does nothing':
```shell
sudo python /home/osmc/voldo.py &
sudo python /home/osmc/volup.py &
sudo python /home/osmc/Start.py &
sudo python /home/osmc/Prev.py &
sudo python /home/osmc/Next.py &
```

If you used different python script names then insert yours into the code.  
Don't forget the '&' after every command. You need this otherwise you could get an error, or your system will never start.
When you put the command into the file save the file and reboot your Raspberry Pi.

Every button should now work as intended by the scripts.  
If not then check the 'rc.local' file again and your python scripts.

## Optional possibilities

If you want to go one step further you can now try to write a script for controlling the OSMC menu with buttons.
In the abstract you only have to change the 'xbmc-send' command.  
But that's something I didn't try yet.