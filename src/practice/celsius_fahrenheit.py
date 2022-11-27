a=input("Celsius to Fahrenheit Enter'c' and Fahrenheit to Celsius Enter'f'")


if a=="c":
    d=float(input("Temparatue in Celsius:"))
    b=d*1.8+32
    print("Temparature in Fahrenheit:",b)
if a=="f":
    y=float(input("Temparatue in Fahrenheit:"))
    x=(y-32)/1.8
    print("Temparature in Fahrenheit:",x)
