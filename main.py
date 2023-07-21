from tkinter import *
import math, re
from logic import Calculation

π = math.pi
e = math.e


FONT=14
button_digits={"bd":"5","bg":"#BBB","fg":"#000","height":2, "width":7, "font":('Arial', FONT, 'bold')}
button_special = {"bd":"5","bg":"#3C3636","fg":"#BBB","height":2, "width":7, "font":('Arial', FONT, 'bold')}


class Calculator:
	def __init__(self):
		# Creates a Window for the calculator and initializes many things that are needed to run the calc aap
		self.window = Tk()
		self.height =580
		self.width = 570
		# self.window.geometry(f"{self.height}x{self.width}")
		# self.main_frame=Frame(self.window, width=400, height=400, bg="black")
		# self.main_frame.grid(row=0, column=0, padx=10, pady=5)
		self.window.resizable(0,0)
		self.window.title("Calculator")
		self.window.config(bg="black")
		self.buttons()
		self.textarea_func()
		self.to_eval = ""

	def textarea_func(self):
		self.textarea=Text(self.window,height="3", width="27",font=("Arial", 25, "bold"))
		self.textarea.tag_configure("right",justify='right')
		self.textarea.tag_add("center", 1.0, "end")
		self.textarea.grid(row=1,columnspan=self.width)

	def calcuating_func(self,n):
			self.to_eval = "" if self.textarea.get(1.0, "end-1c") is None else self.textarea.get(1.0, "end-1c")
			self.to_eval+=(n)
			self.textarea.delete(1.0, "end")
			self.textarea.insert(1.0,self.to_eval)
	def buttons(self):
		# When using the Command parm don't call the function with () just the name would do, and if you wanna use pass some arguments then use lambda
		btn_del= Button(self.window, {"bd":5,"height":2, "width":7}, text="DEL", bg="red" ,font=("Arial", FONT, "bold"),command= lambda:self.delete())
		btn_del.grid(row=5, column=4)

		btn_equals = Button(self.window,{"bd":5,"height":2, "width":7},text="=", command=lambda:self.onequals(self.textarea.get(1.0, "end-1c")), bg="lightgreen" ,font=("Arial", FONT, "bold"))
		btn_equals.grid(row=5, column=5)

		btn_lbracket = Button(self.window,button_special,text="(", command=lambda: self.calcuating_func("("))
		btn_lbracket.grid(row=2, column=2)

		btn_lbracket = Button(self.window,button_special,text=")", command=lambda: self.calcuating_func(")"))
		btn_lbracket.grid(row=2, column=3)

		btn_sin = Button(self.window,button_special,text="sin", command=lambda: self.bracket_fun("sin"))
		btn_sin.grid(row=3, column=1)

		btn_cos = Button(self.window,button_special,text="cos", command=lambda: self.bracket_fun("cos"))
		btn_cos.grid(row=3, column=2)

		btn_tan = Button(self.window,button_special,text="tan", command=lambda: self.bracket_fun("tan"))
		btn_tan.grid(row=3, column=3)

		btn_cot = Button(self.window,button_special,text="cot", command=lambda: self.bracket_fun("cot"))
		btn_cot.grid(row=3, column=4)


		btn_9 = Button(self.window,button_digits,text="9", command=lambda: self.calcuating_func("9"))
		btn_9.grid(row=5, column=3)

		btn_8 = Button(self.window,button_digits,text="8", command=lambda: self.calcuating_func("8"))
		btn_8.grid(row=5, column=2)

		btn_7 = Button(self.window,button_digits,text="7", command=lambda: self.calcuating_func("7"))
		btn_7.grid(row=5, column=1)

		btn_6 = Button(self.window,button_digits,text="6", command=lambda: self.calcuating_func("6"))
		btn_6.grid(row=6, column=3)

		btn_5 = Button(self.window,button_digits,text="5", command=lambda: self.calcuating_func("5"))
		btn_5.grid(row=6, column=2)

		btn_4 = Button(self.window,button_digits,text="4", command=lambda: self.calcuating_func("4"))
		btn_4.grid(row=6, column=1)

		btn_3 = Button(self.window,button_digits,text="3", command=lambda: self.calcuating_func("3"))
		btn_3.grid(row=7, column=3)

		btn_2 = Button(self.window,button_digits,text="2", command=lambda: self.calcuating_func("2"))
		btn_2.grid(row=7, column=2)

		btn_1 = Button(self.window,button_digits,text="1", command=lambda: self.calcuating_func("1"))
		btn_1.grid(row=7, column=1)

		btn_0 = Button(self.window,button_digits,text="0", command=lambda: self.calcuating_func("0"))
		btn_0.grid(row=8, column=1)

		btn_point = Button(self.window,button_digits,text=".", command=lambda: self.calcuating_func(".")) 
		btn_point.grid(row=8, column=2)

		btn_percentage = Button(self.window,button_digits,text="%", command=lambda: self.bracket_fun("%")) 
		btn_percentage.grid(row=8, column=3)

		btn_plus = Button(self.window,button_digits,text="+", command=lambda: self.calcuating_func("+")) 
		btn_plus.grid(row=8, column=5)

		btn_minus = Button(self.window,button_digits,text="-", command=lambda: self.calcuating_func("-")) 
		btn_minus.grid(row=8, column=4)



		btn_multiply = Button(self.window,button_digits,text="*", command=lambda: self.calcuating_func("*")) 
		btn_multiply.grid(row=7, column=4)

		btn_divide = Button(self.window,button_digits,text="/", command=lambda: self.calcuating_func("/")) 
		btn_divide.grid(row=7, column=5)

		btn_modulus = Button(self.window,button_special,text="mod", command=lambda: self.bracket_fun("mod")) 
		btn_modulus.grid(row=2, column=4)

		btn_factorial = Button(self.window,button_special,text="x!", command=lambda: self.bracket_fun("x!")) 
		btn_factorial.grid(row=2, column=5)

		btn_pi = Button(self.window,button_special,text="π", command=lambda: self.calcuating_func("π")) 
		btn_pi.grid(row=2, column=1)

		btn_uroot = Button(self.window,button_special,text="√x", command=lambda: self.bracket_fun("√")) 
		btn_uroot.grid(row=3, column=5)


		btn_square = Button(self.window, button_digits, text="x\u00B2", command=lambda: self.bracket_fun("sq"))
		btn_square.grid(row=6, column=5)		

		btn_ypower = Button(self.window, button_digits, text="x\u02B8", command=lambda: self.bracket_fun("ypower"))
		btn_ypower.grid(row=6, column=4)

		btn_log = Button(self.window, button_special, text="log\u2091", command=lambda: self.calcuating_func("log[e]<>"))
		btn_log.grid(row=4, column=1)

		btn_log2 = Button(self.window, button_special, text="log\u2093y", command=lambda: self.bracket_fun("log"))
		btn_log2.grid(row=4, column=2)

		btn_10power = Button(self.window, button_special, text="10^x", command=lambda: self.bracket_fun("10x"))
		btn_10power.grid(row=4, column=3)

		btn_ex = Button(self.window, button_special, text="e^x", command=lambda: self.bracket_fun("ex"))
		btn_ex.grid(row=4, column=4)

		btn_e = Button(self.window, button_special, text="e", command=lambda: self.calcuating_func("e"))
		btn_e.grid(row=4, column=5)


	def onequals(self, string):
		self.result = Calculation(string).result()
		self.textarea.delete(1.0, "end")
		self.textarea.insert(1.0,f"{string} = {self.result}")		

	def delete(self):
		self.textarea.delete(1.0, "end")


	def bracket_fun(self, _type):

		text = self.textarea.get(1.0, "end-1c")
		self.textarea.delete(1.0, "end")

		if _type == "log":
			self.textarea.insert(1.0,f"{text}{_type}[]<>")
			return
		if _type == "x!":
			self.textarea.insert(1.0,f"{text}<>!")
			return
		if _type == "%":
			self.textarea.insert(1.0, f"{text}/100")
			return
		if _type == "mod":
			self.textarea.insert(1.0, f"{text}%")
			return
		if _type in ["10x", "ex"]:
			self.textarea.insert(1.0,f"{text}{_type[:-1]}^<>")
			return
		if _type == "ypower":
			self.textarea.insert(1.0, f"{text}x^<y>")
			return
		if _type == "sq":
			self.textarea.insert(1.0, f"{text}x^<2>")
			return

		self.textarea.insert(1.0,f"{text}{_type}<>")



	def start(self):
		self.window.mainloop()

if __name__ == "__main__":
	app = Calculator()
	app.start()

