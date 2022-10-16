import math,re
π = math.pi
e = math.e

class Calculation:

	def __init__(self, given):
		self.given = given.replace(" ", "")
		self.main()

	def main(self):
		self.given_list = [i for i in self.given ]

		if "!" in self.given_list:
			self.sub_factorial()

		if "√" in self.given_list:
			self.sub_uroot()

		if "^" in self.given_list:
			# Note here so i use this func for x^y in future too
			self.power()


		if "l" in self.given_list:
			self.log()

		# do the same for sin cos values too
		c_list= ["s", "c", "t"]
		if any((True for x in c_list if x in self.given_list )):
			regex = "[a-zA-Z]+<\d+>"
			match = re.finditer(regex, self.given)
			for m in match:
				functions = re.findall("[a-zA-Z]+", m.group())
				values = re.findall("<\d+>", m.group())
				for i,j in enumerate(functions):
					val = f"{values[i].replace('<', '').replace('>', '')}"
					val = math.radians(int(val))
					to_replace=f'math.{j}({val})'
					if j == "cot":
						to_replace=f'math.tan(1/{val})' 
					self.given = re.sub(regex,to_replace,self.given,count=1)

		
	def sub_factorial(self):
		regex = "\d+!"
		match = re.finditer(regex, self.given)
		for m in match:
			to_replace=f'math.factorial({m.group().replace("!", "")})'	
			self.given = re.sub(regex,to_replace,self.given,count=1)

	def sub_uroot(self):
		regex = "√<\d+>"
		match = re.finditer(regex, self.given)
		for m in match:
			digit = re.findall("\d+", m.group())[0]
			to_replace = f'math.sqrt({digit})'
			self.given = re.sub(regex,to_replace,self.given,count=1)

	def power(self):
		regex = "\d+\^<\d+>"
		match = re.finditer(regex, self.given)
		for m in match:
			digits = re.findall("\d+", m.group())
			to_replace = f'math.pow({digits[0]}, {digits[1]})'
			self.given = re.sub(regex,to_replace,self.given,count=1)
		check_e = re.finditer("e\^<\d+>", self.given)
		if check_e:
			for m in check_e:
				digit = re.findall("\d+", m.group())[0]
				to_replace = f'math.pow(e, {digit})'
				self.given = re.sub("e\^<\d+>", to_replace,self.given, count=1)
	def log(self):
		regex = "log\[\d+]<\d+>"
		match = re.finditer(regex, self.given)
		for m in match:
			numbers = re.findall("\d+", m.group())
			x = numbers[0]
			y = numbers[1]
			to_replace = f'math.log({x},{y})'
			self.given = re.sub(regex,to_replace,self.given,count=1)

	def result(self):
		return eval(self.given)

# Calculation("5^<20>+10^<5>")
# Calculation("e^<5>+log[10]<5>+e+π+1+5+(96+36)*sin<23>+5!+(50+9)+6*10^<6>-√<4>*(5+3)+tan<50>+cos<60>")
# Calculation("√<4> + 5 ")

