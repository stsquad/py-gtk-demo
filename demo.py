#!/usr/bin/env python
#
# A simple PyGtk demo for Dad
#
#
from gi.repository import Gtk

class Demo(object):

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def on_quitButton_clicked(self, button):
        print "quit clicked"
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_from_file("demo.glade")
builder.connect_signals(Demo())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
