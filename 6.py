dic1={1:10,
      2:20,
      3:30,
      4:40,
      5:50,
      6:60}
n=int(input("enter the key:-"))
if n in dic1.keys():
    print("exist")
else:
    print("not exist")