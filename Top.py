import Tkinter as tk
from Tkinter import *
import ttk
from ttk import *
from Elixer import *
from Dark_Elixer import *
from Elixer_GUI import *
from Dark_Elixer_GUI import *

class Top():
	def __init__(self):
		self.initGUI()

	def initGUI(self):
		self.root = Tk()
		self.root.resizable(width = False, height = False)
		self.root.title('CoC Elixer Calculator')
		self.root.rowconfigure(0, weight = 1)
		self.root.columnconfigure(0, weight = 1)

		self.notebook = ttk.Notebook(self.root)
		self.tab_elix = ttk.Frame(self.notebook)
		self.tab_dkelix = ttk.Frame(self.notebook)
		self.notebook.add(self.tab_elix, text = "Elixer Troops")
		self.notebook.add(self.tab_dkelix, text = "Dark Elixer Troops")
		self.elixer = Elixer_GUI(self.tab_elix)
		self.dark_elixer = Dark_Elixer_GUI(self.tab_dkelix)

		self.notebook.grid()
		self.root.mainloop()

if __name__ == '__main__':
	Top()
