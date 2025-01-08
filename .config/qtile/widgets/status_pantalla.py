
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#              Brillo de la Pantalla
#        Autor: Jonattan Contreras | Versión: 1.0


import subprocess
from libqtile.widget import base

class status_pantalla(base.InLoopPollText):
    def __init__(self, **config):
        super().__init__(**config)
        self.update_interval = 2

    def poll(self):
        try:
            actual = int(subprocess.check_output("brightnessctl g", shell=True, text=True).strip())
            maximo = int(subprocess.check_output("brightnessctl m", shell=True, text=True).strip())
            porcentaje = (actual / maximo) * 100

            if porcentaje == 0:
                return "󰃞 "
            elif porcentaje < 40:
                return "󰃝 "
            elif porcentaje < 70:
                return "󰃟 "
            else:
                return "󰃠"

        except subprocess.CalledProcessError:
            return "error en el comando"
        except Exception:
            return "Error en la logica"

