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

def gen_even_fibs_under(upperBound):
  return list(filter(lambda x: x % 2 == 0, gen_list_under(upperBound)))
