
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#               Estado de Volumen
#        Autor: Jonattan Contreras | Versión: 1.0

from libqtile.widget import base
import subprocess

class status_volumen(base.InLoopPollText):
    def __init__(self, **config):
        super().__init__(**config)
        self.update_interval = 2
        self.fontsize = 15
        self.add_callbacks({
            'Button1':self.launch
        })

    def poll(self):
        try:
            output = subprocess.check_output("amixer get Master | grep -o '[0-9]*%' | head -n1", shell=True, text=True).strip().replace('%', '')
            blue = subprocess.check_output("pactl list short sinks", shell=True, text=True).strip()
            cable = subprocess.check_output("pactl list sinks | grep 'Active Port' | awk '{print $3}'", shell=True, text=True).strip()
            connect_blue = False
            connect_cable = False


            if "a2dp_sink" in blue:
                connect_blue = True
            elif "analog-output-headphone" in cable:
                connect_cable = True

            total = int(output)


            if total == 0:
                volumen = " "
            elif total < 50 :
                volumen = " "
            elif total < 60 :
                volumen = "  "
            else:
                volumen = "  "
            
            if connect_blue:
                return f"<span size='20000'>󰥰 </span>"
            elif connect_cable:
                return f"<span size='14000'> </span>"
            else:
                return volumen

        except subprocess.CalledProcessError:
            return "error en el comando"
        except Exception:
            return "error en la logica"

    def launch(self):
        self.qtile.cmd_spawn("pavucontrol") 
