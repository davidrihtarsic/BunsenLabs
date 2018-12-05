#!/usr/bin/env zsh
# gets the emoji from DMENU and copy it to clipboard

grep -v "#" ~/bin/emoji/emojis | dmenu -i -l 20 -fn "Monospace-28" | awk '{print $1}' | tr -d '\n' | xsel -i --clipboard
pgrep -x dunst > /dev/null && notify-send "$(xsel -o --clipboard) copied to clipboard"
