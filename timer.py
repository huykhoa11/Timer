from tkinter import *
win = Tk()
win.title("Timer")

l = Label(win, text="", font=("Helvetica", 40))
l.grid(pady=5,row=0, columnspan=3)
global hour
global minute
global second
global flag		#flag = 1 stop,   flag la de kiem soat ham tang giam?
global start    	#start la de kiem soat viec pause/stop
global check_begin  	# de phong tranh viec no cu lay e1.get(),e2.get(),e3.get() lien tuc, 
start = False		# o day ta chi muon lay e1.get(),e2.get(),e3.get() 1 lan dau tien khi bam nut thoi
check_begin = False

def press():
	global hour
	global minute
	global second
	global flag
	global start
	global check_begin
	if start == False:				#start la de kiem soat viec pause/stop
		start = True
		
		flag = 0					#flag la de kiem soat ham tang giam?
		if check_begin == False:	# de phong tranh viec no cu lay e1.get(),e2.get(),e3.get() lien tuc
			hour = str(e1.get()).zfill(2)
			minute = str(e2.get()).zfill(2)
			second = str(e3.get()).zfill(2)
			check_begin = True
		e1.delete(0, END)
		e2.delete(0, END)
		e3.delete(0, END)
		update()
	elif start == True:		# pause no tame
		start = False
		stop()
	
def update():
	global hour
	global minute
	global second
	global flag
	try:
		hour = int(hour)
		minute = int(minute)
		second = int(second)
		if hour<0 or minute<0 or second<0:
			reset()
	except:
		reset()

	if flag == 0:
		if hour == 0 and minute == 0 and second == 0:
			reset()
		elif hour == 0 and minute == 0 and second != 0:
			second -= 1
		elif hour == 0 and minute != 0 and second == 0:
			minute -= 1
			second = 59
		elif hour != 0 and minute == 0 and second == 0:
			hour -= 1
			minute = 59
			second = 59
		elif hour == 0 and minute != 0 and second != 0:
			second -= 1
			if second < 0:
				minute -= 1
		elif hour != 0 and minute != 0 and second == 0:
			minute -= 1
			second = 59
			if minute < 0:
				hour -= 1
		elif hour != 0 and minute == 0 and second != 0:
			second -= 1
			if second < 0:
				minute -= 1
		elif hour != 0 and minute != 0 and second != 0:
			second -= 1
		hour = str(hour).zfill(2)
		minute = str(minute).zfill(2)
		second = str(second).zfill(2)
		l.config(text = hour+ ":" +minute+ ":" +second)
		if flag == 0:
			l.after(1000, update)

def reset():
	global hour
	global minute
	global second
	global flag		# flag=1 => stop
	global start
	global check_begin
	start = False
	check_begin = False
	hour = str(0).zfill(2)
	minute = str(0).zfill(2)
	second = str(0).zfill(2)
	l.config(text = hour+ ":" +minute+ ":" +second)
	flag = 1

def stop():
	global flag
	flag = 1		# when pause, clock will not run

l1 = Label(win, text="HOUR")
l1.grid(padx=5, pady=2, row=1, column=0)
e1 = Entry(win, bd=5)
e1.grid(padx=5, pady=2, row=1, column=1)

l2 = Label(win, text="MINUTE")
l2.grid(padx=5, pady=2, row=2, column=0)
e2 = Entry(win, bd=5)
e2.grid(padx=5, pady=2, row=2, column=1)

l1 = Label(win, text="SECOND")
l1.grid(padx=5, pady=2, row=3, column=0)
e3 = Entry(win, bd=5)
e3.grid(padx=5, pady=2, row=3, column=1)

b = Button(win, text="Start/Pause", font=1, fg="red", width=12, height=2, command=press)
b.grid(padx=5, pady=10, row=4, column=0)

b1 = Button(win, text="Reset", font=1, fg="green", width=12, height=2, command=reset)
b1.grid(padx=5, pady=10, row=4, column=1)

if __name__ == "__main__":
	mainloop()
