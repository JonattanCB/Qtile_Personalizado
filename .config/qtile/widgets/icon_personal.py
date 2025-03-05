#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#           Configuracion de icon
#        Autor: Jonattan Contreras | Versión: 1.0


import subprocess
from libqtile.widget import base

class icon_personal(base.InLoopPollText):
    def __init__(self,  **config):
        super().__init__(**config)
        self.add_callbacks({
            'Button1':self.launch
        })

    def poll(self):
            return ""

    def launch(self):
        self.qtile.cmd_spawn("alacritty")

