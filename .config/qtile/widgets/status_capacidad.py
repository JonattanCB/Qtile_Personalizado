
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#              Capacidad del Disco
#        Autor: Jonattan Contreras | Versión: 1.0


from libqtile.widget import base
import subprocess

class status_capacidad(base.InLoopPollText):
    def __init__(self, **config):
        super().__init__(**config)
        self.update_interval = 2

    def poll(self):
        try:
            capacidad = subprocess.check_output("df -h | grep '/dev/nvme0n1p3' | awk '{print $2}'", shell=True, text=True).strip()
            usado = subprocess.check_output("df -h | grep '/dev/nvme0n1p3' | awk '{print $3}'",shell=True, text=True).strip()
            return f"  {usado} / {capacidad}"
        except subprocess.CalledProcessError:
            return "Error en el comando"
        except Exception as e:
            return "Error"

