
# coding: utf-8


import unittest
from ex3 import maxProfit

class MyCase(unittest.TestCase):

    def test(self):
        prices = [7,1,5,3,6,4]
        answer = ('total profit is :5', 'buying day is: 2', 'selling day is : 5')
        check = maxProfit(prices)
        self.assertEqual(answer, check)

    def test_b(self):
        prices = [1,2,3,4,5]
        answer = ('total profit is :4', 'buying day is: 1', 'selling day is : 5')
        check = maxProfit(prices)
        self.assertEqual(answer, check)

    def test_c(self):
        prices = [7,6,4,3,1]
        answer = ('total profit is :0', 'buying day is: 5', 'selling day is : 5')
        check = maxProfit(prices)
        self.assertEqual(answer, check)        

if __name__ == '__main__':
    unittest.main()

