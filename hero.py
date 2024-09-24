m1=int(input("enter markas: "))
m2=int(input("enter markas: "))
m3=int(input("enter markas: "))
total=m1+m2+m3
per=total/3
if per>=65:
    print(per,"first division:")
elif per>=50:
     print(per,"Secand division:")
elif per>=33:
     print(per,"thard division")
else:
    print("fail")
    