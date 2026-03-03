#file writing
f= open("demo3.txt",'w')
f.write (f'this is line 0')
f.close()
for i in range(100):
#file reading
    f= open("demo3.txt",'a')
    f.write(f'\nthis is line {i+1}')
    f.close()
#file reading
f= open("demo3.txt",'r')
msg=f.read()
print(msg)
f.close()

