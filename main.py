from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")
        bg_color="#856ff8"
        title=Label(self.root,text="Billing System",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=======variable============
        #=======cosmetics===========
        self.Bath_Soap=IntVar()
        self.Face_Cream=IntVar()
        self.Nailpolish=IntVar()
        self.Lipstick=IntVar()
        self.Eyeliner=IntVar()
        self.Body_Lotion=IntVar()
        #=======grocery===========
        self.Rice=IntVar()
        self.Coffee=IntVar()
        self.Sugar=IntVar()
        self.Cheese=IntVar()
        self.Bread=IntVar()
        self.Eggs=IntVar()
        #=======cosmetics===========
        self.Coke= IntVar()
        self.Sprite= IntVar()
        self.Dew= IntVar()
        self.Pepsi= IntVar()
        self.Red_Bull= IntVar()
        self.Fruit_Juice= IntVar()
        #========Total Products Price and Tax Variables=======
        self.Cosmetic_Price=StringVar()
        self.Grocery_Price=StringVar()
        self.Cold_Drinks_Price=StringVar()

        self.Cosmetic_Tax=StringVar()
        self.Grocery_Tax=StringVar()
        self.Cold_Drinks_Tax=StringVar()

        #==========Customer=============
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        #=======Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="firebrick",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=20)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=20)
        cphn_txt = Entry(F1, width=15,textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=20)
        c_bill_txt = Entry(F1, width=15,textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill, width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #=====Cosmetics Frame======
        F2=LabelFrame(self.root,bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),fg="firebrick", bg=bg_color)
        F2.place(x=5, y=180,width=325,height=380)

        Bath_Soap_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Bath_Soap_txt=Entry(F2,width=10,textvariable=self.Bath_Soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_Cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_Cream_txt = Entry(F2, width=10,textvariable=self.Face_Cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        Nail_Polish_lbl = Label(F2, text="Nail Polish", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Nail_Polish_txt = Entry(F2, width=10,textvariable=self.Nailpolish, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        Lipstick_lbl = Label(F2, text="Lipstick", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Lipstick_txt = Entry(F2, width=10,textvariable=self.Lipstick, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        Eyeliner_lbl = Label(F2, text="Eyeliner", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Eyeliner_txt = Entry(F2, width=10,textvariable=self.Eyeliner, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        Body_Lotion_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_Lotion_txt = Entry(F2, width=10,textvariable=self.Body_Lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        #====Grocery Frame======
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),fg="firebrick", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.Rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl = Label(F3, text="Coffee", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.Coffee, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.Sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl = Label(F3, text="Cheese", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10,textvariable=self.Cheese, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl = Label(F3, text="Bread", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.Bread, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl = Label(F3, text="Eggs ", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.Eggs, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #====Cold Drinks Frame======
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),fg="firebrick", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        c1_lbl = Label(F4, text="Coke", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10,textvariable=self.Coke, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10,textvariable=self.Sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl = Label(F4, text="Dew", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10,textvariable=self.Dew, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl = Label(F4, text="Pepsi", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.Pepsi,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl = Label(F4, text="Red Bull", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10,textvariable=self.Red_Bull, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl = Label(F4, text="Fruit Juice", font=("times new roman", 16, "bold"), bg=bg_color,fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10,textvariable=self.Fruit_Juice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #====Bill Area======
        F5=Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold", bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
