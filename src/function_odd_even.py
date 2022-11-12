def odd_even(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
a=int(input("Thr number:"))
x=odd_even(a)
print(x)