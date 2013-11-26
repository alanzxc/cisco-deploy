# GUI for cisco-deploy and portscan - Beta
# 
# Script by Steven Grove (@sigwo)
#           www.sigwo.com
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#

from Tkinter import *
from tkFileDialog import askopenfilename
class mywidgets:
	def __init__(self,root):
		frame=Frame(root)
		self.makeMenuBar(frame)
		self.txtfr(frame)
		frame.pack()
		return
	#defines the text area
	def txtfr(self,frame):
		textfr = Frame(frame)
		self.text = Text(textfr,height = 50,width = 150,background='white')
		scroll = Scrollbar(textfr)
		self.text.configure(yscrollcommand = scroll.set)
		self.text.pack(side = LEFT)
		scroll.pack(side = RIGHT,fill = Y)
		textfr.pack(side = TOP)
		return
	#defines menubar
	def makeMenuBar(self,frame):
		menubar = Frame(frame,relief = RAISED,borderwidth = 1)
		menubar.pack()
		mb_file = Menubutton(menubar,text = 'File')
		mb_file.pack(side = LEFT)
		mb_file.menu = Menu(mb_file)
		mb_file.menu.add_command(label = 'Open',
		command = self.file_open)
		mb_edit = Menubutton(menubar,text = 'Edit')
		mb_edit.pack(side = LEFT)
		mb_edit.menu = Menu(mb_edit)
		mb_edit.menu.entry_configure(label = 'Copy',command=lambda: frame.event_generate("<<Copy>>"))
		mb_edit.menu.entry_configure(label = 'Paste',command=lambda: frame.event_generate("<<Paste>>"))
		mb_help = Menubutton(menubar,text = 'Help')
		mb_help.pack(padx = 25,side = RIGHT)
		mb_file['menu'] = mb_file.menu
 		mb_edit['menu'] = mb_edit.menu
		return
	#defines file_open which is called when file option open is chosen
	#displays the files giving the user choice to choose  file
	def file_open(self):
		root = Tk()
		filename =askopenfilename(filetypes=[("allfiles","*"),("pythonfiles","*.py")])
		print filename
        


def main():
	root = Tk()
	k = mywidgets(root)
	root.title('interface')
	root.mainloop()
main()
