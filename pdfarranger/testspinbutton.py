import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
print('Installed GTK+ version is ' +
      '.'.join([str(Gtk.get_major_version()),
                str(Gtk.get_minor_version()),
                str(Gtk.get_micro_version())]))
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Test spinbutton defaults")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.adjustment = Gtk.Adjustment(value=42, lower=0, upper=100, step_increment=1, page_increment=10, page_size=5)
        self.spinbutton = Gtk.SpinButton(adjustment=self.adjustment)
        self.box.pack_start(self.spinbutton, True, True, 0)

        self.adjustment_depr = Gtk.Adjustment(42, 0, 100, 1, 10, 5)
        self.spinbutton_depr = Gtk.SpinButton(adjustment=self.adjustment_depr)
        self.box.pack_start(self.spinbutton_depr, True, True, 0)

    def on_button_clicked(self, widget):
        print("Hello World")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
