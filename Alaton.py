alaton_nohour=float(input("Enter Hours: "))
alaton_choice= int(input("1] Janitor 2] Clerk 3] Cashier 4] Manager"))
alaton_position=""
alaton_salary=0

if alaton_choice==1:
   alaton_position= " Janitor"
   alaton_salary= 18000

elif alaton_choice==2:
    alaton_position== "Clerk"
    alaton_salary== 22

elif alaton_choice==3:
    alaton_position= " Cashier "
    alaton_salary= 24000

elif alaton_choice==4:
    alaton_position= " Manager "
    alaton_salary= 40000

else:
    print("invalid")
    alaton_halfmonth= alaton_salary/2
    alaton_rateperhour=alaton_halfmonth/88
    alaton_absenceded=0
    alaton_netsalary=0

if alaton_nohour >=88:
   alaton_extrahours=alaton_nohour-88
   alaton_otrate=alaton_rateperhour*1.25
   alaton_overtimepay=alaton_otrate*alaton_extrahours
   alaton_netsalary = alaton_halfmonth+alaton_overtimepay
   print("overtimepay: ", alaton_overtimepay)

elif alaton_nohour <80:
    alaton_absenceded=alaton_rateperhour*1.10*alaton_absenceded
    alaton_netsalary=alaton_halfmonth-alaton_absenceded
    print(f"absence deduction: {alaton_absenceded:,.2f}")

else:
    print("invalid")
    print(f"Net Salary: {alaton_netsalary:,.2f}")
    print("Position:", alaton_position)





