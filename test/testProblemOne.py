import unittest
from problemOne import check
from problemOne import doSum

class EulerTests(unittest.TestCase):
  def test_multiples_of_three_and_five(self):
    passValues = [3, 5, 6, 9, 10]
    test = range(1, 11)
    assert(set(passValues)== set(check(test)))

  def test_sum_multiples(self):
    passValue = 33
    test = range(1, 11)
    assert(passValue == doSum(test))
