#INPUT
#input we need from the user
#total rent
#total food ordered for snacking
#electricity units spend
#charge per unit
#person living in room
#OUTPUT
#total amount you have to pat is

rent=int(input("enter your room rent="))
food=int(input("enter the amount of food ordered="))
electricity_units=int(input("enter the electricity units spent="))
charge_per_unit=int(input("enter the charge per unit="))
persons=int(input("enter the numbers of persons living in room="))

total_amount_bills=electricity_units*charge_per_unit
output=(food+rent+total_amount_bills)/persons
print("each person will pay=",output)




