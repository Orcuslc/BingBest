#!/bin/bash 

# Set picture options 
# Valid options are: none,wallpaper,centered,scaled,stretched,zoom,span ned 
picOpts="zoom" 

# File Path, the location where the Bing pics are stored, NOTICE: there are many empty spaces after the ".jpg'", which is very necessary! 
filePath=$1

# Set the GNOME3 wallpaper 
DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri '"file://'$filePath'"' 

# Set the GNOME 3 wallpaper picture options 

DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-options $picOpts 

# Exit the script 
exit