def addNums(x, y):
  return x + y

def findMults(listOfNums):
  blue1 = []
  for _i in listOfNums:
    x = _i
    if not x % 3 or not x % 5:
      blue1.extend( [ _i ] )
  return blue1


