#!/bin/zsh

ViewSonic="HDMI2 connected"
Xrandr_commmands="
xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0
xrandr --output HDMI2 --mode 1920x1080 --pos 0x0
xrandr --auto
"

$(echo $Xrandr_commmands | dmenu -l 10) 
