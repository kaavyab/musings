money=500
table=260
phone=250
total=table+phone
can_afford=total>=money
if can_afford:
	message="you can buy"
else:
	message="cant buy"
print(message)