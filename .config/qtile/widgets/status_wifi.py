
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#                Estado de WiFi
#        Autor: Jonattan Contreras | Versión: 1.0


import subprocess
from libqtile.widget import base
from libqtile import hook
from libqtile.config import Match

class status_wifi(base.InLoopPollText):
    def __init__(self,foreground_active="", foreground_inactive="", icon="", **config):
        super().__init__(**config)
        self.foreground_active = foreground_active
        self.foreground_inactive = foreground_inactive
        self.icon = icon
        self.update_interval = 5
        self.connected = False
        self.add_callbacks({
            'Button1': self.launch
        })

    def poll(self):
        try:
            output = subprocess.check_output("ip -4 -o a show wlan0 | awk '{print $4}'", shell=True, text=True).strip()
            avion = subprocess.check_output("nmcli radio wifi", shell=True, text=True).strip()
            nuevo_estado = bool(output)

            if "enabled" in avion :
                if nuevo_estado != self.connected:
                    self.connected = nuevo_estado
                    self.foreground = self.foreground_active if nuevo_estado else self.foreground_inactive

                return self.icon
            else:
                self.foreground = self.foreground_active
                return " "

        except subprocess.CalledProcessError:
            self.foreground = self.foreground_inactive
            return self.icon
        except Exception as e:
            self.foreground = "#ff0000"
            return "Error"
    
    def launch(self):
        try:
            subprocess.check_output("pgrep -f 'alacritty.*--class iwctl-terminal'", shell=True)
        except subprocess.CalledProcessError:
            self.qtile.cmd_spawn("alacritty --class iwctl-terminal -e iwctl")

@hook.subscribe.client_new
def float_iwctl(window):
    if window.match(Match(wm_class="iwctl-terminal")):
        window.floating = True
        window.width = 800
        window.height = 450
        window.center()  
