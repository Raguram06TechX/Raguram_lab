#creater: k.Raguram
print("\t\t\tELECTRICITY BILL CALCULATOR \n")
#get the input from the user
unit=int(input("enter the unit(eg:420):"))
#get the input from the user for commercial or non-commerical
typee=input("Enter Connection Type (e.g: commerical or non-commerical): ")
#check the input for commmercial or non-commercial type
if(typee == "non-commerical"):
    if(unit <= 200):
        print("Free Electricity . No charge !!")
    elif(unit<=500):
        print ("You are with in 500 so the 200 units are Free! enjoy It !")
        a=unit-200
        amount1=a*4
        print("Total Bill:",amount1)    
    elif(unit<=2000):
        amount2=unit*8
        print("Total Bill:",amount2) 
    elif(unit>2000):
        amount3=unit*10
        print("Total Bill:",amount3) 
   
elif(typee == "commerical"):
    if(unit<=500):
        amount1=unit*6
        print("Total Bill:",amount1)    
        
    elif(unit<=1000):
        amount2=unit*9
        print("Total Bill:",amount2)    
    elif(unit<=5000):
        amount3=unit*12
        print("Total Bill:",amount3) 
    elif(unit>5000):
        amount4=unit*15
        print("Total Bill:",amount4)
    
else:
    print("type error!! please enter the type properly ")
