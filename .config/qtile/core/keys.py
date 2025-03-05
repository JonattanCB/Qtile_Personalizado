
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#        Configuración para los atajos de teclado
#        Autor: Jonattan Contreras | Versión: 1.0


# importaciones
from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess


# variantes
mod = "mod4"
alt = "mod1"
terminal = guess_terminal()
navegacion = "brave"
captura = "flameshot gui"

# atajos
keys = [
    # asignar atajos
    Key([mod], "Return", lazy.spawn(terminal), desc="Abrir terminal"),
    Key([mod], "g",  lazy.spawn(navegacion), desc="Abrir navegacion"),
    Key([mod], "print", lazy.spawn(captura), desc="tomar captura de pantalla"),
    Key([mod], "XF86AudioMute", lazy.spawn("amixer set Master 0%  /home/j0tt/Scripts/volume_brightness.sh volume_mute" ), desc="mutear el autdio"),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 1%- /home/j0tt/Scripts/volume_brightness.sh volume_down"),desc="Reducir el audio"),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 1%+"), desc="Aumentar el audio"),
    Key([mod], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Reducir el brillo"),
    Key([mod], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+"), desc="Aumentar el brillo"),
    Key([mod], "i", lazy.spawn("/opt/idea-IU-243.22562.218/bin/idea.sh"), desc="Abrir idea"),

    # mover foco ventanas
    Key([mod], "Left", lazy.layout.left(), desc="Mover foco a la izquierda"),
    Key([mod], "Right", lazy.layout.right(), desc="Mover foco a la derecha"),
    Key([mod], "Down", lazy.layout.down(), desc="Mover foco abajo"),
    Key([mod], "Up", lazy.layout.up(), desc="Mover foco arriba"),
    # mover ventanas
    Key([mod, "control"], "Left", lazy.layout.shuffle_left(), desc="Mover ventana a la izquierda"),
    Key([mod, "control"], "Right", lazy.layout.shuffle_right(), desc="Mover ventana a la derecha"),
    Key([mod, "control"], "Down", lazy.layout.shuffle_down(), desc="Mover ventana abajo"),
    Key([mod, "control"], "Up", lazy.layout.shuffle_up(), desc="Mover ventana arriba" ),
    # tamaño de ventana
    Key([mod, alt], "Left", lazy.layout.grow_left(), desc="Tamaño ventana a la izquierda"),
    Key([mod, alt], "Right", lazy.layout.grow_right(), desc="Tamaño ventana a la derecha"),
    Key([mod, alt], "Down", lazy.layout.grow_down(), desc="Tamaño ventana abajo"),
    Key([mod, alt], "Up", lazy.layout.grow_up(), desc="Tamaño ventana arriba"),
    # Configuración qtile
    Key([mod, alt, "control"], "r", lazy.reload_config(), desc="Reiniciar Qtile"),
    Key([mod, alt, "control"], "q", lazy.shutdown(), desc="Reiniciar sesion Qtile"),
    Key([mod], "w", lazy.window.kill(), desc="Cerrar ventana" ),
    Key([mod, "control"],"f" , lazy.window.toggle_fullscreen(), desc="Pantalla completa" ),

]


