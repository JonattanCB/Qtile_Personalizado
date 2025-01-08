
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#    Configuración de los monitores y la barra
#        Autor: Jonattan Contreras | Versión: 1.0


# importaciones
from libqtile import bar, widget
from libqtile.config import Screen, Group
from libqtile.lazy import lazy
from themes.colors import *
from widgets.status_wifi import status_wifi
from widgets.status_bluetooth import status_bluetooth
from widgets.status_volumen import status_volumen
from widgets.status_capacidad import status_capacidad
from widgets.status_ram import status_ram
from widgets.status_pantalla import status_pantalla
from widgets.icon_personal import icon_personal
from widgets.status_battery import status_bateria


# clases de diseño
def sep(text,color):
    return widget.TextBox(
        text = text,
        font="JetBrainsMono Nerd Font",
        fontsize = 26,
        foreground = color,
        padding = 0,
    )

# pantalla del top principal
screens = [
    Screen(
        top=bar.Bar(
            [ 
                # Izquierda
                widget.GroupBox(
                    font="Font Awesome 6 Brands",
                    fontsize = 12,
                    background = color_work,
                    padding_y = 7,
                    padding_x = 12,
                    spacing = 2,
                    highlight_method="block",
                    borderwidth = 5,
                    rounded = True,
                    disable_drag = True,
                    use_mouse_wheel=True,
                    active = active,
                    inactive = inactive,
                    this_current_screen_border= background,
                ),
                sep("",color_work),

                # Centro
                widget.Spacer(length=bar.STRETCH),
                sep("",color_medio),

                status_ram(
                    fontsize = 14,
                    padding = 10,
                    foreground = color1,
                    background = color_medio
                ),
                sep("", color_medio),
                sep("",color_medio),
                status_capacidad(
                    fontsize = 13,
                    foreground = color1,
                    background = color_medio,
                    padding = 14
                ), 
                sep("", color_medio),
                sep("",color_icon),
                icon_personal(
                    fontsize = 21,
                    padding = 16,
                    foreground = color1,
                    background = color_icon,
                ),
                sep("",color_icon),
                sep("",color_medio),
                status_bateria(
                    foreground_batery = color1,
                    foreground_low = color_rojo,
                    background = color_medio,
                    padding = 18,
                    fontsize = 14
                ),
                sep("",color_medio),
                sep("",color_medio),
                status_wifi(
                    foreground_active = active,
                    foreground_inactive = inactive,
                    icon=" ",
                    fontsize = 14,
                    padding = 14,
                    background = color_medio
                ),
                status_pantalla(
                    fontsize = 14,
                    padding =14,
                    background = color_medio
                ),
                status_bluetooth(
                    foreground_active = active,
                    foreground_inactive = inactive,
                    icon=" ",
                    fontsize = 18,
                    padding = 12,
                    background = color_medio
                ),
                status_volumen( 
                    padding=12,
                    background = color_medio
                ),
                sep("",color_medio),
                widget.Spacer(length=bar.STRETCH),
                #Derecha
                sep("",color_medio),
                widget.Clock(
                    format = "%a, %d %b [<span weight='bold'>%H:%M</span>]",
                    fontsize = 14,
                    padding = 28,
                    background = color_medio
                ),
            ],
            30,
            background = background,
            margin = [10,12,0,12],
        ),
    ),
]

