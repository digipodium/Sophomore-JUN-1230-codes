# Wap to calculate the SI based on following conditions
# if the principal > 50000, then roi would be 9.5
# if the principal > 40000 and <=50000 then roi would be 8.4
# if the principal > 25000 and <=40000 then roi would be 6.1

p = float(input("enter the principal amount: "))
t = int(input("How much time in years: "))

# conditions with calculate
if p > 50000:
    r = 9.5
elif p > 40000:
    r = 8.4
elif p > 25000:
    r = 6.1
else:
    print("no interest in your money")
    r = 0
si = p * r * t / 100
print(f'Simple Interest is {si} based on {r}')
