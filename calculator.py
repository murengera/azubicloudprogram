print("WELCOME TO CALCULATOR PROGRAM")
charge=50
tip=18
tax=7
total=0
# calculate 18% of tip
parcentageTip=float((charge*tip)/100)
# calculate 7% of tax
parcentageTax=float((charge*tax)/100)
sumParcentages=parcentageTax+parcentageTip
GrandTotal=charge+sumParcentages
print("Tip=",parcentageTip)
print("Sales tax=",parcentageTax)
print("Grand total",GrandTotal)





