#!/usr/bin/python

#                                             `........`     .----------`
#                                             `/ssssssss/   +MMMMMMMMMm/
#                                               -sssssssso.oMMMMMMMMNs`
#    ````         ``````    `````````````````    `+ssssssss:oNMMMMNy.   ```           `````
#  /hmmmd+.       hmmmmm. -ydmmmmmmmmmmmmmmmm      :ssssssss//mMMy-   ./ooo+/.       `ooooo-
# :MMMMMMMNy-`    dMMMMM-/NMMMMMNNNNNNNNNNNNN       .ossssssso:o/     +sssssss+-`    .sssss-
# +MMMMMMMMMNd+`  dMMMMM-sMMMMMhoooooooo+----       `:/ssssssss:      ossssssssso/.  .sssss-
# +MMMMMsdMMMMMmy-dMMMMM-sMMMMMMMMMMMMMN:          /mMs:osssssss+.    osssso+ssssss+--sssss-
# +MMMMM-`/dNMMMMNMMMMMM-sMMMMMmddddddh.         /hMMMMd:+ssssssss:   osssso .:osssssosssss-
# +MMMMM-  `.sNMMMMMMMMM-oMMMMMdyyyyyyyssssss  -yMMMMMMMN/:ssssssss+` osssso   `:+sssssssss-
# +MMMMM-     .odMMMMMMs `sNMMMMMMMMMMMMMMMMM`sNMMMMMMMMd- .ossssssso.osssso      .+sssssss`
# -sssss`       `:osso:    .:ssssssssssssssss+ossssssss+`   `:::::::::::::::        `-:::-`
#
# ###
# Obligatory fancy ASCII style logo! - A must have since 1970
#
# Feel free contribute
# Written by Markus Karl Wackermann on 20.09.2018
#
# ###

#Being specific, only import functions actually needed.
import RPi.GPIO as GPIO
from time import sleep
from sys import exit

pin=12 #This is one of two Hardware PWM Pins of the RPi, every other pin will work fine aswell, but software emulated (higher CPU load!)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p=GPIO.PWM(pin, 10)

#Note frequencies taken from this site 'https://pages.mtu.edu/~suits/notefreqs.html'
#Below notes are mixed in octave (fourth & fifth), for tetris example
#The '#' note is my variable for a break/pause, it's freq is 0.5. This is not silenced, but the lowest I could get.
#A better way to silence the piezo would be by changing the dutycycle to 0% or 100% (constant off or on, no matter the frequency)
notes = {'C' : 523.25, 'D' : 587.33, 'E' : 659.25, 'F' : 349.23, 'G' : 392.00, 'A' : 440.00, 'B' : 493.88, '#' : 0.5, 'Ab' : 415.30}
#Divide a whole note to get a half note doesn't sound good, duration timings are therefore not divided by two.
speed = {'sw' : 1,'w' : 0.8, 'h' : 0.6 , 'q' : 0.45, 'qh' : 0.25, 'qhh' : 0.15}

#Main Part of tetris, sequence 1
#Divide with '-' char, first Note(Uppercase), second Duration(lowercase)
s1 = ['E-q','B-qh','C-qh','D-q','C-qh','B-qh','A-q',
'A-qh','C-qh','E-q','D-qh','C-q','B-qhh',
'C-q','D-q','E-q','C-h','A-qh','A-q',
'D-qh','F-qh','A-h','G-qhh','F-h','E-qh',
'C-qh','E-h','D-qhh','C-h','B-qh',
'B-qh','C-q','D-q','E-qh','C-h','A-h','A-h','#-w']
#Break, sequence 2
s2 = ['E-sw','C-sw','D-sw','B-sw','C-sw','A-sw','Ab-sw','B-w','#-q',
'E-sw','C-sw','D-sw','B-sw','C-h','A-h','A-h','Ab-sw','#-sw']
#Whole song from above sequences, Theme A
tetris = [s1,s1,s2,s1,s1,s2,s1]

# -----------------------------------------------------------------------------
# If you're reading this, you shouldn't be here
# unless you know what you are doing.
# -----------------------------------------------------------------------------
#Duty cycle of 50% does his job
p.start(50)

header = '[Note]\t[Frequency]\t[Duration]'+'\n------\t-----------\t----------'
printcount = 0

def goodbye(msg = ''):
	print(msg + '\n\nDone! Have fun. Like. Comment below. Kill yourself.')
	exit()

def play_song(song):
	global header,printcount,notes,speed
	try:
		print(header)
		songposition = 0
		for x in song:
			songposition += 1
			if(songposition >= (len(song))):
				goodbye('\nSong finished...')
			for y in x:
				y = y.split('-')
				note = y[0]
				length = y[1]
				actualspeed = round(float(speed[length]),2)
				print('  '+note + '\t   ' + str(notes[note]) + '\t   ' + str(actualspeed))
				printcount += 1
				if(printcount == 23):
					printcount = 0
					print(header)
				p.ChangeFrequency(notes[note])
				sleep(actualspeed)
				p.ChangeFrequency(10)
	except KeyboardInterrupt:
		goodbye()

while True:
	play_song(tetris)
