# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-09 21:46:51
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-13 22:55:13

import tkinter as tk
import time
import threading
import winsound

import src.__myglobal as myglobal



class Clock(object):
	def __init__(self, root, data):
		# get data
		self.__time = data.get_time()

		# frame
		self.__frame = tk.Frame(
			root,
			width=myglobal.CLOCK["FRAME"]["WIDTH"],
			height=myglobal.CLOCK["FRAME"]["HEIGHT"],
		)
		self.__frame.place(x=myglobal.CLOCK["FRAME"]["X"], y=myglobal.CLOCK["FRAME"]["Y"], anchor="nw")

		# title
		self.__label = tk.Label(
			self.__frame,
			width=myglobal.CLOCK["LABEL"]["WIDTH"],
			height=myglobal.CLOCK["LABEL"]["HEIGHT"],
			text="Tomato Clock",
			font=myglobal.CLOCK["LABEL"]["FONT"]
		)
		self.__label.grid(
			row=myglobal.CLOCK["LABEL"]["ROW"],
			column=myglobal.CLOCK["LABEL"]["COLUMN"],
			rowspan=myglobal.CLOCK["LABEL"]["ROWSPAN"],
			columnspan=myglobal.CLOCK["LABEL"]["COLUMNSPAN"],
			padx=5, pady=5
		)

		# tomato label
		self.__tomato_string = tk.StringVar()
		self.__tomato_label = tk.Label(
			self.__frame,
			width=myglobal.CLOCK["TOMATO_LABEL"]["WIDTH"],
			height=myglobal.CLOCK["TOMATO_LABEL"]["HEIGHT"],
			textvariable=self.__tomato_string,
			font=myglobal.CLOCK["TOMATO_LABEL"]["FONT"]
		)
		self.__tomato_label.grid(
			row=myglobal.CLOCK["TOMATO_LABEL"]["ROW"],
			column=myglobal.CLOCK["TOMATO_LABEL"]["COLUMN"],
			rowspan=myglobal.CLOCK["TOMATO_LABEL"]["ROWSPAN"],
			columnspan=myglobal.CLOCK["TOMATO_LABEL"]["COLUMNSPAN"],
			padx=5, pady=5
		)

		# rest label
		self.__rest_string = tk.StringVar()
		self.__rest_label = tk.Label(
			self.__frame,
			width=myglobal.CLOCK["REST_LABEL"]["WIDTH"],
			height=myglobal.CLOCK["REST_LABEL"]["HEIGHT"],
			textvariable=self.__rest_string,
			font=myglobal.CLOCK["REST_LABEL"]["FONT"]
		)
		self.__rest_label.grid(
			row=myglobal.CLOCK["REST_LABEL"]["ROW"],
			column=myglobal.CLOCK["REST_LABEL"]["COLUMN"],
			rowspan=myglobal.CLOCK["REST_LABEL"]["ROWSPAN"],
			columnspan=myglobal.CLOCK["REST_LABEL"]["COLUMNSPAN"],
			padx=5, pady=5
		)

		# tomato entry
		self.__tomato_entry = tk.Entry(
			self.__frame,
			width=myglobal.CLOCK["TOMATO_ENTRY"]["WIDTH"],
			font=myglobal.CLOCK["TOMATO_ENTRY"]["FONT"]
		)
		self.__tomato_entry.grid(
			row=myglobal.CLOCK["TOMATO_ENTRY"]["ROW"],
			column=myglobal.CLOCK["TOMATO_ENTRY"]["COLUMN"],
			rowspan=myglobal.CLOCK["TOMATO_ENTRY"]["ROWSPAN"],
			columnspan=myglobal.CLOCK["TOMATO_ENTRY"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# rest entry
		self.__rest_entry = tk.Entry(
			self.__frame,
			width=myglobal.CLOCK["REST_ENTRY"]["WIDTH"],
			font=myglobal.CLOCK["REST_ENTRY"]["FONT"]
		)
		self.__rest_entry.grid(
			row=myglobal.CLOCK["REST_ENTRY"]["ROW"],
			column=myglobal.CLOCK["REST_ENTRY"]["COLUMN"],
			rowspan=myglobal.CLOCK["REST_ENTRY"]["ROWSPAN"],
			columnspan=myglobal.CLOCK["REST_ENTRY"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# tomato button
		self.__tomato_button = tk.Button(
			self.__frame,
			width=myglobal.CLOCK["TOMATO_BUTTON"]["WIDTH"],
			height=myglobal.CLOCK["TOMATO_BUTTON"]["HEIGHT"],
			text="tomato",
			font=myglobal.CLOCK["TOMATO_BUTTON"]["FONT"],
			command=lambda:self.__tomato_fun()
		)
		self.__tomato_button.grid(
			row=myglobal.CLOCK["TOMATO_BUTTON"]["ROW"],
			column=myglobal.CLOCK["TOMATO_BUTTON"]["COLUMN"],
			rowspan=myglobal.CLOCK["TOMATO_BUTTON"]["ROWSPAN"],
			columnspan=myglobal.CLOCK["TOMATO_BUTTON"]["COLUMNSPAN"],
			padx=10, pady=10
		)

		# rest button
		self.__rest_button = tk.Button(
			self.__frame,
			width=myglobal.CLOCK["REST_BUTTON"]["WIDTH"],
			height=myglobal.CLOCK["REST_BUTTON"]["HEIGHT"],
			text="rest",
			font=myglobal.CLOCK["REST_BUTTON"]["FONT"],
			command=lambda:self.__rest_fun()
		)
		self.__rest_button.grid(
			row=myglobal.CLOCK["REST_BUTTON"]["ROW"],
			column=myglobal.CLOCK["REST_BUTTON"]["COLUMN"],
			rowspan=myglobal.CLOCK["REST_BUTTON"]["ROWSPAN"],
			columnspan=myglobal.CLOCK["REST_BUTTON"]["COLUMNSPAN"],
			padx=10, pady=10
		)

		# clock label
		self.__time_string = tk.StringVar()
		self.__clock_label = tk.Label(
			self.__frame,
			width=myglobal.CLOCK["CLOCK_LABEL"]["WIDTH"],
			height=myglobal.CLOCK["CLOCK_LABEL"]["HEIGHT"],
			textvariable=self.__time_string,
			font=myglobal.CLOCK["CLOCK_LABEL"]["FONT"]
		)
		self.__clock_label.grid(
			row=myglobal.CLOCK["CLOCK_LABEL"]["ROW"],
			column=myglobal.CLOCK["CLOCK_LABEL"]["COLUMN"],
			rowspan=myglobal.CLOCK["CLOCK_LABEL"]["ROWSPAN"],
			columnspan=myglobal.CLOCK["CLOCK_LABEL"]["COLUMNSPAN"],
			padx=5, pady=25
		)

		# start button
		self.__start_button = tk.Button(
			self.__frame,
			width=myglobal.CLOCK["START_BUTTON"]["WIDTH"],
			height=myglobal.CLOCK["START_BUTTON"]["HEIGHT"],
			text="start",
			font=myglobal.CLOCK["START_BUTTON"]["FONT"],
			command=lambda:self.__start_fun()
		)
		self.__start_button.grid(
			row=myglobal.CLOCK["START_BUTTON"]["ROW"],
			column=myglobal.CLOCK["START_BUTTON"]["COLUMN"],
			rowspan=myglobal.CLOCK["START_BUTTON"]["ROWSPAN"],
			columnspan=myglobal.CLOCK["START_BUTTON"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# stop button
		self.__stop_button = tk.Button(
			self.__frame,
			width=myglobal.CLOCK["STOP_BUTTON"]["WIDTH"],
			height=myglobal.CLOCK["STOP_BUTTON"]["HEIGHT"],
			text="stop",
			font=myglobal.CLOCK["STOP_BUTTON"]["FONT"],
			command=lambda:self.__stop_fun()
		)
		self.__stop_button.grid(
			row=myglobal.CLOCK["STOP_BUTTON"]["ROW"],
			column=myglobal.CLOCK["STOP_BUTTON"]["COLUMN"],
			rowspan=myglobal.CLOCK["STOP_BUTTON"]["ROWSPAN"],
			columnspan=myglobal.CLOCK["STOP_BUTTON"]["COLUMNSPAN"],
			padx=5, pady=10
		)

		# show time
		self.__update_time()
		self.__set_time()

		# count flag
		self.__count_flag = False


	def __update_time(self):
		tomato = str(self.__time[0]).zfill(2)
		rest = str(self.__time[1]).zfill(2)

		self.__tomato_string.set("Tomato:{}".format(tomato))
		self.__rest_string.set("    Rest:{}".format(rest))


	def __tomato_fun(self):
		if not self.__count_flag:
			string = self.__tomato_entry.get()

			if string.isdigit():
				tomato = int(string)
				if tomato <= 0:
					tomato = 1
				elif tomato > 60:
					tomato = 60
				self.__time[0] = tomato
				self.__update_time()


	def __rest_fun(self):
		if not self.__count_flag:
			string = self.__rest_entry.get()

			if string.isdigit():
				rest = int(string)
				if rest <= 0:
					rest = 1
				elif rest > 60:
					rest = 60
				self.__time[1] = rest
				self.__update_time()


	def __set_time(self, sec=0):
		minute = str(sec // 60).zfill(2)
		second = str(sec %  60).zfill(2)

		self.__time_string.set("{0}:{1}".format(minute, second))


	def __clock(self):
		tomato_count = 60 * self.__time[0]
		rest_count = 60 * self.__time[1]

		while self.__count_flag:
			# tomato
			for i in range(tomato_count):
				if self.__count_flag:
					self.__set_time(i)
					time.sleep(1)
				else:
					break
			if self.__count_flag:
				winsound.PlaySound(myglobal.CLOCK["MUSIC"]["TOMATO"], winsound.SND_FILENAME)
			# rest
			for i in range(rest_count):
				if self.__count_flag:
					self.__set_time(i)
					time.sleep(1)
				else:
					break
			if self.__count_flag:
				winsound.PlaySound(myglobal.CLOCK["MUSIC"]["REST"], winsound.SND_FILENAME)

		self.__set_time()


	def __start_fun(self):
		self.__count_flag = True

		clock_thread = threading.Thread(target=lambda:self.__clock())
		clock_thread.start()


	def __stop_fun(self):
		self.__count_flag = False


	def get_time(self):
		return self.__time