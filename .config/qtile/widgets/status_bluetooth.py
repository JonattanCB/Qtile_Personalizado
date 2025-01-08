
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#              Estado de Bluetooth
#        Autor: Jonattan Contreras | Versión: 1.0

import subprocess
from libqtile.widget import base

class status_bluetooth(base.InLoopPollText):
    def __init__(self, foreground_active="", foreground_inactive="", icon="", **config):
        super().__init__(**config)
        self.foreground_active = foreground_active
        self.foreground_inactive = foreground_inactive
        self.icon = icon
        self.update_interval = 2
        self.connected = False
        self.add_callbacks({
            'Button1': self.launch
        })


    def poll(self):
        try:
            output = subprocess.check_output("bluetoothctl show | grep 'Powered: yes'", shell=True, text=True).strip()
            nuevo_estado = bool(output)

            if nuevo_estado != self.connected:
                self.connected = nuevo_estado
                self.foreground = self.foreground_active if nuevo_estado else self.foreground_inactive

            return self.icon
        except subprocess.CalledProcessError:
            self.foreground = self.foreground_inactive
            return self.icon
        except Exception:
            self.foreground = "#ff0000"
            return "Error"
    
    def launch(self):
        self.qtile.cmd_spawn("blueman-manager")
