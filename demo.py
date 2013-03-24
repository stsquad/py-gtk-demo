#!/usr/bin/env python
#
# A simple PyGtk demo for Dad
#
#
from gi.repository import Gtk

class Demo(object):

    def registerTextWidgets(self, te1, tv1, tv2):
        # bring objects into class
        self.textEntry1 = te1
        self.textView1 = tv1
        self.textView2 = tv2

    def onDeleteWindow(self, *args):
        print "delete window"
        Gtk.main_quit(*args)

    def on_fooButton_clicked(self, button):
        # copy text from input and append
        buf = self.textView1.get_buffer()
        buf.insert_at_cursor(self.textEntry1.get_text())
        

    def on_quitButton_clicked(self, button):
        print "quit clicked"
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_from_file("demo.glade")
demo = Demo()
builder.connect_signals(demo)

window = builder.get_object("window1")
window.show_all()

# regiser the text objects to make it easier for the class to do stuff
demo.registerTextWidgets(builder.get_object("textEntry1"),
                         builder.get_object("textView1"),
                         builder.get_object("textView2"))

Gtk.main()
