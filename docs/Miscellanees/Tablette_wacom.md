# Mapper une tablmette wacom sur un seul écran

1. Trouver l'ID du stylet : `xinput | grep "stylus"`
2. Trouver l'ID de l'écran avec `xrandr`
3. Mapper le stylet sur l'écran : `xinput map-to-output 22 HDMI-2` mappe le stylet d'id 22 sur l'écran sur le port HDMI-2

