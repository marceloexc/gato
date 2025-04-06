import sys

import gi
import os

os.environ["GSK_RENDERER"] = "cairo"

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw, Gio



@Gtk.Template(filename='../src/zero.ui')
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'main_window'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MyApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id='com.example.GtkApplication',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        window = self.props.active_window
        if not window:
            window = MainWindow(application=self)
        window.present()

def main():
    app = MyApp()
    return app.run(sys.argv)

if __name__ == '__main__':
    main()
