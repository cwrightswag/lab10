##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
# House outline and roof
swag = drawpad.create_rectangle(280,230,520,430, fill = 'red')
swbg = drawpad.create_line(280,230,400,110)
swcg = drawpad.create_line(520,230,400,110)
# Square Windows and a door
swdg = drawpad.create_rectangle(320,270,350,300, fill = 'blue')
sweg = drawpad.create_rectangle(440,270,470,300, fill = 'blue')
swfg = drawpad.create_rectangle(410,430,380,380, fill = 'purple')
swgg = drawpad.create_rectangle(320,380,350,410, fill = 'blue')
swhg = drawpad.create_rectangle(440,380,470,410, fill = 'blue')
# a door handle and a chimney
swig = drawpad.create_line(520,230,520,170)
swjg = drawpad.create_line(520,170,490,170)
swkg = drawpad.create_line(490,170,490,200)
swlg = drawpad.create_oval(400,400,410,410, fill = 'black')
swmg = drawpad.create_rectangle(0,430,800,460, fill = 'green')



root.mainloop()