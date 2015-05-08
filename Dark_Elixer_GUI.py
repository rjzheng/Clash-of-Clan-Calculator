from Dark_Elixer import *
import Tkinter as tk
from Tkinter import *
import ttk
from ttk import *

class Dark_Elixer_GUI():
	def __init__(self, parent):
		self.parent = parent
		
		self.troop = ttk.Label(self.parent, text = 'Troop')
		self.troop.grid(row = 0, column = 0)
		self.level = ttk.Label(self.parent, text = "Level")
		self.level.grid(row = 0, column = 1)
		self.quantity = ttk.Label(self.parent, text = "Quantity")
		self.quantity.grid(row = 0, column = 2)
		self.total = ttk.Label(self.parent, text = "Total")
		self.total.grid(row = 0, column = 3)

		self.calculate_label = ttk.Label(self.parent, \
							text = 'Total Dark Elixer:')
		self.calculate_label.grid(row = 16, column = 0)
		self.total_var = StringVar()
		self.total_var.set("Calculate")
		self.calculate_entry = ttk.Button(self.parent, \
							textvariable = self.total_var, \
							command = self.total_calc)
		self.calculate_entry.grid(row = 16, column = 3)

		self.minion = ttk.Label(self.parent, text = "Minion:")
		self.minion.grid(row = 1, column = 0)
		self.hog_rider = ttk.Label(self.parent, text = "Hog Rider:")
		self.hog_rider.grid(row = 2, column = 0)
		self.valkyrie = ttk.Label(self.parent, text = "Valkyrie:")
		self.valkyrie.grid(row = 3, column = 0)
		self.golem = ttk.Label(self.parent, text = "Golem:")
		self.golem.grid(row = 4, column = 0)
		self.witch = ttk.Label(self.parent, text = "Witch:")
		self.witch.grid(row = 5, column = 0)

		self.level_min = ttk.Combobox(self.parent)
		self.level_min['values'] = ('1', '2', '3', '4', '5', '6')
		self.level_min.grid(row = 1, column = 1)
		self.level_hog = ttk.Combobox(self.parent)
		self.level_hog['values'] = ('1', '2', '3', '4', '5')
		self.level_hog.grid(row = 2, column = 1)
		self.level_valk = ttk.Combobox(self.parent)
		self.level_valk['values'] = ('1', '2', '3', '4')
		self.level_valk.grid(row = 3, column = 1)
		self.level_golem = ttk.Combobox(self.parent)
		self.level_golem['values'] = ('1', '2', '3', '4', '5')
		self.level_golem.grid(row = 4, column = 1)
		self.level_witch = ttk.Combobox(self.parent)
		self.level_witch['values'] = ('1', '2')
		self.level_witch.grid(row = 5, column = 1)

		self.q1 = ttk.Entry(self.parent)
		self.q1.grid(row = 1, column = 2)
		self.q2 = ttk.Entry(self.parent)
		self.q2.grid(row = 2, column = 2)
		self.q3 = ttk.Entry(self.parent)
		self.q3.grid(row = 3, column = 2)
		self.q4 = ttk.Entry(self.parent)
		self.q4.grid(row = 4, column = 2)
		self.q5 = ttk.Entry(self.parent)
		self.q5.grid(row = 5, column = 2)

		self.b1_var = StringVar()
		self.b1_var.set(0)
		self.b1 = ttk.Button(self.parent, textvariable = self.b1_var, \
				command = self.minion_calc)
		self.b1.grid(row = 1, column = 3)
		self.b2_var = StringVar()
		self.b2_var.set(0)
		self.b2 = ttk.Button(self.parent, textvariable = self.b2_var, \
				command = self.hog_calc)
		self.b2.grid(row = 2, column = 3)
		self.b3_var = StringVar()
		self.b3_var.set(0)
		self.b3 = ttk.Button(self.parent, textvariable = self.b3_var, \
				command = self.valk_calc)
		self.b3.grid(row = 3, column = 3)
		self.b4_var = StringVar()
		self.b4_var.set(0)
		self.b4 = ttk.Button(self.parent, textvariable = self.b4_var, \
				command = self.golem_calc)
		self.b4.grid(row = 4, column = 3)
		self.b5_var = StringVar()
		self.b5_var.set(0)
		self.b5 = ttk.Button(self.parent, textvariable = self.b5_var, \
				command = self.witch_calc)
		self.b5.grid(row = 5, column = 3)

	def minion_calc(self):
		self.ET = Dark_Elixer()
		self.level_troop = self.level_min.get()
		self.quantity_troop = self.q1.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total1 = int(self.ET.minion[self.level_troop]) * \
					int(self.quantity_troop)
			self.b1_var.set(self.total1)
		else:
			self.total1 = 0
			self.b1_var.set(self.total1)

	def hog_calc(self):
		self.ET = Dark_Elixer()
		self.level_troop = self.level_hog.get()
		self.quantity_troop = self.q2.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total2 = int(self.ET.hog_rider[self.level_troop]) * \
				int(self.quantity_troop)
			self.b2_var.set(self.total2)
		else:
			self.total2 = 0
			self.b2_var.set(self.total2)

	def valk_calc(self):
		self.ET = Dark_Elixer()
		self.level_troop = self.level_valk.get()
		self.quantity_troop = self.q3.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total3 = int(self.ET.valkyrie[self.level_troop]) * \
				int(self.quantity_troop)
			self.b3_var.set(self.total3)
		else:
			self.total3 = 0
			self.b3_var.set(self.total3)

	def golem_calc(self):
		self.ET = Dark_Elixer()
		self.level_troop = self.level_golem.get()
		self.quantity_troop = self.q4.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total4 = int(self.ET.golem[self.level_troop]) * \
				int(self.quantity_troop)
			self.b4_var.set(self.total4)
		else:
			self.total4 = 0
			self.b4_var.set(self.total4)

	def witch_calc(self):
		self.ET = Dark_Elixer()
		self.level_troop = self.level_witch.get()
		self.quantity_troop = self.q5.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total5 = int(self.ET.witch[self.level_troop]) * \
				int(self.quantity_troop)
			self.b5_var.set(self.total5)
		else:
			self.total5 = 0
			self.b5_var.set(self.total5)

	def total_calc(self):
		self.minion_calc()
		self.hog_calc()
		self.valk_calc()
		self.golem_calc()
		self.witch_calc()

		self.total = int(self.b1_var.get()) + int(self.b2_var.get()) + \
					int(self.b3_var.get()) + int(self.b4_var.get()) + \
					int(self.b5_var.get()) 
		self.total_var.set(self.total)