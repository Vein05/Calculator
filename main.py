from tkinter import * 

FONT=14
buttons_difgits={"bg":"orange","height":3, "width":26, "font":('Arial', FONT, 'bold')}

class Calculator:
	def __init__(self):
		# Creates a Window for the calculator and initializes many things that are needed to run the calc aap
		self.window = Tk()
		self.height = 560
		self.width = 560
		# self.window.geometry(f"{self.height}x{self.width}")
		# self.main_frame=Frame(self.window, width=400, height=400, bg="black")
		# self.main_frame.grid(row=0, column=0, padx=10, pady=5)
		self.window.resizable(0,0)
		self.window.title("Calculator")
		self.window.config(bg="black")
		self.buttons()
		self.textarea_func()
		self.calculating_things=""

	def textarea_func(self):
		self.textarea=Text(self.window,height="3", width="51",font=("Arial", 25, "bold"))
		self.textarea.grid(row=1,columnspan=self.width)

	def calcuating_func(self,n):
			self.calculating_things+=(n)
			self.textarea.delete(1.0, "end")
			self.textarea.insert(1.0,self.calculating_things)
	def buttons(self):
		# When using the Command parm don't call the function with () just the name would do, and if you wanna use pass some arguments then use lambda
		numbers=['1','2','3','4','5','6','7','8','9','0']
		misc = ['AC', '%', 'Sq', '√']
		btn_1 = Button(self.window,buttons_difgits,text="1", command=lambda: self.calcuating_func("1"))
		btn_1.grid(row=2, column=1)

		btn_2 = Button(self.window,buttons_difgits,text="2", command=lambda: self.calcuating_func("2"))
		btn_2.grid(row=2, column=2)

		btn_3 = Button(self.window,buttons_difgits,text="3", command=lambda: self.calcuating_func("3"))
		btn_3.grid(row=2, column=3)

		btn_4 = Button(self.window,buttons_difgits,text="4", command=lambda: self.calcuating_func("4"))
		btn_4.grid(row=2, column=4)

		btn_5 = Button(self.window,buttons_difgits,text="5", command=lambda: self.calcuating_func("5"))
		btn_5.grid(row=3, column=1)

		btn_6 = Button(self.window,buttons_difgits,text="6", command=lambda: self.calcuating_func("6"))
		btn_6.grid(row=3, column=2)

		btn_7 = Button(self.window,buttons_difgits,text="7", command=lambda: self.calcuating_func("7"))
		btn_7.grid(row=3, column=3)

		btn_8 = Button(self.window,buttons_difgits,text="8", command=lambda: self.calcuating_func("8"))
		btn_8.grid(row=3, column=4)

		btn_9 = Button(self.window,buttons_difgits,text="9", command=lambda: self.calcuating_func("9"))
		btn_9.grid(row=4, column=1)

		btn_0 = Button(self.window,buttons_difgits,text="0", command=lambda: self.calcuating_func("0"))
		btn_0.grid(row=4, column=2)

		btn_ac = Button(self.window,{"height":3, "width":26},text="AC", command=lambda:print("Clear!"), bg="red" ,font=("Arial", FONT, "bold"))
		btn_ac.grid(row=4, column=3)

		btn_ac = Button(self.window,{"height":3, "width":26},text="=", command=lambda:print("Clear!"), bg="lightgreen" ,font=("Arial", FONT, "bold"))
		btn_ac.grid(row=4, column=4)
	def main(self):
		string = input("Enter the calcutaion to be carried out : ")
		# allowed_basic ="0123456789+-/*()"
		# clean="".join(char for char in string if char in allowed_basic)
		# try:
		# 	print(f"The result for {string} is {eval(clean)}")
		# except SyntaxError:
		# 	print("Incorrect syntax used.")

	def start(self):
		self.window.mainloop()

if __name__ == "__main__":
	app = Calculator()
	app.start()


