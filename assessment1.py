Question 1 - 

Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 

Book - Introduction to Python Programming : Rs 499.00

Book - Python Libraries Cookbook : Rs. 855.00

Book - Data Science in Python : Rs. 645.00


Taxes and additional charges are described as details - 

GST : 12%

Delivery Charges : Rs. 250.00


book1=int(input("no. of books of Introduction to python programming: "))
book2=int(input("no. of books of python libraries cookbook: "))
book3=int(input("no. of books of Data Science in Python: "))
book1_price=book1*499.00
book2_price=book2*855.00
book3_price=book3*645.00
tot_price=book1_price+book2_price+book3_price
gst=tot_price*12/100
delivery=250
invoice_amount=tot_price+gst+delivery
print("Total amount:",tot_price)
print("GST(12%): ",gst)
print("Total invoice_amount: ",invoice_amount)


Question 2 - 

Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.

                                  

Input : string1 = "India"

Output : uniqueLetters = i,n,d,a


Input : string1 = "Dedication"

Output : uniqueLetters = d,e,i,c,a,t,o,n



str=input("Enter a string: ")
lowerstr=str.lower()
empstr=""
for i in lowerstr:
    if i not in empstr:
        empstr=empstr+i
print("UniqueLetters: ",",".join(empstr))
