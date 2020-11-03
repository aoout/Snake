
import configparser
import os




config=configparser.ConfigParser()
config.read("configure.ini",encoding='utf-8')

def getcolor(str):
    str_list=str[1:-1].split(',',2)
    color=(int(str_list[0]),int(str_list[1]),int(str_list[2]))
    return color

default_setting=config.getboolean("other",'default_setting')
if default_setting:
    cell_size=20
    cell_num_x=40
    cell_num_y=25
    snake_length=3
    snake_start_speed=15
    snake_speed_addonetime=0.6
    snake_speed_max=22
    snake_color=(0,128,128)
    snake_edge_color=(0,0,128)
    lines_color=(40,40,40)
    backgound_color=(0,0,0)
    apple_color=(255,0,0)
    strange_apple=False
    full_screen=False
    no_wall=False
else:
    cell_size=config.getint("size","cell_size")
    cell_num_x=config.getint("size","cell_num_x")
    cell_num_y=config.getint("size","cell_num_y")
    snake_length=config.getint("size","snake_length")
    snake_start_speed=config.getint("speed","snake_start_speed")
    snake_speed_addonetime=config.getfloat("speed","snake_speed_addonetime")
    snake_speed_max=config.getfloat("speed","snake_speed_max")
    _snake_color=config.get("color","snake_color")
    snake_color=getcolor(_snake_color)
    _snake_edge_color=config.get("color","snake_edge_color")
    snake_edge_color=getcolor(_snake_edge_color)
    _lines_color=config.get("color","lines_color")
    lines_color=getcolor(_lines_color)
    _backgound_color=config.get("color","backgound_color")
    backgound_color=getcolor(_backgound_color)
    _apple_color=config.get("color","apple_color")
    apple_color=getcolor(_apple_color)
    strange_apple=config.getboolean("other","strange_apple")
    if strange_apple:
        _strange_apple_color=config.get("other","strange_apple_color")
        strange_apple_color=getcolor(_strange_apple_color)
    full_screen=config.getboolean("other","full_screen")
    if full_screen:
        _curtain_color=config.get("other",'curtain_color')
        curtain=getcolor(_curtain_color)
    no_wall=config.getboolean("other","no_wall")
