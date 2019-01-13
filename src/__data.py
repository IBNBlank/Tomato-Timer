# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-01-09 21:46:31
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-13 21:03:27

import json

import src.__myglobal as myglobal



class Data(object):
	def __init__(self):
		try:
			with open(myglobal.DATA["FILEPATH"], "r") as load_f:
				data = json.load(load_f)
			self.__time = data["time"]
			self.__daily = data["daily"]
			self.__weekly = data["weekly"]
		except:
			self.__time = [25, 5]
			self.__daily = ["None"]
			self.__weekly = ["None"]


	def get_time(self):
		return self.__time


	def get_daily(self):
		return self.__daily


	def get_weekly(self):
		return self.__weekly


	def save(self, root, clock, daily, weekly):
		with open(myglobal.DATA["FILEPATH"], "w") as load_f:
			data = {
				"time": clock.get_time(),
				"daily": daily.get_plan(),
				"weekly": weekly.get_plan()
			}
			json.dump(data, load_f)

		root.quit()