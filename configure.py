import configparser
import os


config=configparser.ConfigParser()
config.read("configure.ini")

cell_size=config.getint("size","cell_size")
cell_num_x=config.getint("size","cell_num_x")
cell_num_y=config.getint("size","cell_num_y")
snake_start_speed=config.getint("speed","snake_start_speed")
snake_speed_addonetime=config.getfloat("speed","snake_speed_addonetime")


def getcolor(str):
    str_list=str[1:-1].split(',',2)
    color=(int(str_list[0]),int(str_list[1]),int(str_list[2]))
    return color

_snake_color=config.get("color","snake_color")
snake_color=getcolor(_snake_color)
_lines_color=config.get("color","lines_color")
lines_color=getcolor(_lines_color)
_backgound_color=config.get("color","backgound_color")
backgound_color=getcolor(_backgound_color)
_apple_color=config.get("color","apple_color")
apple_color=getcolor(_apple_color)

