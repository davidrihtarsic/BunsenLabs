if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    echo $m
    MONITOR=$m polybar i3-multi&
  done
else
  polybar i3-LVDS1 &
fi
