import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class MyStatusIcon:
    def __init__(self):
        self.status_icon = Gtk.StatusIcon()
        self.status_icon.set_from_stock(Gtk.STOCK_ABOUT)
        self.status_icon.set_visible(True)
        self.status_icon.connect('activate', self.on_activate)

    def on_activate(self, icon):
        print("Status icon activated!")

if __name__ == "__main__":
    MyStatusIcon()
    Gtk.main()
