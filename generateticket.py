#lex_auth_012693763253788672132
import random
def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    n=no_of_passengers
    #Write your logic here
    i=101
    while no_of_passengers>0:
        t=airline+":"+source[:3]+":"+destination[:3]+":"+str(i)
        ticket_number_list.append(t)
        i=i+1
        no_of_passengers-=1
    #Use the below return statement wherever applicable
    if n>=5:
        return ticket_number_list[-5:]
    else:
         return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",6))