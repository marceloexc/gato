import gi
import os
import pip
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

os.environ["GSK_RENDERER"] = "cairo"

from gi.repository import Gtk, Adw, Gio

Adw.init()

@Gtk.Template(filename="gato/ui/generated/mainwindow.ui")
class MyWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "MyWindow"

    entry = Gtk.Template.Child(name="entry")
    label = Gtk.Template.Child(name="label")

    # Optionally bind widgets or signals
    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        import gallery_dl
        if self.entry.get_text().split():
            self.label.set_label(str=self.entry.get_text())
            config = gallery_dl.config.load()
            print(config)
            job = gallery_dl.job.DownloadJob(self.entry.get_text(), config)
            job.run()

    @Gtk.Template.Callback()
    def get_gallery_dl(self, button):
        install_package("gallery-dl")

    @Gtk.Template.Callback()
    def try_importing(self, button):
        import gallery_dl

    @Gtk.Template.Callback()
    def remove_gallery_dl(self, button):
        uninstall_package("gallery-dl")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MyApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.marceloexc.gato")
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        win = MyWindow(application=app)
        win.present()


def install_package(package_name):
    pip.main(["install", "--upgrade", package_name])

def uninstall_package(package_name):
    pip.main(["uninstall", package_name])
        
def main():
    app = MyApp()
    app.run()
        
if __name__ == "__main__":
    main()
