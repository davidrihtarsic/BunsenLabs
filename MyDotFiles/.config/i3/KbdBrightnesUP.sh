#!/bin/zsh

KBD=$(cat /sys/class/leds/asus::kbd_backlight/brightness);
KBD=$[KBD+1];
if [ "$KBD" -gt "3" ];
	then KBD=3;
fi;
echo $KBD;
echo $KBD > /sys/class/leds/asus::kbd_backlight/brightness