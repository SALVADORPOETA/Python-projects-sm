l1 = int(input("Enter first limit: "))
l2 = int(input("Enter second limit: "))

total = l2 - l1
n = int(input("Enter number of rectangles: "))
e = int(input("Enter extra sum: "))
part = total//n
print(part)
print("\n")

for i in range(l1, l2+1, part):
	print(i+e)

print("\n")
print(i+part)