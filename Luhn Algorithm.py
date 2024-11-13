def luhn_algorithm(number): 
    num_str=str(number)
    total_sum=0  
    for i in range(len(num_str)):
            digit=int(num_str[-(i + 1)])  
            if i%2==1:
                digit=digit*2
                if digit>9:
                    digit=digit-10
                    total_sum+=digit+1
                else:
                    total_sum+=digit
            else:
                total_sum=total_sum+digit
    return total_sum
number = 79927398713
 
a=luhn_algorithm(number)
if a%10==0:
    print(number,'is valid')
else:
    print(number,'not valid')

