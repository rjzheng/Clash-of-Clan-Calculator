from Elixer import *
import Tkinter as tk
from Tkinter import *
import ttk
from ttk import *

class Elixer_GUI():
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

		self.calculate_label = ttk.Label(self.parent, text = 'Total Elixer:')
		self.calculate_label.grid(row = 16, column = 0)
		self.total_var = StringVar()
		self.total_var.set("Calculate")
		self.calculate_entry = ttk.Button(self.parent, \
							textvariable = self.total_var, \
							command = self.total_calc)
		self.calculate_entry.grid(row = 16, column = 3)

		self.barbarian = ttk.Label(self.parent, text = "Barbarian:")
		self.barbarian.grid(row = 1, column = 0)
		self.archer = ttk.Label(self.parent, text = "Archer:")
		self.archer.grid(row = 2, column = 0)
		self.goblin = ttk.Label(self.parent, text = "Goblin:")
		self.goblin.grid(row = 3, column = 0)
		self.giant = ttk.Label(self.parent, text = "Giant:")
		self.giant.grid(row = 4, column = 0)
		self.wall_breaker = ttk.Label(self.parent, text = "Wall Breaker:")
		self.wall_breaker.grid(row = 5, column = 0)
		self.balloon = ttk.Label(self.parent, text = "Balloon:")
		self.balloon.grid(row = 6, column = 0)
		self.wizard = ttk.Label(self.parent, text = "Wizard:")
		self.wizard.grid(row = 7, column = 0)
		self.healer = ttk.Label(self.parent, text = "Healer:")
		self.healer.grid(row = 8, column = 0)
		self.dragon = ttk.Label(self.parent, text = "Dragon:")
		self.dragon.grid(row = 9, column = 0)
		self.pekka = ttk.Label(self.parent, text = "P.E.K.K.A:")
		self.pekka.grid(row = 10, column = 0)

		self.lightning = ttk.Label(self.parent, text = "Lightning Spell:")
		self.lightning.grid(row = 11, column = 0)
		self.healing = ttk.Label(self.parent, text = "Healing Spell:")
		self.healing.grid(row = 12, column = 0)
		self.rage = ttk.Label(self.parent, text = "Rage Spell:")
		self.rage.grid(row = 13, column = 0)
		self.jump = ttk.Label(self.parent, text = "Jump Spell:")
		self.jump.grid(row = 14, column = 0)
		self.freeze = ttk.Label(self.parent, text = "Freeze Spell:")
		self.freeze.grid(row = 15, column = 0)

		self.level_barb = ttk.Combobox(self.parent)
		self.level_barb['values'] = ('1', '2', '3', '4', '5', '6')
		self.level_barb.grid(row = 1, column = 1)
		self.level_archer = ttk.Combobox(self.parent)
		self.level_archer['values'] = ('1', '2', '3', '4', '5', '6')
		self.level_archer.grid(row = 2, column = 1)
		self.level_goblin = ttk.Combobox(self.parent)
		self.level_goblin['values'] = ('1', '2', '3', '4', '5', '6')
		self.level_goblin.grid(row = 3, column = 1)
		self.level_giant = ttk.Combobox(self.parent)
		self.level_giant['values'] = ('1', '2', '3', '4', '5', '6')
		self.level_giant.grid(row = 4, column = 1)
		self.level_wb = ttk.Combobox(self.parent)
		self.level_wb['values'] = ('1', '2', '3', '4', '5', '6')
		self.level_wb.grid(row = 5, column = 1)
		self.level_balloon = ttk.Combobox(self.parent)
		self.level_balloon['values'] = ('1', '2', '3', '4', '5', '6')
		self.level_balloon.grid(row = 6, column = 1)
		self.level_wiz = ttk.Combobox(self.parent)
		self.level_wiz['values'] = ('1', '2', '3', '4', '5', '6')
		self.level_wiz.grid(row = 7, column = 1)
		self.level_healer = ttk.Combobox(self.parent)
		self.level_healer['values'] = ('1', '2', '3', '4')
		self.level_healer.grid(row = 8, column = 1)
		self.level_drag = ttk.Combobox(self.parent)
		self.level_drag['values'] = ('1', '2', '3', '4')
		self.level_drag.grid(row = 9, column = 1)
		self.level_pekka = ttk.Combobox(self.parent)
		self.level_pekka['values'] = ('1', '2', '3', '4', '5')
		self.level_pekka.grid(row = 10, column = 1)
		self.level_light = ttk.Combobox(self.parent)
		self.level_light['values'] = ('1', '2', '3', '4', '5', '6')
		self.level_light.grid(row = 11, column = 1)
		self.level_heal = ttk.Combobox(self.parent)
		self.level_heal['values'] = ('1', '2', '3', '4', '5', '6')
		self.level_heal.grid(row = 12, column = 1)
		self.level_rage = ttk.Combobox(self.parent)
		self.level_rage['values'] = ('1', '2', '3', '4', '5')
		self.level_rage.grid(row = 13, column = 1)
		self.level_jump = ttk.Combobox(self.parent)
		self.level_jump['values'] = ('1', '2', '3')
		self.level_jump.grid(row = 14, column = 1)
		self.level_freeze = ttk.Combobox(self.parent)
		self.level_freeze['values'] = ('1', '2', '3', '4', '5')
		self.level_freeze.grid(row = 15, column = 1)

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
		self.q6 = ttk.Entry(self.parent)
		self.q6.grid(row = 6, column = 2)
		self.q7 = ttk.Entry(self.parent)
		self.q7.grid(row = 7, column = 2)
		self.q8 = ttk.Entry(self.parent)
		self.q8.grid(row = 8, column = 2)
		self.q9 = ttk.Entry(self.parent)
		self.q9.grid(row = 9, column = 2)
		self.q10 = ttk.Entry(self.parent)
		self.q10.grid(row = 10, column = 2)
		self.q11 = ttk.Entry(self.parent)
		self.q11.grid(row = 11, column = 2)
		self.q12 = ttk.Entry(self.parent)
		self.q12.grid(row = 12, column = 2)
		self.q13 = ttk.Entry(self.parent)
		self.q13.grid(row = 13, column = 2)
		self.q14 = ttk.Entry(self.parent)
		self.q14.grid(row = 14, column = 2)
		self.q15 = ttk.Entry(self.parent)
		self.q15.grid(row = 15, column = 2)

		self.b1_var = StringVar()
		self.b1_var.set(0)
		self.b1 = ttk.Button(self.parent, textvariable = self.b1_var, \
				command = self.barbarian_calc)
		self.b1.grid(row = 1, column = 3)
		self.b2_var = StringVar()
		self.b2_var.set(0)
		self.b2 = ttk.Button(self.parent, textvariable = self.b2_var, \
				command = self.archer_calc)
		self.b2.grid(row = 2, column = 3)
		self.b3_var = StringVar()
		self.b3_var.set(0)
		self.b3 = ttk.Button(self.parent, textvariable = self.b3_var, \
				command = self.goblin_calc)
		self.b3.grid(row = 3, column = 3)
		self.b4_var = StringVar()
		self.b4_var.set(0)
		self.b4 = ttk.Button(self.parent, textvariable = self.b4_var, \
				command = self.giant_calc)
		self.b4.grid(row = 4, column = 3)
		self.b5_var = StringVar()
		self.b5_var.set(0)
		self.b5 = ttk.Button(self.parent, textvariable = self.b5_var, \
				command = self.wb_calc)
		self.b5.grid(row = 5, column = 3)
		self.b6_var = StringVar()
		self.b6_var.set(0)
		self.b6 = ttk.Button(self.parent, textvariable = self.b6_var, \
				command = self.balloon_calc)
		self.b6.grid(row = 6, column = 3)
		self.b7_var = StringVar()
		self.b7_var.set(0)
		self.b7 = ttk.Button(self.parent, textvariable = self.b7_var, \
				command = self.wiz_calc)
		self.b7.grid(row = 7, column = 3)
		self.b8_var = StringVar()
		self.b8_var.set(0)
		self.b8 = ttk.Button(self.parent, textvariable = self.b8_var, \
				command = self.healer_calc)
		self.b8.grid(row = 8, column = 3)
		self.b9_var = StringVar()
		self.b9_var.set(0)
		self.b9 = ttk.Button(self.parent, textvariable = self.b9_var, \
				command = self.dragon_calc)
		self.b9.grid(row = 9, column = 3)
		self.b10_var = StringVar()
		self.b10_var.set(0)
		self.b10 = ttk.Button(self.parent, textvariable = self.b10_var, \
				command = self.pekka_calc)
		self.b10.grid(row = 10, column = 3)
		self.b11_var = StringVar()
		self.b11_var.set(0)
		self.b11 = ttk.Button(self.parent, textvariable = self.b11_var, \
				command = self.light_calc)
		self.b11.grid(row = 11, column = 3)
		self.b12_var = StringVar()
		self.b12_var.set(0)
		self.b12 = ttk.Button(self.parent, textvariable = self.b12_var, \
				command = self.heal_calc)
		self.b12.grid(row = 12, column = 3)
		self.b13_var = StringVar()
		self.b13_var.set(0)
		self.b13 = ttk.Button(self.parent, textvariable = self.b13_var, \
				command = self.rage_calc)
		self.b13.grid(row = 13, column = 3)
		self.b14_var = StringVar()
		self.b14_var.set(0)
		self.b14 = ttk.Button(self.parent, textvariable = self.b14_var, \
				command = self.jump_calc)
		self.b14.grid(row = 14, column = 3)
		self.b15_var = StringVar()
		self.b15_var.set(0)
		self.b15 = ttk.Button(self.parent, textvariable = self.b15_var, \
				command = self.freeze_calc)
		self.b15.grid(row = 15, column = 3)

	def barbarian_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_barb.get()
		self.quantity_troop = self.q1.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total1 = int(self.ET.barbarian[self.level_troop]) * \
					int(self.quantity_troop)
			self.b1_var.set(self.total1)
		else:
			self.total1 = 0
			self.b1_var.set(self.total1)

	def archer_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_archer.get()
		self.quantity_troop = self.q2.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total2 = int(self.ET.archer[self.level_troop]) * \
				int(self.quantity_troop)
			self.b2_var.set(self.total2)
		else:
			self.total2 = 0
			self.b2_var.set(self.total2)

	def goblin_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_goblin.get()
		self.quantity_troop = self.q3.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total3 = int(self.ET.goblin[self.level_troop]) * \
				int(self.quantity_troop)
			self.b3_var.set(self.total3)
		else:
			self.total3 = 0
			self.b3_var.set(self.total3)

	def giant_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_giant.get()
		self.quantity_troop = self.q4.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total4 = int(self.ET.giant[self.level_troop]) * \
				int(self.quantity_troop)
			self.b4_var.set(self.total4)
		else:
			self.total4 = 0
			self.b4_var.set(self.total4)

	def wb_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_wb.get()
		self.quantity_troop = self.q5.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total5 = int(self.ET.wall_breaker[self.level_troop]) * \
				int(self.quantity_troop)
			self.b5_var.set(self.total5)
		else:
			self.total5 = 0
			self.b5_var.set(self.total5)

	def balloon_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_balloon.get()
		self.quantity_troop = self.q6.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total6 = int(self.ET.balloon[self.level_troop]) * \
				int(self.quantity_troop)
			self.b6_var.set(self.total6)
		else:
			self.total6 = 0
			self.b6_var.set(self.total6)

	def wiz_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_wiz.get()
		self.quantity_troop = self.q7.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total7 = int(self.ET.wizard[self.level_troop]) * \
				int(self.quantity_troop)
			self.b7_var.set(self.total7)
		else:
			self.total7 = 0
			self.b7_var.set(self.total7)

	def healer_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_healer.get()
		self.quantity_troop = self.q8.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total8 = int(self.ET.healer[self.level_troop]) * \
				int(self.quantity_troop)
			self.b8_var.set(self.total8)
		else:
			self.total8 = 0
			self.b8_var.set(self.total8)

	def dragon_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_drag.get()
		self.quantity_troop = self.q9.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total9 = int(self.ET.dragon[self.level_troop]) * \
				int(self.quantity_troop)
			self.b9_var.set(self.total9)
		else:
			self.total9 = 0
			self.b9_var.set(self.total9)

	def pekka_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_pekka.get()
		self.quantity_troop = self.q10.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total10 = int(self.ET.pekka[self.level_troop]) * \
				int(self.quantity_troop)
			self.b10_var.set(self.total10)
		else:
			self.total10 = 0
			self.b10_var.set(self.total10)

	def light_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_light.get()
		self.quantity_troop = self.q11.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total11 = int(self.ET.lightning[self.level_troop]) * \
				int(self.quantity_troop)
			self.b11_var.set(self.total11)
		else:
			self.total11 = 0
			self.b11_var.set(self.total11)

	def heal_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_heal.get()
		self.quantity_troop = self.q12.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total12 = int(self.ET.healing[self.level_troop]) * \
				int(self.quantity_troop)
			self.b12_var.set(self.total12)
		else:
			self.total12 = 0
			self.b12_var.set(self.total12)

	def rage_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_rage.get()
		self.quantity_troop = self.q13.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total13 = int(self.ET.rage[self.level_troop]) * \
				int(self.quantity_troop)
			self.b13_var.set(self.total13)
		else:
			self.total13 = 0
			self.b13_var.set(self.total13)

	def jump_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_jump.get()
		self.quantity_troop = self.q14.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total14 = int(self.ET.jump[self.level_troop]) * \
				int(self.quantity_troop)
			self.b14_var.set(self.total14)
		else:
			self.total14 = 0
			self.b14_var.set(self.total14)

	def freeze_calc(self):
		self.ET = Elixer()
		self.level_troop = self.level_freeze.get()
		self.quantity_troop = self.q15.get()
		if self.level_troop != '' and self.quantity_troop != '':
			self.total15 = int(self.ET.freeze[self.level_troop]) * \
				int(self.quantity_troop)
			self.b15_var.set(self.total15)
		else:
			self.total15 = 0
			self.b15_var.set(self.total15)

	def total_calc(self):
		self.barbarian_calc()
		self.archer_calc()
		self.goblin_calc()
		self.giant_calc()
		self.wb_calc()
		self.balloon_calc()
		self.wiz_calc()
		self.healer_calc()
		self.dragon_calc()
		self.pekka_calc()
		self.light_calc()
		self.heal_calc()
		self.rage_calc()
		self.jump_calc()
		self.freeze_calc()
		self.total = int(self.b1_var.get()) + int(self.b2_var.get()) + \
					int(self.b3_var.get()) + int(self.b4_var.get()) + \
					int(self.b5_var.get()) + int(self.b6_var.get()) + \
					int(self.b7_var.get()) + int(self.b8_var.get()) + \
					int(self.b9_var.get()) + int(self.b10_var.get()) + \
					int(self.b11_var.get()) + int(self.b12_var.get()) + \
					int(self.b13_var.get()) + int(self.b14_var.get()) + \
					int(self.b15_var.get())
		self.total_var.set(self.total)