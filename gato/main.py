import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw, Gio

Adw.init()

@Gtk.Template(filename="ui/generated/mainwindow.ui")
class MyWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MyWindow"

    # Optionally bind widgets or signals
    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        print("Button clicked!")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MyApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyApp")
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        win = MyWindow(application=app)
        win.present()

if __name__ == "__main__":
    app = MyApp()
    app.run()
