#!/bin/zsh

KBD=$(cat /sys/class/leds/asus::kbd_backlight/brightness);
KBD=$[KBD-1];
if [ "$KBD" -lt "0" ];
	then KBD=0;
fi;
echo $KBD;
echo $KBD > /sys/class/leds/asus::kbd_backlight/brightness