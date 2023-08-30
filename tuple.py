address=("kigali","nairobi",2345,3,"kenya")
country=("usa","burundi",address)
print(address)
print(address[0])
print(country)

# firstname=input("enter your first name")
# lastname=input("enter your last name")
# fullname=(firstname,lastname)
# print(fullname)

print(address[0:2])
print(len(address))
print(address.count(1))
for item in address:
    print(item)