#!/bin/python3
from gi.repository import Poppler, Gtk

def draw(widget, cr):
        # set background.
        cr.set_source_rgb(0.7, 0.6, 0.5)
        cr.paint()

        # set page background
        cr.set_source_rgb(1, 1, 1)
        cr.rectangle(0,0,800,400)

        cr.fill()
        page.render(cr)

filepath = "/home/da/test.pdf"
f11 = open(filepath, "rb")
data1 = f11.read()
f11.close()

document = Poppler.Document.new_from_data(data1, None)
page = document.get_page(0)
print (document.get_n_pages())


window = Gtk.Window(title="Hello World")
window.connect("delete-event", Gtk.main_quit)
window.connect("draw", draw)
window.set_app_paintable(True)

window.show_all()
Gtk.main()
