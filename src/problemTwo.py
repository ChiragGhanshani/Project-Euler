def gen_list_under(upperBound):
  if upperBound <= 1: return []
  elif upperBound == 2: return [1]
  else:
    listOfNums = [1, 2]
    first, second = (1, 2)
    while (first + second) < upperBound:
      listOfNums.append(first + second)
      first = second
      second = listOfNums[-1]
    return listOfNums

print(gen_list_under(10))
