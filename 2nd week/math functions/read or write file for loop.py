#file writing
f= open("demo2.txt",'w')
for i in range(100):
  f.write (f'this is line {i+1}\n')
f.close()
#file reading
f= open("demo2.txt",'r')
txt=f.read()
print(txt)
f.close()
#file reading
f= open("demo2.txt",'a')
f.write(f'this is line {i}')
f.close()
#file reading
f= open("demo2.txt",'r')
msg=f.read()
print(msg)
f.close()

