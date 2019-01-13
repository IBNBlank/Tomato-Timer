# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-09 21:47:42
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-13 21:30:58

import tkinter as tk

import src.__myglobal as myglobal



class Weekly(object):
	def __init__(self, root, data):
		# get data
		self.__plan = data.get_weekly()

		# frame
		self.__frame = tk.Frame(
			root,
			width=myglobal.WEEKLY["FRAME"]["WIDTH"],
			height=myglobal.WEEKLY["FRAME"]["HEIGHT"],
		)
		self.__frame.place(x=myglobal.WEEKLY["FRAME"]["X"], y=myglobal.WEEKLY["FRAME"]["Y"], anchor="nw")

		# title
		self.__label = tk.Label(
			self.__frame,
			width=myglobal.WEEKLY["LABEL"]["WIDTH"],
			height=myglobal.WEEKLY["LABEL"]["HEIGHT"],
			text="Weekly Plan",
			font=myglobal.WEEKLY["LABEL"]["FONT"]
		)
		self.__label.grid(
			row=myglobal.WEEKLY["LABEL"]["ROW"],
			column=myglobal.WEEKLY["LABEL"]["COLUMN"],
			rowspan=myglobal.WEEKLY["LABEL"]["ROWSPAN"],
			columnspan=myglobal.WEEKLY["LABEL"]["COLUMNSPAN"],
			padx=5, pady=5
		)

		# plan entry
		self.__entry = tk.Entry(
			self.__frame,
			width=myglobal.WEEKLY["ENTRY"]["WIDTH"],
			font=myglobal.WEEKLY["ENTRY"]["FONT"]
		)
		self.__entry.grid(
			row=myglobal.WEEKLY["ENTRY"]["ROW"],
			column=myglobal.WEEKLY["ENTRY"]["COLUMN"],
			rowspan=myglobal.WEEKLY["ENTRY"]["ROWSPAN"],
			columnspan=myglobal.WEEKLY["ENTRY"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# plan list
		self.__list = tk.Listbox(
			self.__frame,
			width=myglobal.WEEKLY["LIST"]["WIDTH"],
			height=myglobal.WEEKLY["LIST"]["HEIGHT"],
			font=myglobal.WEEKLY["LIST"]["FONT"]
		)
		self.__list.grid(
			row=myglobal.WEEKLY["LIST"]["ROW"],
			column=myglobal.WEEKLY["LIST"]["COLUMN"],
			rowspan=myglobal.WEEKLY["LIST"]["ROWSPAN"],
			columnspan=myglobal.WEEKLY["LIST"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# add button
		self.__add = tk.Button(
			self.__frame,
			width=myglobal.WEEKLY["ADD"]["WIDTH"],
			height=myglobal.WEEKLY["ADD"]["HEIGHT"],
			text="+",
			font=myglobal.WEEKLY["ADD"]["FONT"],
			command=lambda:self.__add_fun()
		)
		self.__add.grid(
			row=myglobal.WEEKLY["ADD"]["ROW"],
			column=myglobal.WEEKLY["ADD"]["COLUMN"],
			rowspan=myglobal.WEEKLY["ADD"]["ROWSPAN"],
			columnspan=myglobal.WEEKLY["ADD"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# del button
		self.__del =  tk.Button(
			self.__frame,
			width=myglobal.WEEKLY["DEL"]["WIDTH"],
			height=myglobal.WEEKLY["DEL"]["HEIGHT"],
			text="-",
			font=myglobal.WEEKLY["DEL"]["FONT"],
			command=lambda:self.__del_fun()
		)
		self.__del.grid(
			row=myglobal.WEEKLY["DEL"]["ROW"],
			column=myglobal.WEEKLY["DEL"]["COLUMN"],
			rowspan=myglobal.WEEKLY["DEL"]["ROWSPAN"],
			columnspan=myglobal.WEEKLY["DEL"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# update
		self.__update_list()


	def __update_list(self):
		# clear
		self.__list.delete(0, "end")

		# insert
		for item in self.__plan:
			self.__list.insert("end", item)


	def __add_fun(self):
		string = self.__entry.get()

		if string != '':
			while "None" in self.__plan:
				self.__plan.remove("None")
			self.__plan.append(string)
			self.__update_list()


	def __del_fun(self):
		try:
			index, = self.__list.curselection()
			del self.__plan[index]
			if not self.__plan:
				self.__plan.append("None")
			self.__update_list()
		except:
			pass


	def get_plan(self):
		return self.__plan