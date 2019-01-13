# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-09 21:47:08
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-13 21:27:54

import tkinter as tk

import src.__myglobal as myglobal



class Daily(object):
	def __init__(self, root, data):
		# get data
		self.__plan = data.get_daily()

		# frame
		self.__frame = tk.Frame(
			root,
			width=myglobal.DAILY["FRAME"]["WIDTH"],
			height=myglobal.DAILY["FRAME"]["HEIGHT"],
		)
		self.__frame.place(x=myglobal.DAILY["FRAME"]["X"], y=myglobal.DAILY["FRAME"]["Y"], anchor="nw")

		# title
		self.__label = tk.Label(
			self.__frame,
			width=myglobal.DAILY["LABEL"]["WIDTH"],
			height=myglobal.DAILY["LABEL"]["HEIGHT"],
			text="Daily Plan",
			font=myglobal.DAILY["LABEL"]["FONT"]
		)
		self.__label.grid(
			row=myglobal.DAILY["LABEL"]["ROW"],
			column=myglobal.DAILY["LABEL"]["COLUMN"],
			rowspan=myglobal.DAILY["LABEL"]["ROWSPAN"],
			columnspan=myglobal.DAILY["LABEL"]["COLUMNSPAN"],
			padx=5, pady=5
		)

		# plan entry
		self.__entry = tk.Entry(
			self.__frame,
			width=myglobal.DAILY["ENTRY"]["WIDTH"],
			font=myglobal.DAILY["ENTRY"]["FONT"]
		)
		self.__entry.grid(
			row=myglobal.DAILY["ENTRY"]["ROW"],
			column=myglobal.DAILY["ENTRY"]["COLUMN"],
			rowspan=myglobal.DAILY["ENTRY"]["ROWSPAN"],
			columnspan=myglobal.DAILY["ENTRY"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# plan list
		self.__list = tk.Listbox(
			self.__frame,
			width=myglobal.DAILY["LIST"]["WIDTH"],
			height=myglobal.DAILY["LIST"]["HEIGHT"],
			font=myglobal.DAILY["LIST"]["FONT"]
		)
		self.__list.grid(
			row=myglobal.DAILY["LIST"]["ROW"],
			column=myglobal.DAILY["LIST"]["COLUMN"],
			rowspan=myglobal.DAILY["LIST"]["ROWSPAN"],
			columnspan=myglobal.DAILY["LIST"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# add button
		self.__add = tk.Button(
			self.__frame,
			width=myglobal.DAILY["ADD"]["WIDTH"],
			height=myglobal.DAILY["ADD"]["HEIGHT"],
			text="+",
			font=myglobal.DAILY["ADD"]["FONT"],
			command=lambda:self.__add_fun()
		)
		self.__add.grid(
			row=myglobal.DAILY["ADD"]["ROW"],
			column=myglobal.DAILY["ADD"]["COLUMN"],
			rowspan=myglobal.DAILY["ADD"]["ROWSPAN"],
			columnspan=myglobal.DAILY["ADD"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# del button
		self.__del =  tk.Button(
			self.__frame,
			width=myglobal.DAILY["DEL"]["WIDTH"],
			height=myglobal.DAILY["DEL"]["HEIGHT"],
			text="-",
			font=myglobal.DAILY["DEL"]["FONT"],
			command=lambda:self.__del_fun()
		)
		self.__del.grid(
			row=myglobal.DAILY["DEL"]["ROW"],
			column=myglobal.DAILY["DEL"]["COLUMN"],
			rowspan=myglobal.DAILY["DEL"]["ROWSPAN"],
			columnspan=myglobal.DAILY["DEL"]["COLUMNSPAN"],
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