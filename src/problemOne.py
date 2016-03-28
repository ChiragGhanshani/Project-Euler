def check(listToCheck):
  return list(filter(lambda x: x % 3 == 0 or x % 5 == 0, listToCheck))

print(check(range(1, 1001)))
