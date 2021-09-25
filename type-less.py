#!/usr/bin/python3

elements = [
[0,0,1,1,0.5,"xcalc","xcalc &"],
[1,0,1,1,0.0,"xterm","xterm &"],
[2,0,1,1,0.0,"xeyes","xeyes &"],

[0,1,1,1,0.5,"<","ssh pihole &"],
[1,1,1,1,0.0,"ssh pi@pihole","terminator -m -x ssh pihole &"],
[2,1,1,1,0.5,">","terminator --geometry=940x1080+940 -x ssh pihole &"],

[0,2,1,1,0.5,"<","terminator --geometry=940x1080+0 -x ssh jdb &"],
[1,2,1,1,0.0,"ssh pi@jdb","terminator -m -x ssh jdb &"],
[2,2,1,1,0.5,">","terminator --geometry=940x1080+940 -x ssh jdb &"],

[0,3,1,1,0.5,"Full HD","xrandr --output DP-2 --mode 1920x1080 --scale 2x2"],
[1,3,1,1,0.5,"MediathekView","GDK_SCALE=2 java -jar ~/Filme/MediathekView.jar &"],
[2,3,1,1,0.5,"   4K   ","xrandr --output DP-2 --mode 3840x2160 --scale 1x1"]]

import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Type Less!", resizable=False) #, decorated=False

        grid = Gtk.Grid()
        self.add(grid)
        self.set_position(Gtk.WindowPosition.MOUSE)

        for x in elements:
            button = Gtk.Button(label=x[5],xalign=x[4])
            button.connect("clicked", self.create_function(x[6]))
            grid.attach(button, x[0], x[1], x[2], x[3])
 
    def create_function(self, command):
        def function_template(widget):
            os.system(command)
            exit()
        return function_template
            

win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()