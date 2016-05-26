import unittest
import problemTwo

class EulerTests(unittest.TestCase):
  def test_gen_list_under_zero(self):
    assert(set(problemTwo.gen_list_under(0)) == set([]))

  def test_gen_list_under_two(self):
    assert(set(problemTwo.gen_list_under(2)) == set([1]))

  def test_gen_list_under_ten(self):
    assert(set(problemTwo.gen_list_under(10)) == set([1, 2, 3, 5, 8]))

  def test_gen_even_fibs_ten(self):
    assert(set(problemTwo.gen_even_fibs_under(10)) == set([2, 8]))
