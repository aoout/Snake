def getcolor(str):
    str_list=str[1:-1].split(',',2)
    color=(int(str_list[0]),int(str_list[1]),int(str_list[2]))
    return color


a='(255,0,0)'
c=getcolor(a)
c
type(c)
b=(255,0,0)
b
type(b)
c==b