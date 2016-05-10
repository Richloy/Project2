import os
from tkinter import *
from tkinter import ttk

class interface:

	def create_interface(self):
		root = Tk()
		'''scrollbar = Scrollbar(root)
		scrollbar.pack( side = RIGHT, fill=Y )

		mylist = Listbox(root, yscrollcommand = scrollbar.set )
		for line in range(100):
		   mylist.insert(END, "This is line number " + str(line))

		mylist.pack( side = LEFT, fill = BOTH )
		scrollbar.config( command = mylist.yview )'''
		colour = StringVar()
		colour.set('red')
		l = Label(root, textvariable=colour, fg = 'red', highlightbackground = 'blue')	
		btn = Button(root, text = "Click Me", highlightbackground = 'blue')
		
		l.pack()
		btn.pack()
		mainloop()
		
		
		
	def colourUpdate(self):
		if colour.get() != 'red':
			colour.set('red')
		else:
			colour.set('blue')
		print (colour.get())
		l.configure(fg=colour.get())


	
	
	
		'''window.mainloop()
		b1 = ttk.Button(window,text="One")
		b2 = ttk.Button(window,text="Two")'''
	
	def run_game(self, version):
		print ("Interface will now run Brick Collider Version " + version)
		#if version == 8:
		os.system("python BrickColliderv"+version+".py")



if __name__ == "__main__":
	interface().create_interface()