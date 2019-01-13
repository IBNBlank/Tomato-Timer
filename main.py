# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-09 00:09:05
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-13 21:04:22

import tkinter as tk

import src.__data as data
import src.__clock as clock
import src.__daily as daily
import src.__weekly as weekly
import src.__myglobal as myglobal

if __name__ == '__main__':
	###### Initial #####
	### data initial ###
	instantiated_data = data.Data()


	### GUI initial ###
	# window body
	root = tk.Tk()
	root.title(myglobal.BODY["TITLE"])
	root.geometry(myglobal.BODY["SIZE"])
	# clock initial
	instantiated_clock = clock.Clock(root, instantiated_data)
	# daily initial
	instantiated_daily = daily.Daily(root, instantiated_data)
	# weekly initial
	instantiated_weekly = weekly.Weekly(root, instantiated_data)


	### event initial ###
	# close event
	root.protocol("WM_DELETE_WINDOW", lambda:instantiated_data.save(root,
		instantiated_clock, instantiated_daily, instantiated_weekly))



	##### Mainloop #####
	root.mainloop()