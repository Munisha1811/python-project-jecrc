print("Hello!")

print("I am your assistant I can help you \n")

print("It is a program which is based on unit conversion\n")

print("It includes:\n1. Length  2. Temperature  3. Mass  4. Data  5. Speed  6. Time\n")


print("1. Length includes: ")

print("i. Millimeters  ii. Inches   iii. Centimeters  iv. Meters  v. Kilometers  vi. Feets  vii. Yards  viii. Miles \n")


print("2. Temperature includes: ")

print("i. Celsius  ii. Fahrenheit  iii. Kelvin")


print("3. Mass includes: ")

print("i. Tons  ii. Kilograms  iii. Grams \n")


print("4. Speed includes: ")

print("i. Meters per second  ii. Kilometers per hour  iii. Miles per hour \n")


print("5. Time includes: ")

print("i. Milliseconds  ii. Seconds  iii. Minutes  iv. Hours  v. Days  vi. Weeks \n")


a= input("Enter Quantity:")

b= input("Which Unit:")


if a=="Length":
    if b=="Inches":
        import tkinter as tk
        window = tk.Tk()
        def mill():
            n1= float(p.get())
            n2= n1*25.4
            q.insert(0, n2)
        def m():
            n1= float(p.get())
            n2= n1*0.0254
            q.insert(0, n2)
        def cm():
            n1= float(p.get())
            n2= n1*2.54
            q.insert(0, n2)
        def km():
            n1= float(p.get())
            n2= n1*.0000254
            q.insert(0, n2)
        def feet():
            n1= float(p.get())
            n2= n1*.0833333
            q.insert(0, n2)
        def yards():
            n1= float(p.get())
            n2= n1*0.277777
            q.insert(0, n2)
        def miles():
            n1= float(p.get())
            n2= n1*0.0001893939
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text="Inches").grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0, column=1)
        tk.Label(window, text="ANSWER").grid(row=1, column=0)
        q = tk.Entry()
        q.grid(row=1, column=1)

        tk.Button(window, text="MILLMETER", command=mill).grid(row=2, column=0)
        tk.Button(window, text="CENTIMETER", command=cm).grid(row=2, column=1)
        tk.Button(window, text="KILOMETER", command=km).grid(row=2, column=2)
        tk.Button(window, text="METER", command=m).grid(row=2, column=3)
        tk.Button(window, text="FEETS", command=feet).grid(row=3, column=0)
        tk.Button(window, text="YARDS", command=yards).grid(row=3, column=1)
        tk.Button(window, text="MILES", command=miles).grid(row=3, column=2)
        tk.Button(window, text="CLEAR", command=clc).grid(row=4, column=0)
        window.mainloop()
        
    if b=="Millimeters":
        import tkinter as tk
        window = tk.Tk()
        def cm():
            n1= float(p.get())
            n2= n1*.1
            q.insert(0, n2)
        def m():
            n1= float(p.get())
            n2= n1*.001
            q.insert(0, n2)
        def km():
            n1= float(p.get())
            n2= n1*.000001
            q.insert(0, n2)
        def inches():
            n1= float(p.get())
            n2= n1*0.0393700
            q.insert(0, n2)
        def feet():
            n1= float(p.get())
            n2= n1*0.0032808399
            q.insert(0, n2)
        def yards():
            n1= float(p.get())
            n2= n1*0.00109361
            q.insert(0, n2)
        def miles():
            n1= float(p.get())
            n2= n1*(6.21*(10**-7))
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text="MILLIMETER").grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0, column=1)

        tk.Label(window, text="ANSWER").grid(row=1, column=0)
        q = tk.Entry()
        q.grid(row=1, column=1)

        tk.Button(window, text="METERS", command=m).grid(row=2, column=0)
        tk.Button(window, text="CENTIMETER", command=cm).grid(row=2, column=1)
        tk.Button(window, text="KILOMETER", command=km).grid(row=2, column=2)
        tk.Button(window, text="FEETS", command=feet).grid(row=3, column=0)
        tk.Button(window, text="YARDS", command=yards).grid(row=3, column=1)
        tk.Button(window, text="MILES", command=miles).grid(row=3, column=2)
        tk.Button(window, text="INCHES", command=inches).grid(row=3, column=3)
        tk.Button(window, text="CLEAR", command=clc).grid(row=4, column=1)
        window.mainloop()
        
    if b=="Centimeters":
        import tkinter as tk
        window = tk.Tk()
        def m():
            n1= float(p.get())
            n2= n1*.01
            q.insert(0, n2)
        def milli():
            n1= float(p.get())
            n2= n1*10
            q.insert(0, n2)
        def km():
            n1= float(p.get())
            n2= n1*.00001
            q.insert(0, n2)
        def inches():
            n1= float(p.get())
            n2= n1*0.3937007874
            q.insert(0, n2)
        def feet():
            n1= float(p.get())
            n2= n1*0.032808399
            q.insert(0, n2)
        def yards():
            n1= float(p.get())
            n2= n1*0.0109361
            q.insert(0, n2)
        def miles():
            n1= float(p.get())
            n2= n1*.0000062137
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text="CENTIMETER").grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0, column=1)

        tk.Label(window, text="ANSWER").grid(row=1, column=0)
        q = tk.Entry()
        q.grid(row=1, column=1)

        tk.Button(window, text="METERS", command=m).grid(row=2, column=0)
        tk.Button(window, text="MILLIMETERS", command=milli).grid(row=2, column=1)
        tk.Button(window, text="KILOMETER", command=km).grid(row=2, column=2)
        tk.Button(window, text="FEETS", command=feet).grid(row=3, column=0)
        tk.Button(window, text="YARDS", command=yards).grid(row=3, column=1)
        tk.Button(window, text="MILES", command=miles).grid(row=3, column=2)
        tk.Button(window, text="INCHES", command=inches).grid(row=3, column=3)
        tk.Button(window, text="CLEAR", command=clc).grid(row=4, column=1)
        window.mainloop()
        
    if b=="Meters":
        import tkinter as tk
        window = tk.Tk()
        def milli():
            n1= float(p.get())
            n2= n1*1000
            q.insert(0, n2)
        def cm():
            n1= float(p.get())
            n2= n1*100
            q.insert(0, n2)
        def km():
            n1= float(p.get())
            n2= n1*.001
            q.insert(0, n2)
        def inches():
            n1= float(p.get())
            n2= n1*39.37007874
            q.insert(0, n2)
        def feet():
            n1= float(p.get())
            n2= n1*3.2808399
            q.insert(0, n2)
        def yards():
            n1= float(p.get())
            n2= n1*1.093612983
            q.insert(0, n2)
        def miles():
            n1= float(p.get())
            n2= n1*.0006213712
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text="METER").grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0, column=1)

        tk.Label(window, text="ANSWER").grid(row=1, column=0)
        q = tk.Entry()
        q.grid(row=1, column=1)

        tk.Button(window, text="CENTIMETERS", command=cm).grid(row=2, column=0)
        tk.Button(window, text="MILLIMETERS", command=milli).grid(row=2, column=1)
        tk.Button(window, text="KILOMETER", command=km).grid(row=2, column=2)
        tk.Button(window, text="FEETS", command=feet).grid(row=3, column=0)
        tk.Button(window, text="YARDS", command=yards).grid(row=3, column=1)
        tk.Button(window, text="MILES", command=miles).grid(row=3, column=2)
        tk.Button(window, text="INCHES", command=inches).grid(row=3, column=3)
        tk.Button(window, text="CLEAR", command=clc).grid(row=4, column=1)
        window.mainloop()
        
    if b=="Kilometers":
        import tkinter as tk
        window = tk.Tk()
        def milli():
            n1= float(p.get())
            n2= n1*1000000
            q.insert(0, n2)
        def cm():
            n1= float(p.get())
            n2= n1*100000
            q.insert(0, n2)
        def m():
            n1= float(p.get())
            n2= n1*.1000
            q.insert(0, n2)
        def inches():
            n1= float(p.get())
            n2= n1*39370.07874
            q.insert(0, n2)
        def feet():
            n1= float(p.get())
            n2= n1*3280.8399
            q.insert(0, n2)
        def yards():
            n1= float(p.get())
            n2= n1*1093.612983
            q.insert(0, n2)
        def miles():
            n1= float(p.get())
            n2= n1*.6213712
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text="KILOMETER").grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0, column=1)

        tk.Label(window, text="ANSWER").grid(row=1, column=0)
        q = tk.Entry()
        q.grid(row=1, column=1)

        tk.Button(window, text="CENTIMETERS", command=cm).grid(row=2, column=0)
        tk.Button(window, text="MILLIMETERS", command=milli).grid(row=2, column=1)
        tk.Button(window, text="METER", command=m).grid(row=2, column=2)
        tk.Button(window, text="FEETS", command=feet).grid(row=3, column=0)
        tk.Button(window, text="YARDS", command=yards).grid(row=3, column=1)
        tk.Button(window, text="MILES", command=miles).grid(row=3, column=2)
        tk.Button(window, text="INCHES", command=inches).grid(row=3, column=3)
        tk.Button(window, text="CLEAR", command=clc).grid(row=4, column=1)
        window.mainloop()
        
    if b=="Feet":
        import tkinter as tk
        window = tk.Tk()
        def milli():
            n1= float(p.get())
            n2= n1*304.8
            q.insert(0, n2)
        def cm():
            n1= float(p.get())
            n2= n1*30.48
            q.insert(0, n2)
        def m():
            n1= float(p.get())
            n2= n1*.3048
            q.insert(0, n2)
        def inches():
            n1= float(p.get())
            n2= n1*12
            q.insert(0, n2)
        def km():
            n1= float(p.get())
            n2= n1*0.0003048
            q.insert(0, n2)
        def yards():
            n1= float(p.get())
            n2= n1*.333333
            q.insert(0, n2)
        def miles():
            n1= float(p.get())
            n2= n1*.0001893939
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text="FEETS").grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0, column=1)

        tk.Label(window, text="ANSWER").grid(row=1, column=0)
        q = tk.Entry()
        q.grid(row=1, column=1)

        tk.Button(window, text="CENTIMETERS", command=cm).grid(row=2, column=0)
        tk.Button(window, text="MILLIMETERS", command=milli).grid(row=2, column=1)
        tk.Button(window, text="METER", command=m).grid(row=2, column=2)
        tk.Button(window, text="KILOMETERS", command=km).grid(row=3, column=0)
        tk.Button(window, text="YARDS", command=yards).grid(row=3, column=1)
        tk.Button(window, text="MILES", command=miles).grid(row=3, column=2)
        tk.Button(window, text="INCHES", command=inches).grid(row=3, column=3)
        tk.Button(window, text="CLEAR", command=clc).grid(row=4, column=1)
        window.mainloop()
        
    if b=="Yards":
        import tkinter as tk
        window = tk.Tk()
        def milli():
            n1= float(p.get())
            n2= n1*914.4
            q.insert(0, n2)
        def cm():
            n1= float(p.get())
            n2= n1*91.44
            q.insert(0, n2)
        def m():
            n1= float(p.get())
            n2= n1*.9144
            q.insert(0, n2)
        def inches():
            n1= float(p.get())
            n2= n1*36
            q.insert(0, n2)
        def km():
            n1= float(p.get())
            n2= n1*0.0009144
            q.insert(0, n2)
        def feet():
            n1= float(p.get())
            n2= n1*3
            q.insert(0, n2)
        def miles():
            n1= float(p.get())
            n2= n1*.0005681818
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text="YARDS").grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0, column=1)

        tk.Label(window, text="ANSWER").grid(row=1, column=0)
        q = tk.Entry()
        q.grid(row=1, column=1)

        tk.Button(window, text="CENTIMETERS", command=cm).grid(row=2, column=0)
        tk.Button(window, text="MILLIMETERS", command=milli).grid(row=2, column=1)
        tk.Button(window, text="METER", command=m).grid(row=2, column=2)
        tk.Button(window, text="KILOMETERS", command=km).grid(row=3, column=0)
        tk.Button(window, text="FEET", command=feet).grid(row=3, column=1)
        tk.Button(window, text="MILES", command=miles).grid(row=3, column=2)
        tk.Button(window, text="INCHES", command=inches).grid(row=3, column=3)
        tk.Button(window, text="CLEAR", command=clc).grid(row=4, column=1)
        window.mainloop()
        
    if b=="Miles":
        import tkinter as tk
        window = tk.Tk()
        def milli():
            n1= float(p.get())
            n2= n1*1609344
            q.insert(0, n2)
        def cm():
            n1= float(p.get())
            n2= n1*160934.4
            q.insert(0, n2)
        def m():
            n1= float(p.get())
            n2= n1*1609.344
            q.insert(0, n2)
        def inches():
            n1= float(p.get())
            n2= n1*63360
            q.insert(0, n2)
        def km():
            n1= float(p.get())
            n2= n1*1.609344
            q.insert(0, n2)
        def feet():
            n1= float(p.get())
            n2= n1*5280
            q.insert(0, n2)
        def yard():
            n1= float(p.get())
            n2= n1*.1760
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text="MILES").grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0, column=1)

        tk.Label(window, text="ANSWER").grid(row=1, column=0)
        q = tk.Entry()
        q.grid(row=1, column=1)

        tk.Button(window, text="CENTIMETERS", command=cm).grid(row=2, column=0)
        tk.Button(window, text="MILLIMETERS", command=milli).grid(row=2, column=1)
        tk.Button(window, text="METER", command=m).grid(row=2, column=2)
        tk.Button(window, text="KILOMETERS", command=km).grid(row=3, column=0)
        tk.Button(window, text="FEET", command=feet).grid(row=3, column=1)
        tk.Button(window, text="YARD", command=yard).grid(row=3, column=2)
        tk.Button(window, text="INCHES", command=inches).grid(row=3, column=3)
        tk.Button(window, text="CLEAR", command=clc).grid(row=4, column=1)
        window.mainloop()
        
if a=="Temperature":
    if b=="Celsius":
        import tkinter as tk
        window = tk.Tk()
        def feh():
            n1= float(p.get())
            n2=n1*(9/5) + 32
            q.insert(0, n2)
        def kel():
            n1= float(p.get())
            n2=n1+273.15
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='CELSIUS').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='KEL', command=kel).grid(row=2,column=0)
        tk.Button(window, text='FEH', command=feh).grid(row=2,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=2,column=2)
        window.mainloop()
        
    if b=="Fahrenheit":
        import tkinter as tk
        window = tk.Tk()
        def cel():
            n1= float(p.get())
            n2=(n1-32)*(5/9)
            q.insert(0, n2)
        def kel():
            n1= float(p.get())
            n2=((n1-32)*(5/9))+273.15
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='FAHRENHEIT').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='KEL', command=kel).grid(row=2,column=0)
        tk.Button(window, text='CEL', command=cel).grid(row=2,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=2,column=2)
        window.mainloop()
        
    if b=="Kelvin":
        import tkinter as tk
        window = tk.Tk()
        def cel():
            n1= float(p.get())
            n2=n1-273.15
            q.insert(0, n2)
        def feh():
            n1= float(p.get())
            n2=((n1-273.15)*(9/5))+32
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='KELVIN').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='FEH', command=feh).grid(row=2,column=0)
        tk.Button(window, text='CEL', command=cel).grid(row=2,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=2,column=2)
        window.mainloop()


if a=="Mass":
    if b=="Tons":
        import tkinter as tk
        window = tk.Tk()
        def kg():
            n1= float(p.get())
            n2=n1*1000
            q.insert(0, n2)
        def gm():
            n1= float(p.get())
            n2=n1*1000000
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='TONS').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='KILOGRAMS', command=kg).grid(row=2,column=0)
        tk.Button(window, text='GRAMS', command=gm).grid(row=2,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=2,column=2)
        window.mainloop()
        
    if b=="Kilograms":
        import tkinter as tk
        window = tk.Tk()
        def tons():
            n1= float(p.get())
            n2=n1*0.001
            q.insert(0, n2)
        def gm():
            n1= float(p.get())
            n2=n1*1000
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='KILOGRAMS').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='TONS', command=tons).grid(row=2,column=0)
        tk.Button(window, text='GRAMS', command=gm).grid(row=2,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=2,column=2)
        window.mainloop()
        
    if b=="Grams":
        import tkinter as tk
        window = tk.Tk()
        def tons():
            n1= float(p.get())
            n2=n1*0.000001
            q.insert(0, n2)
        def kg():
            n1= float(p.get())
            n2=n1*.001
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='GRAMS').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='TONS', command=tons).grid(row=2,column=0)
        tk.Button(window, text='KILOGRAMS', command=kg).grid(row=2,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=2,column=2)
        window.mainloop()

if a=="Speed":
    if b=="Meters per second":
        import tkinter as tk

        window = tk.Tk()
        def kmh():
            n1= float(p.get())
            n2=n1*3.6
            q.insert(0, n2)
        def mih():
            n1= float(p.get())
            n2=n1*2.2369362921
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='M/S').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='KM/H', command=kmh).grid(row=2,column=0)
        tk.Button(window, text='MI/H', command=mih).grid(row=2,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=3,column=1)
        window.mainloop()
        
    if b=="Kilometers per hour":
        import tkinter as tk

        window = tk.Tk()
        def ms():
            n1= float(p.get())
            n2=n1*0.2777777778
            q.insert(0, n2)
        def mih():
            n1= float(p.get())
            n2=n1*0.6213711922
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='KM/H').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='M/S', command=ms).grid(row=2,column=0)
        tk.Button(window, text='MI/H', command=mih).grid(row=2,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=3,column=1)
        window.mainloop()
        
    if b=="Miles per hour":
        import tkinter as tk

        window = tk.Tk()
        def ms():
            n1= float(p.get())
            n2=n1*0.44704
            q.insert(0, n2)
        def kmh():
            n1= float(p.get())
            n2=n1*1.609344
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='MI/H').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='KM/H', command=kmh).grid(row=2,column=0)
        tk.Button(window, text='M/S', command=mih).grid(row=2,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=3,column=1)
        window.mainloop()
if a=="Time":
    if b=="Milliseconds":
        import tkinter as tk

        window = tk.Tk()
        def s():
            n1= float(p.get())
            n2=n1*0.001
            q.insert(0, n2)
        def mi():
            n1= float(p.get())
            n2=n1*0.0000166667
            q.insert(0, n2)
        def hr():
            n1= float(p.get())
            n2=n1*(2.77777778*(10**-7))
            q.insert(0, n2)
        def days():
            n1= float(p.get())
            n2=n1*(1.15740741*(10**-8))
            q.insert(0, n2)
        def week():
            n1= float(p.get())
            n2=n1*(1.65343915*(10**-9))
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='MILLISECONDS').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='SECONDS', command=s).grid(row=2,column=0)
        tk.Button(window, text='MINUTES', command=mi).grid(row=2,column=1)
        tk.Button(window, text='HOURS', command=hr).grid(row=2,column=2)
        tk.Button(window, text='DAYS', command=days).grid(row=3,column=0)
        tk.Button(window, text='WEEK', command=week).grid(row=3,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=3,column=2)
        window.mainloop()
        
    if b=="Seconds":
        import tkinter as tk

        window = tk.Tk()
        def mil():
            n1= float(p.get())
            n2=n1*1000
            q.insert(0, n2)
        def mi():
            n1= float(p.get())
            n2=n1*0.0166666667
            q.insert(0, n2)
        def hr():
            n1= float(p.get())
            n2=n1*0.0002777778
            q.insert(0, n2)
        def days():
            n1= float(p.get())
            n2=n1*.0000115741
            q.insert(0, n2)
        def week():
            n1= float(p.get())
            n2=n1*0.0000016534
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='SECONDS').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='MILLISECONDS', command=mil).grid(row=2,column=0)
        tk.Button(window, text='MINUTES', command=mi).grid(row=2,column=1)
        tk.Button(window, text='HOURS', command=hr).grid(row=2,column=2)
        tk.Button(window, text='DAYS', command=days).grid(row=3,column=0)
        tk.Button(window, text='WEEK', command=week).grid(row=3,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=3,column=2)
        window.mainloop()
        
    if b=="Minutes":
        import tkinter as tk

        window = tk.Tk()
        def mil():
            n1= float(p.get())
            n2=n1*60000
            q.insert(0, n2)
        def s():
            n1= float(p.get())
            n2=n1*60
            q.insert(0, n2)
        def hr():
            n1= float(p.get())
            n2=n1*0.0166666667
            q.insert(0, n2)
        def days():
            n1= float(p.get())
            n2=n1*.0006944444
            q.insert(0, n2)
        def week():
            n1= float(p.get())
            n2=n1*0.0000992063
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='MINUTES').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='MILLISECONDS', command=mil).grid(row=2,column=0)
        tk.Button(window, text='SECOND', command=s).grid(row=2,column=1)
        tk.Button(window, text='HOURS', command=hr).grid(row=2,column=2)
        tk.Button(window, text='DAYS', command=days).grid(row=3,column=0)
        tk.Button(window, text='WEEK', command=week).grid(row=3,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=3,column=2)
        window.mainloop()
        
    if b=="Hours":
        import tkinter as tk

        window = tk.Tk()
        def mil():
            n1= float(p.get())
            n2=n1*3600000
            q.insert(0, n2)
        def s():
            n1= float(p.get())
            n2=n1*3600
            q.insert(0, n2)
        def mi():
            n1= float(p.get())
            n2=n1*60
            q.insert(0, n2)
        def days():
            n1= float(p.get())
            n2=n1*.0416666667
            q.insert(0, n2)
        def week():
            n1= float(p.get())
            n2=n1*0.005952381
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='HOURS').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='MILLISECONDS', command=mil).grid(row=2,column=0)
        tk.Button(window, text='SECOND', command=s).grid(row=2,column=1)
        tk.Button(window, text='MINUTES', command=mi).grid(row=2,column=2)
        tk.Button(window, text='DAYS', command=days).grid(row=3,column=0)
        tk.Button(window, text='WEEK', command=week).grid(row=3,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=3,column=2)
        window.mainloop()
        
    if b=="Days":
        import tkinter as tk

        window = tk.Tk()
        def mil():
            n1= float(p.get())
            n2=n1*86400000
            q.insert(0, n2)
        def s():
            n1= float(p.get())
            n2=n1*86400
            q.insert(0, n2)
        def mi():
            n1= float(p.get())
            n2=n1*1440
            q.insert(0, n2)
        def hr():
            n1= float(p.get())
            n2=n1*24
            q.insert(0, n2)
        def week():
            n1= float(p.get())
            n2=n1*0.1428571429
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='DAYS').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='MILLISECONDS', command=mil).grid(row=2,column=0)
        tk.Button(window, text='SECOND', command=s).grid(row=2,column=1)
        tk.Button(window, text='MINUTES', command=mi).grid(row=2,column=2)
        tk.Button(window, text='HOURS', command=hr).grid(row=3,column=0)
        tk.Button(window, text='WEEK', command=week).grid(row=3,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=3,column=2)
        window.mainloop()
        
    if b=="Weeks":
        import tkinter as tk

        window = tk.Tk()
        def mil():
            n1= float(p.get())
            n2=n1*604800000
            q.insert(0, n2)
        def s():
            n1= float(p.get())
            n2=n1*604800
            q.insert(0, n2)
        def mi():
            n1= float(p.get())
            n2=n1*10080
            q.insert(0, n2)
        def hr():
            n1= float(p.get())
            n2=n1*168
            q.insert(0, n2)
        def week():
            n1= float(p.get())
            n2=n1*7
            q.insert(0, n2)
        def clc():
            p.delete(0, tk.END)
            q.delete(0, tk.END)
        tk.Label(window, text='WEEKS').grid(row=0,column=0)
        p = tk.Entry()
        p.grid(row=0,column=1)
        tk.Label(window, text='ANSWER:').grid(row=1,column=0)
        q = tk.Entry()
        q.grid(row=1,column=1)

        tk.Button(window, text='MILLISECONDS', command=mil).grid(row=2,column=0)
        tk.Button(window, text='SECOND', command=s).grid(row=2,column=1)
        tk.Button(window, text='MINUTES', command=mi).grid(row=2,column=2)
        tk.Button(window, text='HOURS', command=hr).grid(row=3,column=0)
        tk.Button(window, text='DAYS', command=days).grid(row=3,column=1)
        tk.Button(window, text='CLEAR', command=clc).grid(row=3,column=2)
        window.mainloop()




        
