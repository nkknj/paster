import re
import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		#left window
		self.txtbox_i=tk.Text(self, width=40)
		self.txtbox_i.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

		#center button
		self.button=tk.Button(self, text='-->')
		self.button['command']=self.trans
		self.button.pack(side=tk.LEFT)

		#right window
		self.txtbox_o=tk.Text(self, width=40)
		self.txtbox_o.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

	#translate raw text to fixed text
	def trans(self):
		txt_o=self.fixer()
		self.txtbox_o.delete('1.0', 'end')
		self.txtbox_o.insert('1.0', txt_o)

	#get fixed text
	def fixer(self):
		#get raw text
		text=self.txtbox_i.get('1.0', 'end -1c')

		#remove linefeed code at the top and the bottom
		text=re.sub('^\n', '', text)
		text=re.sub('\n$', '', text)

		#remove linefeed code in the text
		text=text.replace(' \n', ' ')
		text=text.replace('\n', ' ')

		#remove () things
		text=re.sub(' \(.*?\)', ' ', text)
		text=re.sub('\(.*?\)', '', text)

		#remove space in front of comma or period
		text=text.replace(' ,', ',')
		text=text.replace(' .', '.')

		#shorten long space
		text=text.replace('  ', ' ')

		return text


root=tk.Tk()
app=Application(master=root)
app.mainloop()


