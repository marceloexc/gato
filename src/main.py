import sys
import gi
import os

import pip

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

# cairo renderer does not switch to dGPU on 15' MBP.
# this should be a toggle in the app, however
# os.environ["GSK_RENDERER"] = "cairo"

from gi.repository import Gtk, Gio, Adw, Gdk


class GatoApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id='com.marceloexc.gato', flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        builder = Gtk.Builder()
        builder.add_from_file('text.ui')

        window = builder.get_object('main_window')
        window.set_application(self)

        # Ensure native macOS title bar
        window.set_titlebar(None)

        # Set up macOS menu
        self.setup_menu()

        # Get references to widgets
        text_entry = builder.get_object('global_search')  # Assuming this is your text entry

        # Create a context menu
        context_menu = Gio.Menu()
        context_menu.append("Cut", "app.cut")
        context_menu.append("Copy", "app.copy")
        context_menu.append("Paste", "app.paste")

        # Add actions
        cut_action = Gio.SimpleAction.new("cut", None)
        cut_action.connect("activate", self.on_cut)
        self.add_action(cut_action)

        copy_action = Gio.SimpleAction.new("copy", None)
        copy_action.connect("activate", self.on_copy)
        self.add_action(copy_action)

        paste_action = Gio.SimpleAction.new("paste", None)
        paste_action.connect("activate", self.on_paste)
        self.add_action(paste_action)

        # Connect the context menu to the widget
        # text_entry.connect("button-press-event", self.on_button_press, context_menu)

        window.present()

    def on_button_press(self, widget, event, context_menu):
        if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 3:
            context_menu.popup_at_pointer(event)
            return True
        return False

    def on_cut(self, action, param):
        # Implement cut functionality
        print("Cut")

    def on_copy(self, action, param):
        # Implement copy functionality
        print("Copy")

    def on_paste(self, action, param):
        # Implement paste functionality
        print("Paste")

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

    def setup_menu(self):
        # Set up your macOS menu here
        menu = Gio.Menu()
        # Add menu items...
        self.set_menubar(menu)

if __name__ == '__main__':
    app = GatoApp()
    app.run(sys.argv)
