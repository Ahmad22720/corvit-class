#file writing
f= open("demo",'w')
f.write(" this is line 2")
f.write("\n this is first program")
f.write("\n this is line 4")
f.close()
#file reading
f= open("demo",'r')
txt=f.read()
print(txt)
f.close()