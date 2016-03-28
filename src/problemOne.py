def check(listToCheck):
  return list(filter(lambda x: x % 3 == 0 or x % 5 == 0, listToCheck))

def doSum(listToUse):
  return sum(check(listToUse))

print(doSum(range(1, 1000)))
print(check(range(1, 1000)))
print(len(check(range(1, 1000))))
