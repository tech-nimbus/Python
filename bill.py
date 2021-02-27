from tkinter import *
import math, random
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ==================Variables==================
            #=================Cosmetics===================
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()

        self.soap_price = 40.0
        self.face_cream_price = 120.0
        self.face_wash_price = 60.0
        self.spray_price = 180.0
        self.gel_price = 140.0
        self.lotion_price = 180.0

            # ===================Grocery======================
        self.rice = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        self.oil = IntVar()

        self.rice_price = 80.0
        self.daal_price = 180.0
        self.wheat_price = 240.0
        self.sugar_price = 45.0
        self.tea_price = 150.0
        self.oil_price = 180.0

            #===================Cold Drinks====================
        self.maaza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        self.maaza_price = 60.0
        self.coke_price = 60.0
        self.frooti_price = 50.0
        self.thumbsup_price = 45.0
        self.limca_price = 40.0
        self.sprite_price = 60.0

            # ===============Total price and Tax Variable===============
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

            #================Customer================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no = StringVar()
        self.bill_no = str(x)
        self.search_bill = StringVar()


        # =============Customer Detail Frame=============
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", fg="white", bg=bg_color, font=("times new roman", 18, "bold")).grid(
            row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Phone No.", fg="white", bg=bg_color, font=("times new roman", 18, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        cbill_lbl = Label(F1, text="Bill Number", fg="white", bg=bg_color, font=("times new roman", 18, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, pady=10,
                                                                                        padx=10)

        # ==============Cosmetics Frame=============
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)

        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=10, textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=10, textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=10, textvariable=self.gel, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        Body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_txt = Entry(F2, width=10, textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)

        # ==============Grocery Frame=============
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=326, y=180, width=325, height=380)

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                     padx=10, pady=10)

        g2_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                     padx=10, pady=10)

        g3_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                     padx=10, pady=10)

        g4_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                     padx=10, pady=10)

        g5_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                     padx=10, pady=10)

        g6_lbl = Label(F3, text="Cooking Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                     padx=10, pady=10)

        # ==============Cold Drink Frame=============
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=651, y=180, width=325, height=380)

        c1_lbl = Label(F4, text="Maaza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.maaza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                     padx=10, pady=10)

        c2_lbl = Label(F4, text="Coke", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10,
                                                                                                                 sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.coke, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                     padx=10, pady=10)

        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=2, column=0, padx=10, pady=10, sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                     padx=10, pady=10)

        c4_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=3, column=0, padx=10, pady=10, sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                     padx=10, pady=10)

        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                     padx=10, pady=10)

        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=5, column=0, padx=10, pady=10, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                     padx=10, pady=10)

        # ===============Bill Area=================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=977, y=180, width=375, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


        # ==================Button Frame===============

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Cosmetic Price", font=("times new roman", 14, "bold"), bg= bg_color, fg="white").grid(row=0, column=0, padx=20, pady=1, sticky="W")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="white").grid(row=1, column=0, padx=20, pady=1, sticky="W")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="white").grid(row=2, column=0, padx=20, pady=1, sticky="W")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        t1_lbl = Label(F6, text="Cosmetic Tax", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="white").grid(row=0, column=2, padx=20, pady=1, sticky="W")
        t1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        t2_lbl = Label(F6, text="Grocery Tax", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="white").grid(row=1, column=2, padx=20, pady=1, sticky="W")
        t2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        t3_lbl = Label(F6, text="Cold Drinks Tax", font=("times new roman", 14, "bold"), bg=bg_color,
                       fg="white").grid(row=2, column=2, padx=20, pady=1, sticky="W")
        t3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=745, width=585, height=105)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white", font="arial 15 bold", pady=15, width=10, bd=2).grid(row=0, column=0, padx=5, pady=5)
        Gbill_btn = Button(btn_F, command=self.bill_area, text="Generate Bill", bg="cadetblue", fg="white", font="arial 15 bold", pady=15, width=10,
                           bd=2).grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear", bg="cadetblue", fg="white", font="arial 15 bold", pady=15, width=10,
                           bd=2).grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit", bg="cadetblue", fg="white", font="arial 15 bold", pady=15, width=10,
                           bd=2).grid(row=0, column=3, padx=5, pady=5)
        #self.welcome_bill()

    def total(self):
        self.total_soap_price = self.soap.get()*self.soap_price
        self.total_face_cream_price = self.face_cream.get()*self.face_cream_price
        self.total_face_wash_price = self.face_wash.get()*self.face_wash_price
        self.total_spray_price = self.spray.get()*self.spray_price
        self.total_gel_price = self.gel.get()*self.gel_price
        self.total_lotion_price = self.lotion.get()*self.lotion_price
        self.total_cosmetic_price =float(
                                    self.total_soap_price +
                                    self.total_face_cream_price +
                                    self.total_face_wash_price +
                                    self.total_spray_price +
                                    self.total_gel_price +
                                    self.total_lotion_price
                                    )
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.cosmetic_tax.set("Rs. " + str(round((self.total_cosmetic_price*0.05), 2)))

        self.total_rice_price = self.rice.get() * self.rice_price
        self.total_daal_price = self.daal.get() * self.daal_price
        self.total_wheat_price = self.wheat.get() * self.wheat_price
        self.total_sugar_price = self.sugar.get() * self.sugar_price
        self.total_tea_price = self.tea.get() * self.tea_price
        self.total_oil_price = self.oil.get() * self.oil_price
        self.total_grocery_price = float(
                                        self.total_rice_price +
                                        self.total_daal_price +
                                        self.total_wheat_price +
                                        self.total_sugar_price +
                                        self.total_tea_price +
                                        self.total_oil_price
                                        )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.grocery_tax.set("Rs. " + str(round((self.total_grocery_price * 0.05), 2)))

        self.total_maaza_price = self.maaza.get() * self.maaza_price
        self.total_coke_price = self.coke.get() * self.coke_price
        self.total_frooti_price = self.frooti.get() * self.frooti_price
        self.total_thumbsup_price = self.thumbsup.get() * self.thumbsup_price
        self.total_limca_price = self.limca.get() * self.limca_price
        self.total_sprite_price = self.sprite.get() * self.sprite_price
        self.total_cold_drink_price = float(
                                            self.total_maaza_price +
                                            self.total_coke_price +
                                            self.total_frooti_price +
                                            self.total_thumbsup_price +
                                            self.total_limca_price +
                                            self.total_sprite_price
                                            )
        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.cold_drink_tax.set("Rs. " + str(round((self.total_cold_drink_price * 0.05), 2)))
        self.total_price = str(self.total_cosmetic_price + self.total_grocery_price + self.total_cold_drink_price)
        #if (self.total_cosmetic_price == 0) & (self.total_grocery_price == 0) & (self.total_cold_drink_price == 0):
        #    self.txtarea.insert(END, f"\nNo Product has been selected")

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t Welcome Shopping\n")
        self.txtarea.insert(END, f"\n Bill Number: {self.bill_no}")
        self.txtarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Customer Phone: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n=========================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n=========================================")


    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        elif (self.total_cosmetic_price == 0) & (self.total_grocery_price == 0) & (self.total_cold_drink_price == 0):
            messagebox.showerror("Error", "No product has been selected")
        else:
            self.welcome_bill()
            self.total()
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\nBath Soap\t\t{self.soap.get()}\t\t{self.total_soap_price}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\nFace Cream\t\t{self.face_cream.get()}\t\t{self.total_face_cream_price}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\nFace Wash\t\t{self.face_wash.get()}\t\t{self.total_face_wash_price}")
            if self.spray.get() != 0:
                self.txtarea.insert(END, f"\nHair Spray\t\t{self.spray.get()}\t\t{self.total_spray_price}")
            if self.gel.get() != 0:
                self.txtarea.insert(END, f"\nHair Gel\t\t{self.gel.get()}\t\t{self.total_gel_price}")
            if self.lotion.get() != 0:
                self.txtarea.insert(END, f"\nBody Lotion\t\t{self.lotion.get()}\t\t{self.total_lotion_price}")
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t\t{self.total_rice_price}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\nDaal\t\t{self.daal.get()}\t\t{self.total_daal_price}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t\t{self.total_wheat_price}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t\t{self.total_sugar_price}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\nTea\t\t{self.tea.get()}\t\t{self.total_tea_price}")
            if self.oil.get() != 0:
                self.txtarea.insert(END, f"\nCooking Oil\t\t{self.oil.get()}\t\t{self.total_oil_price}")
            if self.maaza.get() != 0:
                self.txtarea.insert(END, f"\nMaaza\t\t{self.maaza.get()}\t\t{self.total_maaza_price}")
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\nCoke\t\t{self.coke.get()}\t\t{self.total_coke_price}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\nFrooti\t\t{self.frooti.get()}\t\t{self.total_frooti_price}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(END, f"\nThumbs Up\t\t{self.thumbsup.get()}\t\t{self.total_thumbsup_price}")
            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\nLimca\t\t{self.limca.get()}\t\t{self.total_limca_price}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\nSprite\t\t{self.sprite.get()}\t\t{self.total_sprite_price}")
            self.txtarea.insert(END, f"\n========================================")
            self.txtarea.insert(END, f"\nTotal Price =            \t\t\tRs. {self.total_price}")


root = Tk()
obj = Bill_App(root)
root.mainloop()
