card_no ="5610591081018250"
number = list(card_no)
odd_sum=0
double_list=[]
for (idx, val)  in enumerate(number):
    if idx % 2 != 0:
       odd_sum += int(val)    
    else:   
        double_list.append(int(val)*2)
double_string =""    
for x in double_list:
    double_string += str(x)
#converting a string to a list 
double_list = list(double_string)    
even_sum=0
for x in double_list:
    even_sum += int(x)
net_sum = odd_sum + even_sum  
if net_sum % 10 == 0:
    print("Valid card")
else:   
    print("Invalid card")   