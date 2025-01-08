
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#        Configuración para las áreas de trabajo
#        Autor: Jonattan Contreras | Versión: 1.0


# importaciones
from libqtile.config import Group, Key
from libqtile.lazy import lazy
from core.keys import keys, mod

# variables
groups = [Group(i) for i in "12345"]

for i, group in enumerate(groups, 1):
    keys.extend([
        Key([mod], str(i), lazy.group[group.name].toscreen()),
        Key([mod, "shift"], str(i), lazy.window.togroup(group.name)),
    ])
