def check(listToCheck):
  return list(filter(lambda x: x % 3 == 0 or x % 5 == 0, listToCheck))

def doSum(listToUse):
  return reduce(lambda x, y: x + y, check(listToUse))

print(doSum(range(1, 1001)))
