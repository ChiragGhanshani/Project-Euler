import unittest
import problemThree

class TestProbelmThree(unittest.TestCase):
  def test_canary(self):
    assert(True == True)

  def test_addNumbers(self):
    assert(problemThree.addNums(1, 1) == 2)

  def test_addNumbers_Two_and_Two(self):
    assert(problemThree.addNums(2, 2) == 4)

  def test_add_numbers(self):
    assert(problemThree.addNums(5, 6) != 10)

  def test_find_multiples_of_three_and_5(self):
    assert(set(problemThree.findMults(range(0, 10))) == set([0, 3, 5, 6, 9]))
