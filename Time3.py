def test(n):
  iteration = 0
  for i in range(0, n):
    for j in range(0, n):
      print("*", end = " ")
      iteration += 1
    print(" ")
  print("\nWhen 'n' is:", n , "Iteration =" , iteration)

test(10)
test(4)
test(3)

print("With every 'n' the taken = n^2")
print("(n^2)")