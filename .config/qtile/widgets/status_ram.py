
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#         Identificar Memoria RAM
#        Autor: Jonattan Contreras | Versión: 1.0


import subprocess
from libqtile.widget import base

class status_ram(base.InLoopPollText):
    def __init__(self, **config):
        super().__init__(**config)
        self.update_interval = 2

    def poll(self):
        try:
            uso = subprocess.check_output("free -h | grep 'Mem' | awk '{print $3}'",shell=True, text=True).strip()
            capacidad = subprocess.check_output("free -h | grep 'Mem' | awk '{print $2}'",shell=True, text=True).strip()

            return f"󰍛 {uso} / {capacidad}"
        except subprocess.CalledProcessError:
            return "error en el comando"
        except Exception:
            return "Error"

