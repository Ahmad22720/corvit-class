weight=float(input('enter a value of weight in kgs:'))
height=float(input('enter a value of height in inches:'))
h_=height*0.3048
bmi = weight / (h_ ** 2)
print('your BMI is:',bmi)
if(bmi<18.5):
    print('you are undrweight:')
elif(18.5<bmi<25):
    print('you are undrweight:')
elif(25<bmi<30):
    print('you are overweight:')
else:
    print('you are obese:')