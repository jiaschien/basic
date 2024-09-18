class Myclass():
	
    def smeth():
	print('This is a static method')
    smeth = staticmethod(smeth)

    def cmeth():
	print('This is a class method', cls)
    cmeth = classmethod(cmeth)
