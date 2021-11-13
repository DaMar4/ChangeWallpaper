#!/usr/bin/env bash
change_wallpaper()
{
	python ./Documentos/Proyectos/renombrar.py
	var1=$(find /home/daniel/.local/share/backgrounds/ -maxdepth 1 -type f | wc -l)
	dir="/home/daniel/.local/share"
	themes=($(ls -p --hide="wallpaper.sh" $dir/backgrounds))
	theme="${themes[$(( $RANDOM % $var1 ))]}"
	feh --bg-fill "$dir/backgrounds/$theme"
}
change_wallpaper
while :
sleep 20
do
	change_wallpaper
done
