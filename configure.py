import configparser
import os


config=configparser.ConfigParser()
config.read("configure.ini")

cell_size=config.getint("configure1","cell_size")
cell_num_x=config.getint("configure1","cell_num_x")
cell_num_y=config.getint("configure1","cell_num_y")
snake_start_speed=config.getint("configure1","snake_start_speed")
snake_speed_addonetime=config.getfloat("configure1","snake_speed_addonetime")