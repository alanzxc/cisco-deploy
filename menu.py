# http://stackoverflow.com/questions/8449053/how-to-make-menubar
from Tkinter import *
from tkFileDialog import askopenfilename
class mywidgets:
	def __init__(self,root):
		frame=Frame(root)
		self.make_menu(frame)
		self.txtfr(frame)
		frame.pack()
		return
	def txtfr(self,frame):
		textfr = Frame(frame)
		self.text = Text(textfr,height = 100,width = 150,background='white')
		scroll = Scrollbar(textfr)
		self.text.configure(yscrollcommand = scroll.set)
		self.text.pack(side = LEFT)
		scroll.pack(side = RIGHT,fill = Y)
		textfr.pack(side = TOP)
		return
	def make_menu(self, w):
		global the_menu
		the_menu = Tkinter.Menu(w, tearoff=0)
		the_menu.add_command(label="Cut")
		the_menu.add_command(label="Copy")
		the_menu.add_command(label="Paste")
		the_menu.add_command(label="Delete")
	def show_menu(self, e):
		global the_menu
		w = event.widget
		the_menu.entryconfigure("Cut",
		command=lambda: w.event_generate("<<Cut>>"))
		the_menu.entryconfigure("Copy",
		command=lambda: w.event_generate("<<Copy>>"))
		the_menu.entryconfigure("Paste",
		command=lambda: w.event_generate("<<Paste>>"))
		# no <<Delete>> as generic event - there is <<Clear>>
		# http://www.tcl.tk/man/tcl8.5/TkCmd/event.htm
		the_menu.entryconfigure("Delete",
		command=lambda: w.event_generate("<<Clear>>"))
		the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)
	#defines file_open which is called when file option openis choosen
	#displays the files giving the user choice to choose  file
	def file_open(self):
		root = Tk()
		filename =askopenfilename(filetypes=[("allfiles","*"),("pythonfiles","*.py")])
		print filename
def main():
	root = Tk()
	k = mywidgets(root)
	root.title('menu')
	root.mainloop()
main()