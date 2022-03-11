def swapFile():
    file1=input("Enter File")
    file2=input("Enter File")
with open(file1,'r') as a:
    data_a = a.read()
with open(file2,'r') as b:
    data_b = a.read()
with open(file1,'w') as a:
    data_a = a.write(data_b)
with open(file1,'w') as b:
    data_b = a.write(data_a)

