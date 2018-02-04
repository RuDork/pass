#!/usr/bin/python3
import sys
def aftertax():
#    salary = int(sys.argv[1])
    social = salary * 0.165
    taxsalary = salary - social - 3500
    if taxsalary < 1500:
        tax = taxsalary * 0.03
    elif 1500 <= taxsalary <= 4500:
        tax = taxsalary * 0.1 - 105
    elif 4500 <= taxsalary <= 9000:
        tax = taxsalary * 0.2 - 555
    elif 9000 <= taxsalary <= 35000:
        tax = taxsalary * 0.25 - 1005
    elif 35000 <= taxsalary <= 55000:
        tax = taxsalary * 0.3 - 2755
    elif 55000 <= taxsalary <= 80000:
        tax = taxsalary * 0.35 - 5505
    else:
        tax = taxsalary * 0.45 - 13505
    aftertax = format(salary-social-tax,'.2f') 
    return aftertax
#print(aftertax())
for people in sys.argv[1:]:
    man = people.split(':')
    try:
        salary = int(man[1])
    except:
        print("Parameter Error")
    print(man[0],end='')
    print(':',end='')
    print(aftertax())
#    manid_salary = {man[0]:aftertax()}
#    print(manid_salary)
