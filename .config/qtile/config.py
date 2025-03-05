
#           ██╗         ██████╗        ████████╗
#           ██║        ██╔═══██╗       ╚══██╔══╝
#           ██║        ██║   ██║          ██║   
#      ██   ██║        ██║   ██║          ██║   
#      ╚█████╔╝        ╚██████╔╝          ██║   
#       ╚════╝          ╚═════╝           ╚═╝   
#
#              Configuración de Qtile
#        Autor: Jonattan Contreras | Versión: 1.0


# importaciones
from core.keys import keys
from core.mouse import mouse
from core.groups import groups
from core.layouts import layouts
from core.screens import screens
from widgets.widgets import widget_defaults 

from libqtile import hook
from libqtile.config import Match
import os 
import subprocess

# carga la Configuración autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart/autostart.sh')
    subprocess.call([home])


# Configuración general
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D" 


# configuraciones predertmidadas para ventanas flotantes
@hook.subscribe.client_new
def float_audio_control(window):
    if window.match(Match(wm_class="pavucontrol")):
        window.floating = True
        window.width = 800
        window.height = 450
        window.center()

@hook.subscribe.client_new
def float_audio_control(window):
    if window.match(Match(wm_class="blueman-manager")):
        window.floating = True
        window.width = 800
        window.height = 450
        window.center()
