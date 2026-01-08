temperature=int(input("Enter temperature: "))
type=input("C/F : ").upper()

if type == 'C' :
    f = (temperature * 9/5) + 32
    print(f)
elif type =='F':
    c = (temperature - 32) * 5/9
    print(c)
else:
    print("wrong input")