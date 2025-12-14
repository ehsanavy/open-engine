#project maniger

import read_data
from tkinter import *
import editor
import scene


class Main:
	def open_project():
		pass
	def create_project():
		pass
	def delete_project():
		pass
	def window():
		win = Tk()
		win.geometry("800x600")
		win.title("OPEN ENGINE project maniger")
		def button_projects(np):
			def edit_project():
				editor.Main.main(np)
				scene.Main.name(np)
			b = Button(win,text=str(np),command=edit_project)
			b.pack()
		
		a = read_data.Data.read_projects()
		e = len(a)
		print(a)
		print(e)
		for i in range(e):
			button_projects(a[i])
		
		win.mainloop()
