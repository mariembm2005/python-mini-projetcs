ch = input("enter username  : ")
if(len(ch)>12):
    print("no more than 12 caracters!!!!!!!")
elif(ch.count(" ")>0):
    print("no space contained!!!!!")
elif(ch.isalpha()==False):
    print("no digits contained!!!!!")
else:
    print(f"'{ch}' is valid")