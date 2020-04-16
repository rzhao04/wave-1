price = float
price = input ('what is price: ')
finalPrice = float
finalPrice = price * 100
cash = float
cash = input ('what is cash: ')
purchase = float
purchase = cash * 100
finalPrice < purchase
change = float
change = purchase - finalPrice
pennies = 1
nickels = 5
dimes = 10
quarters = 25
loonies = 100
toonies = 200
nT = int (change / toonies)
aChange = change - nT * toonies
print ('# of toonies', nT)
nL = int (aChange / loonies)
bChange = aChange - nL * loonies
print ('# of loonies', nL)
nQ = int (bChange / quarters)
cChange = bChange - nQ * quarters
print ('# of quarters', nQ)
nD = int (cChange / dimes)
dChange = cChange - nD * dimes
print ('# of dimes', nD)
nN = int (dChange / nickels)
eChange = dChange - nN * nickels
print ('# of nickels', nN)
nP = eChange / pennies
print ('# of pennies', nP)