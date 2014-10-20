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
sweg = drawpad.create_rectangle(280,230,520,430)
yolo = drawpad.create_line(280,230,400,110)
ni = drawpad.create_line(520,230,400,110)
# Square Windows and a door
swua = drawpad.create_rectangle(320,270,350,300)
swug = drawpad.create_rectangle(440,270,470,300)
swag = drawpad.create_rectangle(410,430,380,380)
swbg = drawpad.create_rectangle(320,380,350,410)
swcg = drawpad.create_rectangle(440,380,470,410)
# 



root.mainloop()