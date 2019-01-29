#!/bin/zsh

ViewSonic="HDMI2 connected"
Xrandr_commmands="
xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0
xrandr --output HDMI2 --mode 1920x1080 --pos 0x0
xrandr --output eDP1 --auto
xrandr --output eDP1 --rotate normal
xrandr --output eDP1 --rotate left
"

$(echo $Xrandr_commmands | dmenu -l 10) 
