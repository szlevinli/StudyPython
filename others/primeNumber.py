for i in range(2, 100):
  for j in range(2, i + 1):
    if i % j == 0 and i != j:
      break
    elif i % j != 0:
      continue
    else:
      print(i, end=',')

print('\n')