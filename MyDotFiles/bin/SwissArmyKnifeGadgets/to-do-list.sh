#! /bin/bash

grep -v "$(sort -V ~/Files/1-ToDo/to-do-list.md | dmenu -l 10 | sed 's/^/+ /' | sed 's/+ +/-/' | tee -a ~/Files/1-ToDo/to-do-list.md | sed 's/-/+/')" ~/Files/1-ToDo/to-do-list.md >> ~/Files/1-ToDo/tmp.md && mv ~/Files/1-ToDo/tmp.md ~/Files/1-ToDo/to-do-list.md

sort -V ~/Files/1-ToDo/to-do-list.md > ~/Files/1-ToDo/tmp.md && mv ~/Files/1-ToDo/tmp.md ~/Files/1-ToDo/to-do-list.md
