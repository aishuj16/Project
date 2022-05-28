from distutils.cmd import Command
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime
class Lib:
	def __init__(self, root):
		self.root = root
		self.root.title("Library Management System")
		self.root.geometry("1560x800+0+0")

# **********************************************Variables**************************************************************************

		self.member_var = StringVar()
		self.prn_var = StringVar()
		self.id_var = StringVar()
		self.firstname_var = StringVar()
		self.lastname_var = StringVar()
		self.address1_var = StringVar()
		self.address2_var = StringVar()
		self.postcode_var = StringVar()
		self.mobile_var = StringVar()
		self.bookid_var = StringVar()
		self.booktitle_var = StringVar()
		self.author_var = StringVar()
		self.dateborrowed_var = StringVar()
		self.datedue_var = StringVar()
		self.daysonbook_var = StringVar()
		self.latereturnfine_var = StringVar()
		self.dateoverdue_var = StringVar()
		self.actualprice_var = StringVar()




		lbtitle = Label(self.root, text = "LIBRARY MANAGEMENT SYSTEM", bg="snow", fg="purple",bd=15, relief=RIDGE, font =("Sitka Heading", 30,"bold"), padx=2,pady=6)
		lbtitle.pack(side=TOP, fill= X)
	
		frame = Frame(self.root, bd=12 , relief = RIDGE, padx = 20, bg="Snow")
		frame.place(x=2 , y=100, width=1530,height = 600)

#****************************Left side **************************************************************
		DataFrameLeft = LabelFrame(self.root,text = "LIBRARY MEMBERSHIP INFO", bg="snow", fg="teal",bd=10, relief=RIDGE, font =("Javanese Text", 12,"bold"), padx=2,pady=6 )
		DataFrameLeft .place(x =18 , y = 115 , width =900 , height=410)
		

		lbMember = Label(DataFrameLeft, bg="Snow", text = "Member Type", font = ("Javanese Text", 10 ,"bold"), padx =2 , pady = 2)
		lbMember.grid(row=0, column=0 , sticky="W" )

		comMem=ttk.Combobox(DataFrameLeft, font = ("Javanese Text", 10 ,"bold"), state = "readonly" , width=18, textvariable = self.member_var )
		comMem["value"]=("Admin Staff" , "Lecturer" , "Student")
		comMem.grid(row =0, column = 1)

		lbPRN=Label(DataFrameLeft, bg="Snow", text = "PRN ", font = ("Javanese Text", 10 ,"bold"), padx =2, pady = 2)
		lbPRN.grid(row=1, column=0 , sticky="W")
		txtPRN =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20, textvariable = self.prn_var)
		txtPRN.grid(row = 1 , column = 1 , sticky="W")
		
		lbID=Label(DataFrameLeft, bg="Snow", text = "ID ", font = ("Javanese Text", 10 ,"bold"), padx =2, pady = 2)
		lbID.grid(row=2, column=0 , sticky="W")
		txtID =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20, textvariable = self.id_var )
		txtID.grid(row = 2 , column = 1 , sticky="W")

		lbFname=Label(DataFrameLeft, bg="Snow", text = "First Name  ",font = ("Javanese Text", 10 ,"bold"), padx =2, pady = 2)
		lbFname.grid(row=3, column=0 , sticky="W")
		txtFname =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20, textvariable =self.firstname_var )
		txtFname.grid(row = 3 , column = 1 , sticky="W")

		lbLname=Label(DataFrameLeft, bg="Snow", text = "Last Name ", font = ("Javanese Text", 10 ,"bold"), padx =2, pady = 2)
		lbLname.grid(row=4, column=0 , sticky="W")
		txtLname =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20, textvariable = self.lastname_var )
		txtLname.grid(row = 4 , column = 1 , sticky="W")

		lbAdd1=Label(DataFrameLeft, bg="Snow", text = "Address 1 ", font = ("Javanese Text", 10 ,"bold"), padx =2, pady = 2)
		lbAdd1.grid(row=5, column=0 , sticky="W")
		txtAdd1 =Entry(DataFrameLeft , font = ("Javanese Text", 10 ,"bold"), width=20 , textvariable = self.address1_var)
		txtAdd1.grid(row = 5 , column = 1 , sticky="W")

		lbAdd2=Label(DataFrameLeft, bg="Snow", text = "Address 2 ", font = ("Javanese Text", 10 ,"bold"), padx =2, pady = 2)
		lbAdd2.grid(row=6, column=0 , sticky="W")
		txtAdd2 =Entry(DataFrameLeft , font = ("Javanese Text", 10 ,"bold"), width=20 , textvariable = self.address2_var)
		txtAdd2.grid(row = 6 , column = 1 , sticky="W")

		lbPostCode=Label(DataFrameLeft, bg="Snow", text = "Post Code ", font = ("Javanese Text", 10 ,"bold"), padx =2, pady = 2)
		lbPostCode.grid(row=7, column=0 , sticky="W")
		txtPostCode =Entry(DataFrameLeft , font = ("Javanese Text", 10 ,"bold"), width=20 , textvariable =self.postcode_var )
		txtPostCode.grid(row = 7 , column = 1 , sticky="W")

		lbMobile=Label(DataFrameLeft, bg="Snow", text = "Mobile ", font = ("Javanese Text", 10 ,"bold"), padx =2, pady = 2)
		lbMobile.grid(row=8, column=0 , sticky="W")
		txtMobile =Entry(DataFrameLeft , font = ("Javanese Text", 10 ,"bold"), width=20 , textvariable = self.mobile_var  )
		txtMobile.grid(row = 8 , column = 1 , sticky="W")

		lbBookid=Label(DataFrameLeft, bg="Snow", text = "Book ID ", font = ("Javanese Text", 10 ,"bold"), padx =65, pady = 2)
		lbBookid.grid(row=0, column=2 , sticky="W")
		txtBookid =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20 ,textvariable = self.bookid_var)
		txtBookid.grid(row = 0 , column = 3 , sticky="W")

		lbBooktit=Label(DataFrameLeft, bg="Snow", text = "Book Title ", font = ("Javanese Text", 10 ,"bold"), padx =65, pady = 2)
		lbBooktit.grid(row=1, column=2 , sticky="W")
		txtBooktit =Entry(DataFrameLeft , font = ("Javanese Text", 10 ,"bold"), width=20 , textvariable =self.booktitle_var )
		txtBooktit.grid(row = 1 , column = 3 , sticky="W")

		lbAuthor=Label(DataFrameLeft, bg="Snow", text = "Author ", font = ("Javanese Text", 10 ,"bold"), padx =65, pady = 2)
		lbAuthor.grid(row=2, column=2 , sticky="W")
		txtAuthor =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20 , textvariable  =self.author_var  )
		txtAuthor.grid(row = 2 , column = 3 , sticky="W")

		lbBorrowed=Label(DataFrameLeft, bg="Snow", text = "Borrowed  Date ", font = ("Javanese Text", 10 ,"bold"), padx =65, pady = 2)
		lbBorrowed.grid(row=3, column=2 , sticky="W")
		txtBorrowed =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20,  textvariable = self.dateborrowed_var )
		txtBorrowed.grid(row = 3 , column = 3 , sticky="W")

		lbDue=Label(DataFrameLeft, bg="Snow", text = "Due Date ", font = ("Javanese Text", 10 ,"bold"), padx =65, pady = 2)
		lbDue.grid(row=4, column=2 , sticky="W")
		txtDue =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20 , textvariable = self.datedue_var  )
		txtDue.grid(row = 4 , column = 3 , sticky="W")

		lbDaysonbook=Label(DataFrameLeft, bg="Snow", text = "Days On Book", font = ("Javanese Text", 10 ,"bold"), padx =65, pady = 2)
		lbDaysonbook.grid(row=5, column=2 , sticky="W")
		txtDaysonbook =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20 , textvariable = self.daysonbook_var  )
		txtDaysonbook.grid(row = 5 , column = 3 , sticky="W")

		lbLatereturn=Label(DataFrameLeft, bg="Snow", text = "Late Return Fine ",font = ("Javanese Text", 10 ,"bold"), padx =65, pady = 2)
		lbLatereturn.grid(row=6, column=2 , sticky="W")
		txtLatereturn =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20 , textvariable =self.latereturnfine_var)
		txtLatereturn.grid(row = 6 , column = 3 , sticky="W")

		lbDateoverdue=Label(DataFrameLeft, bg="Snow", text = "Date Over Due ", font = ("Javanese Text", 10 ,"bold"), padx =65, pady = 2)
		lbDateoverdue.grid(row=7, column=2 , sticky="W")
		txtDateoverdue =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20 , textvariable = self.dateoverdue_var )
		txtDateoverdue.grid(row = 7 , column = 3 , sticky="W")

		lbActprice=Label(DataFrameLeft, bg="Snow", text = "Actual Price ", font = ("Javanese Text", 10 ,"bold"), padx =65, pady = 2)
		lbActprice.grid(row=8, column=2 , sticky="W")
		txtActprice =Entry(DataFrameLeft ,font = ("Javanese Text", 10 ,"bold"), width=20, textvariable  = self.actualprice_var )
		txtActprice.grid(row = 8 , column = 3 , sticky="W")


#****************************Right side **************************************************************
		DataFrameRight = LabelFrame(self.root,text = "BOOK DETAILS", bg="snow", fg="teal",bd=10, relief=RIDGE, font =("Javanese Text", 12,"bold"), padx=2,pady=6 )
		DataFrameRight .place(x =920 , y = 115 , width =600 , height= 410)


		self.txtBox = Text(DataFrameRight, font = ("Javanese Text", 10 ,), width = 35 , height = 11 , padx = 4 , pady = 4)
		self.txtBox.grid(row = 0 , column = 2)

		listscrollbar= Scrollbar(DataFrameRight)
		listscrollbar.grid(row = 0 , column = 0 ,sticky = "NS")

		listBook = ["In Search of Lost Time",  "Ulysses" ,  "Don Quixote" ,  "The Great Gatsby" , "Moby Dick",  "War and Peace" , 
			 "Hamlet"  , "The Odyssey" , "Crime and Punishment" , "Wuthering Heights" ,  "Pride and Prejudice" , "Anna Karenina" , 
			"To the Lighthouse"  ,  "Invisible Man" , "Beloved"]

		def selectbook(event = " "):
			value = str(listBox.get(listBox.curselection()))
			x = value
			if (x=="In Search of Lost Time"):
				self.bookid_var.set("BK456")
				self.booktitle_var.set("In Search of Lost Time")
				self.author_var.set("Vesrian . K ")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("500")


			elif (x=="Ulysses"):
				self.bookid_var.set("BK451")
				self.booktitle_var.set("IUlysses")
				self.author_var.set("Simik.A")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 150")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("550")


			elif (x=="Don Quixote"):
				self.bookid_var.set("BK486")
				self.booktitle_var.set("Don Quixote")
				self.author_var.set("V .K ")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("400")

			elif (x=="The Great Gatsby"):
				self.bookid_var.set("BK756")
				self.booktitle_var.set("The Great Gatsby")
				self.author_var.set("Mark N ")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("800")

			elif (x=="Moby Dick"):
				self.bookid_var.set("BK426")
				self.booktitle_var.set("Moby Dick")
				self.author_var.set("Roy.WB ")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("569")

			elif (x=="War and Peace"):
				self.bookid_var.set("BK226")
				self.booktitle_var.set("War and Peace")
				self.author_var.set("Anna.Levi")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("900")


			elif (x=="Hamlet"):
				self.bookid_var.set("BK356")
				self.booktitle_var.set("Hamlet")
				self.author_var.set("Quench .R")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("600")

			elif (x=="The Odyssey"):
				self.bookid_var.set("BK983")
				self.booktitle_var.set("The Odyssey")
				self.author_var.set("Lucy.white")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("660")

			elif (x=="Crime and Punishment"):
				self.bookid_var.set("BK325")
				self.booktitle_var.set("Crime and Punishment")
				self.author_var.set("Sims.claw ")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("580")

			elif (x=="Wuthering Heights"):
				self.bookid_var.set("BK378")
				self.booktitle_var.set("Wuthering Heights")
				self.author_var.set("Luther K ")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("300")

			elif (x=="Pride and Prejudice"):
				self.bookid_var.set("BK222")
				self.booktitle_var.set("Pride and Prejudice")
				self.author_var.set("Jean .D")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("700")

			elif (x=="Anna Karenina"):
				self.bookid_var.set("BK689")
				self.booktitle_var.set("Anna Karenina")
				self.author_var.set("Sean.P ")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("555")

			elif (x=="To the Lighthouse"):
				self.bookid_var.set("BK666")
				self.booktitle_var.set("To the Lighthouse")
				self.author_var.set("Vean . J ")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("789")

			elif (x=="Invisible Man"):
				self.bookid_var.set("BK777")
				self.booktitle_var.set("Invisible Man")
				self.author_var.set("Vesrian . K ")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("500")

			elif (x=="Beloved"):
				self.bookid_var.set("BK787")
				self.booktitle_var.set("Beloved")
				self.author_var.set("Vesrian . K ")
				d1 = datetime.date.today()
				d2 = datetime.timedelta(days = 15)
				d3 = d1 + d2
				self.dateborrowed_var.set(d1)
				self.datedue_var.set(d3)
				self.daysonbook_var.set(15)
				self.latereturnfine_var.set("Rs 100")
				self.dateoverdue_var.set("NO")
				self.actualprice_var.set("444")


		
		listBox = Listbox(DataFrameRight ,font = ("Javanese Text", 10 ,), width = 30 , height = 11 )
		listBox.bind("<<ListboxSelect>>" , selectbook)
		listBox.grid(row = 0 , column = 1 ,padx = 4 )
		
		listscrollbar.config(command = listBox.yview)
	
		for i in listBook : 
			listBox.insert(END , i)
#****************************Button frame **************************************************************
		ButtonFrame = Frame(self.root, bg="snow",padx = 8 ,bd=10, relief=RIDGE)
		ButtonFrame.place(x=0 , y=530,width= 1560, height =70)

		btAdd = Button(ButtonFrame, text =  "ADD " , font = ("Javanese Text", 10 , "bold"), width = 25,  bg = "Purple" , fg = "snow" , command = self.add_data)
		btAdd.grid(row = 0 , column = 0 , padx= 8 )
		
		btshow = Button(ButtonFrame, text =  "SHOW " , font = ("Javanese Text", 10 , "bold"), width = 25,  bg = "Purple" , fg = "snow" , command=self.showData)
		btshow.grid(row = 0 , column = 1, padx= 8)

		btupdate = Button(ButtonFrame, text =  "UPDATE " , font = ("Javanese Text", 10 , "bold"), width = 25,  bg = "Purple" , fg = "snow" , command=self.update)
		btupdate.grid(row = 0 , column = 2 , padx= 8 )

		btdelete = Button(ButtonFrame, text =  "DELETE " , font = ("Javanese Text", 10 , "bold"), width = 25,  bg = "Purple" , fg = "snow" , command=self.delete)
		btdelete.grid(row = 0 , column = 3, padx= 8 )

		btreset = Button(ButtonFrame, text =  "RESET" , font = ("Javanese Text", 10 , "bold"), width = 25,  bg = "Purple" , fg = "snow", command=self.reset)
		btreset.grid(row = 0 , column = 4, padx= 8)

		btexit = Button(ButtonFrame, text =  "EXIT" , font = ("Javanese Text", 10 , "bold"), width = 25,  bg = "Purple" , fg = "snow", command=self.iExit)
		btexit.grid(row = 0 , column = 5, padx= 8 )

#****************************Details Frame **************************************************************		
		DetailsFrame = Frame(self.root, bg="snow",padx = 5 ,bd=10, relief=RIDGE)
		DetailsFrame.place(x=0 , y=600,width= 1560, height =182)

		tableFrame = Frame(DetailsFrame, bg="snow" ,bd=6, relief=RIDGE)
		tableFrame.place(x = 0 , y = 2 , width = 1508 , height = 160)
		


		xscroll=ttk.Scrollbar(tableFrame , orient = HORIZONTAL)
		yscroll=ttk.Scrollbar(tableFrame , orient = VERTICAL)

		self.lib_table = ttk.Treeview(tableFrame, column=("Member type", "PRN" ,"ID", "Firstname", "Lastname" ,
		"Address 1", "Address 2", "Post Code", "Mobile", "Book id", "Book title", "Author", "Date borrowed", 
		"Date due", "Days", "Late return fine", "Date over due", "Final Price"), xscrollcommand =xscroll.set , yscrollcommand =yscroll.set )


		xscroll.pack(side = BOTTOM , fill = X)
		yscroll.pack(side = RIGHT , fill = Y)

		xscroll.config(command = self.lib_table.xview)
		yscroll.config(command = self.lib_table.yview)
		

		
		self.lib_table.heading("Member type", text = "Member type")
		self.lib_table.heading("PRN", text = "PRN")
		self.lib_table.heading("ID", text = "ID")
		self.lib_table.heading("Title", text = "Title")
		self.lib_table.heading("Firstname", text = "Firstname")
		self.lib_table.heading("Lastname", text = "Lastname")
		self.lib_table.heading("Address 1", text = "Address 1")
		self.lib_table.heading("Address 2", text ="Address 2")
		self.lib_table.heading("Post Code", text = "Post Code")
		self.lib_table.heading("Mobile", text = "Mobile")
		self.lib_table.heading("Book id", text = "Book id")
		self.lib_table.heading("Book title", text = "Book title")
		self.lib_table.heading("Author", text = "Author")
		self.lib_table.heading("Date borrowed", text = "Date borrowed")
		self.lib_table.heading("Date due", text = "Date due")
		self.lib_table.heading("Days", text = "Days")
		self.lib_table.heading("Late return fine", text = "Late return fine")
		self.lib_table.heading("Date over due", text = "Date over due")
		self.lib_table.heading("Final Price", text = "Final Price")



		self.lib_table.column("Member type", width =100)
		self.lib_table.column("PRN", width =100)
		self.lib_table.column("ID", width =100)
		self.lib_table.column("Title", width =100)
		self.lib_table.column("Firstname", width =100)
		self.lib_table.column("Lastname", width =100)
		self.lib_table.column("Address 1", width =100)
		self.lib_table.column("Address 2", width =100)
		self.lib_table.column("Post Code", width =100)
		self.lib_table.column("Mobile", width =100)
		self.lib_table.column("Book id", width =100)
		self.lib_table.column("Book title", width =100)
		self.lib_table.column("Author", width =100)
		self.lib_table.column("Date borrowed", width =100)
		self.lib_table.column("Date due", width =100)
		self.lib_table.column("Days", width =100)
		self.lib_table.column("Late return fine",width =100)
		self.lib_table.column("Date over due", width =100)
		self.lib_table.column("Final Price", width =100)

		self.Fetch_data()
		self.lib_table.bind("<ButtonRelease-1>", self.get_cursor)

		self.lib_table["show"]="headings"
		self.lib_table.pack(fill = BOTH , expand = 1)


# ************************************************** Connection and function *********************************************************
	con = None

	
	
	def add_data(self):
		con = mysql.connector.connect(host = "localhost",username = "root",password = "abc456", database = "Library")
		my_cursor = con.cursor()
		my_cursor.execute("insert into lib values(%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s )", (self.member_var.get(),
		self.prn_var .get(), self.id_var.get(), self.firstname_var.get(), self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(), 
		self.postcode_var.get(), self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(), self.author_var.get(), self.dateborrowed_var.get(), 
		self.datedue_var.get(), self.daysonbook_var.get(), self.latereturnfine_var.get(), self.dateoverdue_var.get(), self.actualprice_var.get()))

		con.commit()
		self.Fetch_data()
		self.reset()
		con.close()
	
		messagebox.showinfo("Success", "Data added succcessfully")

	def update(self):
		con = mysql.connector.connect(host = "localhost",username = "root",password = "abc456", database = "Library")
		my_cursor = con.cursor()
		my_cursor.execute("update lib set Member =%s,ID =%s,Firstname =%s,Lastname =%s,Address1 =%s,Address2 =%s,postcode =%s,Mobile =%s,Bookid =%s,Booktitle =%s,Author =%s,Borroweddate =%s,Duedate =%s,Dayonbook =%s,Latereturnfine =%s,Dateoverdue =%s,Actualprice =%s where PRN=%s",
		(self.member_var.get(),
		self.id_var.get(),
		self.firstname_var.get(),
		self.lastname_var.get(),
		self.address1_var.get(),
		self.address2_var.get(), 
		self.postcode_var.get(),
		self.mobile_var.get(),
		self.bookid_var.get(),
		self.booktitle_var.get(),
		self.author_var.get(),
		self.dateborrowed_var.get(), 
		self.datedue_var.get(),
		self.daysonbook_var.get(), 
		self.latereturnfine_var.get(),
		self.dateoverdue_var.get(),
		self.actualprice_var.get(),
		self.prn_var.get(),
		))
 
		con.commit()
		self.Fetch_data()
		self.reset()
		con.close()
		messagebox.showinfo("Success", "Data updated succcessfully")


	def Fetch_data(self):
		con = mysql.connector.connect(host = "localhost",username = "root",password = "abc456", database = "Library")
		my_cursor = con.cursor()
		my_cursor.execute("Select * from lib")
		rows = my_cursor.fetchall()

		if len(rows)!=0:
			self.lib_table.delete(*self.lib_table.get_children())
			for i in rows:
				self.lib_table.insert("" ,END,values=i)
			con.commit()
		con.close()



	def get_cursor(self,event=""):
		cursor_row = self.lib_table.focus()
		content = self.lib_table.item(cursor_row)
		row = content['values']

		self.member_var.set(row[0]),
		self.prn_var.set(row[1]),
		self.id_var.set(row[2]),
		self.firstname_var.set(row[3]),
		self.lastname_var.set(row[4]),
		self.address1_var.set(row[5]),
		self.address2_var.set(row[6]),
		self.postcode_var.set(row[7]),
		self.mobile_var.set(row[8]),
		self.bookid_var.set(row[9]),
		self.booktitle_var.set(row[10]),
		self.author_var.set(row[11]),
		self.dateborrowed_var.set(row[12]),
		self.datedue_var.set(row[13]),
		self.daysonbook_var.set(row[14]),
		self.latereturnfine_var.set(row[15]),
		self.dateoverdue_var.set(row[16]),
		self.actualprice_var.set(row[17])


	def showData(self):
		self.txtBox.insert(END, "Member Type:\t\t"+ self.member_var.get() + "\n")
		self.txtBox.insert(END, "PRN :\t\t"+ self.prn_var.get() + "\n")
		self.txtBox.insert(END, "ID :\t\t"+ self.id_var.get() + "\n")
		self.txtBox.insert(END, "Firstname :\t\t"+ self.firstname_var.get() + "\n")
		self.txtBox.insert(END, "Lastname:\t\t"+ self.lastname_var.get() + "\n")
		self.txtBox.insert(END, "Address 1 :\t\t"+ self.address1_var.get() + "\n")
		self.txtBox.insert(END, "Address 2 :\t\t"+ self.address2_var.get() + "\n")
		self.txtBox.insert(END, "Post :\t\t"+ self.postcode_var.get() + "\n")
		self.txtBox.insert(END, "Mobile :\t\t"+ self.mobile_var.get() + "\n")
		self.txtBox.insert(END, "Book id :\t\t"+ self.bookid_var.get() + "\n")
		self.txtBox.insert(END, "Book Title :\t\t"+ self.booktitle_var.get() + "\n")
		self.txtBox.insert(END, "Author :\t\t"+ self.author_var.get() + "\n")
		self.txtBox.insert(END, "Date Borrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
		self.txtBox.insert(END, "Days on Book :\t\t"+ self.daysonbook_var.get() + "\n")
		self.txtBox.insert(END, "Late Return Fine  :\t\t"+ self.latereturnfine_var.get() + "\n")
		self.txtBox.insert(END, "Date Overdue :\t\t"+ self.dateoverdue_var.get() + "\n")
		self.txtBox.insert(END, "Actual Price :\t\t"+ self.actualprice_var.get() + "\n")



	def reset(self):
		self.member_var.set(""),
		self.prn_var.set(""),
		self.id_var.set(""),
		self.firstname_var.set(""),
		self.lastname_var.set(""),
		self.address1_var.set(""),
		self.address2_var.set(""),
		self.postcode_var.set(""),
		self.mobile_var.set(""),
		self.bookid_var.set(""),
		self.booktitle_var.set(""),
		self.author_var.set(""),
		self.dateborrowed_var.set(""),
		self.datedue_var.set(""),
		self.daysonbook_var.set(""),
		self.latereturnfine_var.set(""),
		self.dateoverdue_var.set(""),
		self.actualprice_var.set("")
		self.txtBox.delete("1.0",END)


	def iExit(self):
		iExit = tkinter.messagebox.askyesno("Choose","Do you want to exit")
		if iExit >0:
			self.root.destroy()
			return


	def delete(self):
		if self.prn_var.get()=="" or self.id_var.get()=="":
			messagebox.showerror("error","Please select Member first")
		else:
			con = mysql.connector.connect(host = "localhost",username = "root",password = "abc456", database = "Library")
			my_cursor = con.cursor()
			query = "delete from lib where PRN=%s"
			value=(self.prn_var.get(),)
			my_cursor.execute(query,value)

			con.commit()
			self.Fetch_data()
			self.reset()
			con.close()
			messagebox.showinfo("Success", "Data deleted succcessfully")

if __name__ == "__main__":
	root = Tk()
	obj = Lib(root)
	root.mainloop()