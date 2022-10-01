import tkinter as tk


class Calculator:
	def __init__(self):
		# Creates a Window for the calculator and initializes many things that are needed to run the calc aap
		self.window = tk.Tk()
		self.window.geometry("560x627")
		self.window.resizable()
		self.window.title("Calculator")	
		self.buttons()
		

	def buttons(self):
		self.button = tk.Button(self.window, text="Click here!", command = self.main())
		self.button.pack()
	def main(self):
		# string = input("Enter the calcutaion to be carried out : ")
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