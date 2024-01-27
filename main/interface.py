import tkinter as tk
from settingsHandler import SettingsHandler

class MyInterface:
    def __init__(self, root, settings_handler):
        self.root = root
        root.title("Audibly Audible")
        root.geometry("400x250")

        self.settings_handler = settings_handler

        self.label = tk.Label(root, text="Audibly Audible", font=("Arial", 20) )
        self.label.pack(pady=20, padx=30)
        

        self.currentDBLevel = tk.Label(text="69 dB", font=("Arial", 15))
        self.currentDBLevel.pack()

        self.activeLabel = tk.Label(root, text="INACTIVE", font=("Arial", 20) )
        self.activeLabel.pack(pady=20, padx=30)

        self.button = tk.Button(root, text="Click to activate", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.settings_handler.system_enabled = not self.settings_handler.system_enabled
        sysEnabled = self.settings_handler.system_enabled
        self.activeLabel.config(text=f"{'ACTIVE' if sysEnabled else 'INACTIVE'}")
        self.button.config(text=f"Click to {'deactivate' if sysEnabled else 'activate'}")

def run_interface():
    settings_handler = SettingsHandler()
    root = tk.Tk()
    app = MyInterface(root, settings_handler)
    root.mainloop()

if __name__ == "__main__":
    run_interface()
