
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

class status_bateria(base.InLoopPollText):
    def __init__(self, foreground_batery, foreground_low, **config):
        super().__init__(**config)
        self.update_interval = 3
        self.foreground_batery = foreground_batery
        self.foreground_low = foreground_low

    def poll(self):
        try:
            bateria = int(subprocess.check_output("acpi -b | awk '{print $4}'", shell=True, text=True).strip().replace('%,', ''))
            conectado = subprocess.check_output("acpi -b | awk '{print $3}'", shell=True, text=True).strip().replace(',', '')

            if "Charging" in conectado:
                icon = "  "
                color = self.foreground_batery
            else:
                if bateria < 10:
                    icon = " "
                elif bateria < 30:
                    icon = " "
                elif bateria < 50:
                    icon = " "
                elif bateria < 80:
                    icon = " "
                else:
                    icon = " "

                color = self.foreground_low if bateria < 16 else self.foreground_batery
                
            return (
                f"<span size='11500' weight='200' color='{color}'>{icon}</span>"
                f"<span weight='100' size='10100' color='{color}'>{bateria}%</span>"
            )

        except subprocess.CalledProcessError:
            return "Error en comando"
        except Exception:
            bateria = 100
            icon = "  "
            color = self.foreground_batery
            return (
                f"<span size='11500' weight='200' color='{color}'>{icon}</span>"
                f"<span weight='100' size='10100' color='{color}'>{bateria}%</span>"
            )

