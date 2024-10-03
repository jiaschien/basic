# coding=UTF-8

class Robot:
    # 表示……

	# 一个类变量，用来计数机器人的数量
	population = 0

	def __init__(self, name):
	    # 初始化数据
		self.name = name
		print('(Initializing {})'.format(self.name))

		# 当有人被创建时，机器人
		# 将会增加人口数量
		Robot.population += 1

	def die(self):
	    ''' 我挂了。'''
		print('{} is being destroyed'.format(self.name))

		Robot.population -= 1


