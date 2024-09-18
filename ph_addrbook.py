# 一个简单的数据库

# 一个将人名用作键的字典。每个人都用一个字典表示，
# 字典包含键'phone'和'addr'，他们分别于电话号码和地址相关联
people = {
    
	'alice':{
	    'phone': '2341',
		'addr': 'Foo drive 23'
	},

	'Beth':{
	    'phone': '9102',
		'addr': 'Bar street 42'
	},

	'Cecil': {
	    'phone': '3158',
		'addr': 'Baz avenue 90'
	}

}

# 电话号码和地址的描述性标签，供打印输出时使用
lebels = {
    'phone': 'phone number',
	'addr': 'address'
}

name = input('Name: ')

# 要查找电话号码还是地址？

