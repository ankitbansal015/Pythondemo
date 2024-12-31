
from tkinter import *
from tkinter import messagebox
import math,random,os

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=========variable=========
        #=======cosmetics=========
        self.soap=IntVar()
        self.Face_wash=IntVar()
        self.face_cream = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.lotion = IntVar()

        #==========grocery=======
        self.daal = IntVar()
        self.sugar = IntVar()
        self.maida = IntVar()
        self.Atta = IntVar()
        self.haldi = IntVar()
        self.dhania = IntVar()

        #============cold drinks=======
        self.Mazza = IntVar()
        self.thumbs_up= IntVar()
        self.mountain_dew = IntVar()
        self.sprite= IntVar()
        self.frooti = IntVar()
        self.coca_cola = IntVar()

        #============total product price and tax variables======
        self.cosmetic_price=StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #========customer=======
        self.c_name=StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        x=random.randint(100,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()



        #=====customer deatil frame======
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_text = Entry(F1, width=15,textvariable=self.c_name ,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl=Label(F1,text=" Phone No",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_text=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_text=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

        #==========cosmetics frame=====
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=325,height=380)
        bath_lbl=Label(F2,text="Bath soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_wash_lbl=Label(F2,text="Facewash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_wash_txt=Entry(F2,width=10,textvariable=self.Face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="FaceCream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_shampoo_lbl=Label(F2,text="Hair shampoo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_shampoo_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_gel_lbl=Label(F2,text="Hair gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_gel_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lotion_lbl=Label(F2,text="Body lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_lotion_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # ==========grocery frame=====
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=170, width=325, height=380)
        g1_lbl = Label(F3, text="daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)

        g3_lbl = Label(F3, text="Maida", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10,textvariable=self.maida, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10,pady=10)

        g4_lbl = Label(F3, text="Aatta", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.Atta,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10,pady=10)

        g5_lbl = Label(F3, text="Haldi", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10,textvariable=self.haldi, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl = Label(F3, text="Dhania", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10,textvariable=self.dhania, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # ==========coldrinks Frame =====
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Coldrinks", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=670, y=170, width=325, height=380)
        c1_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        c1_txt = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        c2_lbl = Label(F4, text="Coco cola", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        c2_txt = Entry(F4, width=10,textvariable=self.coca_cola, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl = Label(F4, text="Thumb Up", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10,textvariable=self.thumbs_up, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10, pady=10)

        c5_lbl = Label(F4, text="Mountain Dew", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        c5_txt = Entry(F4, width=10,textvariable=self.mountain_dew, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl = Label(F4, text="Mazza", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.Mazza,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10, pady=10)

        #==============Bill area=========

        F5 =Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=370)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=======button frame============
        F6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl=Label(F6,text="Total Cosmetic price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6, text="Total grocery price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Coldrink price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18,textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(F6, text=" Cosmetic Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(F6, text="grocery Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(F6, text="Coldrink Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18,textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="All Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2, padx=5, pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3, padx=5, pady=5)
        self.Welcome_bill()


    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fw_p=self.Face_wash.get()*60
        self.c_fc_p=self.face_cream.get()*120
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.lotion.get()*180
        self.total_cosmetic_price=float(
            self.c_s_p+
            self.c_fw_p+
            self.c_fc_p+
            self.c_hs_p+
            self.c_hg_p+
            self.c_bl_p
            )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))

        self.g_da_p=self.daal.get() * 120
        self.g_s_p=self.sugar.get() * 40
        self.g_m_p=self.maida.get() * 30
        self.g_a_p=self.Atta.get() * 40
        self.g_h_p=self.haldi.get() *160
        self.g_d_p=self.dhania.get() * 180
        self.total_grocery_price = float(
            self.g_da_p+
            self.g_s_p+
            self.g_m_p +
            self.g_a_p+
            self.g_h_p+
            self.g_d_p
            )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.05),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_f_p=self.frooti.get() * 60
        self.d_c_p=self.coca_cola.get() * 60
        self.d_t_s=self.thumbs_up.get() * 50
        self.d_s_p=self.sprite.get() * 45
        self.d_mo_p=self.mountain_dew.get() * 55
        self.d_m_p=self.Mazza.get() * 35

        self.total_cold_drink_price = float(
            self.d_f_p +
            self.d_c_p +
            self.d_t_s +
            self.d_s_p +
            self.d_mo_p +
            self.d_m_p
            )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price * 0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))

        self.Total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_drink_price+
                              self.c_tax+
                              self.g_tax+
                              self.cd_tax
                            )

    def Welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWELCOME BANSAL CONFECTIONARY\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n======================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("ERROR","Customer Details are must")

        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("ERROR", "No Product Sold")
        else:


            self.Welcome_bill()
            #=========cosmetics=========
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.Face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face wash\t\t{self.Face_wash.get()}\t\t{self.c_fw_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n face cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\n hair spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get() != 0:
                self.txtarea.insert(END, f"\n hair gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n body lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

            #=========grocery=========
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.maida.get() != 0:
                self.txtarea.insert(END, f"\n maida\t\t{self.maida.get()}\t\t{self.g_m_p}")
            if self.Atta.get() != 0:
                self.txtarea.insert(END, f"\n Atta\t\t{self.Atta.get()}\t\t{self.g_a_p}")
            if self.haldi.get() != 0:
                self.txtarea.insert(END, f"\n Haldi\t\t{self.haldi.get()}\t\t{self.g_h_p}")
            if self.dhania.get()!=0:
                self.txtarea.insert(END,f"\n Dhania\t\t{self.dhania.get()}\t\t{self.g_d_p}")

            # =========cold-drink=========
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
            if self.coca_cola.get() != 0:
                self.txtarea.insert(END, f"\n Coca cola\t\t{self.coca_cola.get()}\t\t{self.d_c_p}")
            if self.thumbs_up.get() != 0:
                self.txtarea.insert(END, f"\n Thumbs up\t\t{self.thumbs_up.get()}\t\t{self.d_t_s}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
            if self.mountain_dew.get() != 0:
                self.txtarea.insert(END, f"\n Mountain dew\t\t{self.mountain_dew.get()}\t\t{self.d_mo_p}")
            if self.Mazza.get() != 0:
                self.txtarea.insert(END, f"\n Mazza\t\t{self.Mazza.get()}\t\t{self.d_m_p}")

            self.txtarea.insert(END, f"\n--------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmetics Tax\t\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill : \t\t\t Rs. {self.Total_bill}")
            self.txtarea.insert(END, f"\n--------------------------------------")
            self.Save_bill()
    def Save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save bill")

        if op>0:
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} Saved successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill no.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear Data?")
        if op > 0:


            self.soap.set(0)
            self.Face_wash.set(0)
            self.face_cream.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)

            # ==========grocery=======
            self.daal.set(0)
            self.sugar.set(0)
            self.maida.set(0)
            self.Atta.set(0)
            self.haldi.set(0)
            self.dhania.set(0)

            # ============cold drinks=======
            self.Mazza.set(0)
            self.thumbs_up.set(0)
            self.mountain_dew.set(0)
            self.sprite.set(0)
            self.frooti.set(0)
            self.coca_cola.set(0)

            # ============total product price and tax variables======
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # ========customer=======
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x = random.randint(100, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.Welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()


root=Tk()
obj=Bill_App(root)
root.mainloop()

