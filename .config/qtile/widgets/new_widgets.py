#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#         
#        Autor: Jonattan Contreras | Versión: 1.0


import subprocess
from libqtile.widget import base

class Status(base.InLoopPollText):
    def __init__(self,  **config):
        super().__init__(**config)
        self.update_interval = 1

    def poll(self):
        try:
            output = subprocess.check_output("", shell=True, text=True ).strip()

            return output
        except subprocess.CalledProcessError:
            return "Error en comando"
        except Exception:
            return "Error en logica"

