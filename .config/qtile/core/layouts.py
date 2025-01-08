
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#     Configuración para distribuir y redimensionar ventanas
#        Autor: Jonattan Contreras | Versión: 1.0


# imporataciones
from libqtile import hook, layout
from libqtile.config import Group, Match
from themes.colors import *

# layout de abrir ventanas
layouts = [
    layout.Columns(
        border_focus = active_focus ,
        border_normal = normal_focus ,
        border_width=3, 
        margin=10),
    layout.Max(margin=10),
    layout.Stack(num_stacks=2, margin=5),
    layout.Floating(),
    layout.Tile(margin = 2),
     layout.TreeTab(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"), 
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(wm_class="pavucontrol"),
        Match(title="mpv"),
        Match(title="feh"),
    ],
    border_width=3

)
