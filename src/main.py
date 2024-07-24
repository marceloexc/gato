import sys
import gi
import os

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# cairo renderer does not switch to dGPU on 15' MBP.
# this should be a toggle in the app, however
os.environ["GSK_RENDERER"] = "cairo"

from gi.repository import Gtk, Gio, Adw


class GatoApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.marceloexc.gato', flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        # Load the UI file
        builder = Gtk.Builder()
        builder.add_from_file('text.ui')

        # Get the main window
        window = builder.get_object('main_window')
        window.set_application(self)

        # Ensure we're using the native macOS title bar
        window.set_titlebar(None)

        # Set up the macOS menu bar
        self.setup_menu()

        # Get references to the widgets
        self.entry = builder.get_object('main-form')
        self.label = builder.get_object('main_label')
        self.button = builder.get_object('main_button')

        # Connect the button click event
        self.button.connect('clicked', self.on_button_clicked)

        window.present()

    def setup_menu(self):
        # Create a menu bar
        menu_bar = Gio.Menu()

        # Create "App" menu
        app_menu = Gio.Menu()
        app_menu.append("About", "app.about")
        app_menu.append("Quit", "app.quit")
        menu_bar.append_submenu("App", app_menu)

        # Set the menu bar for the application
        self.set_menubar(menu_bar)

        # Add actions
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_quit)
        self.add_action(quit_action)

        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.on_about)
        self.add_action(about_action)

    def on_button_clicked(self, button):
        entry_text = self.entry.get_text()
        print(f"Entry text: {entry_text}")
        self.label.set_text(f"You entered: {entry_text}")
        self.button.set_label("Text updated!")

    def on_quit(self, action, param):
        self.quit()

    def on_about(self, action, param):
        about_dialog = Gtk.AboutDialog(transient_for=self.get_active_window(), modal=True)
        about_dialog.set_program_name("gato")
        about_dialog.set_version("1.0")
        about_dialog.set_authors(["Marcelo Mendez"])
        about_dialog.set_copyright("© 2024 Marcelo Mendez")
        about_dialog.set_comments("batch gui downloader")
        about_dialog.set_website("https://github.com/marceloexc/gato")
        about_dialog.set_website_label("Visit Website")
        about_dialog.present()


if __name__ == '__main__':
    app = GatoApp()
    app.run(sys.argv)
