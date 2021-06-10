from tkinter import *
from db import select,drop_table
def menu():
   root = Tk()
   root.geometry("1150x750+0+0")

   def order():


      top = Toplevel();
      frame_inner1 = LabelFrame(top, text="", padx=50, pady=50)
      frame_inner1.pack(padx=50, pady=50)
      innerLabel = Label(frame_inner1, text="Thank you for Ordering")
      innerLabel.pack()

      def time(a,b):
         d=select()
         drop_table()

         if(d<1):
            s=a+b+5
         elif (d < 2):
            s = a+ b + 10
         elif (d < 3):
            s = a + b + 15
         elif (d < 4):
            s = a + b + 20
         elif (d < 5):
            s = a + b+ 25
         else:
            s=a+b+30
         return s


      s=time(10,5)
      myLabel1 = Label(frame_inner1, text="Your Food will be delivered in "+ str(s)+" minutes")
      myLabel1.pack()

   def calculate():

      MasalaChanna = e1.get()
      Paneer_Makhani_Biryani = e2.get()
      Aamras_Ki_Kadhi = e3.get()
      Dahi_Kebab = e4.get()
      MushroomKofta_inTomatoGravy = e5.get()
      Stuffed_Baby_Eggplant = e6.get()
      Gobhi_Aloo = e7.get()
      Mattar_Paneer = e8.get()

      Grilled_Chicken = e11.get()
      Tandoori_LambChops = e21.get()
      MuttonKorma = e31.get()
      PinaColada_PorkRibs = e41.get()
      Chicken_Pakoda = e51.get()
      KeemaSamosa_with_YoghurtDip = e61.get()
      Malabar_Fish_Biryani = e71.get()

      Lassi = e12.get()
      ButterMilk = e22.get()
      Choclate_Milkshake = e32.get()
      Oreo_Milkshake = e42.get()
      total=((int(MasalaChanna)*115)+(int(Paneer_Makhani_Biryani)*150)+(int(Aamras_Ki_Kadhi)*100)+(int(Dahi_Kebab)*150)+(int(MushroomKofta_inTomatoGravy)*175)
               +(int(Stuffed_Baby_Eggplant)*115)+(int(Gobhi_Aloo)*125)+(int(Mattar_Paneer)*115)+(int(Grilled_Chicken)*300)+
               (int(Tandoori_LambChops)*550)+(int(MuttonKorma)*500)+(int(PinaColada_PorkRibs)*650)+(int(Chicken_Pakoda)*175)+
               (int(KeemaSamosa_with_YoghurtDip)*200)+(int(Malabar_Fish_Biryani)*550)+(int(Lassi)*30)+(int(ButterMilk)*20)+
               (int(Choclate_Milkshake)*90)+(int(Oreo_Milkshake)*100))

      lbl=Label(root,text = total, font ="times 15")
      lbl.place(x=1000, y=310)

   lb0=Label(root, font=('arial', 40, 'bold'), background='#87918c', text= "\t\t\t\tfoogo\t\t\t\t")
   lb0.place(x=600,y=30,anchor="center")
   """lb0=Label(root,text="foogo",font="times 25 bold")
   lb0.place(x=700,y=20,anchor="center")
   """#-----------------Billing Section --------------------------
   v=StringVar(root,'0')
   lb24=Label(root,text="Vegetable Items",font="times 20 bold")
   lb24.place(x=70,y=70)
   lb31=Label(root,text="Masala Channa 115",font="times 15")
   lb31.place(x=20,y=130)
   e1=Entry(root)
   e1.insert(END,'0')
   e1.place(x=350,y=130)
   lb41=Label(root,text="Paneer Makhani Biryani 150",font="times 15")
   lb41.place(x=20,y=160)
   e2=Entry(root)
   e2.insert(END,'0')
   e2.place(x=350,y=160)
   lb51=Label(root,text="Aamras Ki Kadhi 100",font="times 15")
   lb51.place(x=20,y=190)
   e3=Entry(root)
   e3.insert(END,'0')
   e3.place(x=350,y=190)
   lb61=Label(root,text="DahiKebab 150",font="times 15")
   lb61.place(x=20,y=220)
   e4=Entry(root)
   e4.insert(END,'0')
   e4.place(x=350,y=220)
   lb71=Label(root,text="MushroomKofta 175",font="times 15")
   lb71.place(x=20,y=250)
   e5=Entry(root)
   e5.insert(END,'0')
   e5.place(x=350,y=250)
   lb81=Label(root,text="Stuffed Baby Eggplant 115",font="times 15")
   lb81.place(x=20,y=280)
   e6=Entry(root)
   e6.insert(END,'0')
   e6.place(x=350,y=280)
   lb91=Label(root,text="Gobhi Aloo 125",font="times 15")
   lb91.place(x=20,y=310)
   e7=Entry(root)
   e7.insert(END,'0')
   e7.place(x=350,y=310)
   lb101=Label(root,text="Mattar Paneer 115",font="times 15")
   lb101.place(x=20,y=340)
   e8=Entry(root)
   e8.insert(END,'0')
   e8.place(x=350,y=340)

   lb25=Label(root,text="NonVegetable Items",font="times 20 bold")
   lb25.place(x=70,y=390)
   lb121=Label(root,text="Grilled Chicken 300",font="times 15")
   lb121.place(x=20,y=450)
   e11=Entry(root)
   e11.place(x=350,y=450)
   lb131=Label(root,text="Tandoori LambChop 550",font="times 15")
   lb131.place(x=20,y=480)
   e21=Entry(root)
   e21.place(x=350,y=480)
   lb141=Label(root,text="MuttonKorma 500",font="times 15")
   lb141.place(x=20,y=510)
   e31=Entry(root)
   e31.place(x=350,y=510)
   lb151=Label(root,text="PinaColada PorkRibs 650",font="times 15")
   lb151.place(x=20,y=540)
   e41=Entry(root)
   e41.place(x=350,y=540)
   lb161=Label(root,text="Chicken Pakoda 175",font="times 15")
   lb161.place(x=20,y=570)
   e51=Entry(root)
   e51.place(x=350,y=570)
   lb171=Label(root,text="KeemaSamosa YoghurtDip 200",font="times 15")
   lb171.place(x=20,y=600)
   e61=Entry(root)
   e61.place(x=350,y=600)
   lb181=Label(root,text="Malabar Fish Biryani 550",font="times 15")
   lb181.place(x=20,y=630)
   e71=Entry(root)
   e71.place(x=350,y=630)

   e11.insert(END,'0')
   e21.insert(END,'0')
   e31.insert(END,'0')
   e41.insert(END,'0')
   e51.insert(END,'0')
   e61.insert(END,'0')
   e71.insert(END,'0')
   lb191=Label(root,text="Beverages",font="times 20 bold")
   lb191.place(x=650,y=70)
   lb201=Label(root,text="Lassi 30",font="times 15")
   lb201.place(x=650,y=120)
   e12=Entry(root)
   e12.place(x=900,y=130)
   lb211=Label(root,text="ButterMilk 20",font="times 15")
   lb211.place(x=650,y=150)
   e22=Entry(root)
   e22.place(x=900,y=160)
   lb22=Label(root,text="ChoclateMilkshake 90",font="times 15")
   lb22.place(x=650,y=180)
   e32=Entry(root)
   e32.place(x=900,y=190)
   lb23=Label(root,text="Oreo Milkshake 100",font="times 15")
   lb23.place(x=650,y=210)
   e42=Entry(root)
   e42.place(x=900,y=220)
   e12.insert(END,'0')
   e22.insert(END,'0')
   e32.insert(END,'0')
   e42.insert(END,'0')
   b2=Button(root,text='Bill',font="times 15",width=20,command=calculate)
   b2.place(x=650,y=300)
   checkout = Button(root, text='Order', font="times 15", width=20,command=order)
   checkout.place(x=650, y=370)

   root.mainloop()





