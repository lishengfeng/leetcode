# Given a 32-bit signed integer, reverse digits of an integer.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        print('x: ' +str(x))
        s = (x > 0) - (x < 0)
        print('s: ' + str(s))
        print('x*s: ' + str(x*s))
        print('[::-1]: ' + (str(x*s)[::-1]))
        r = int(str(x*s)[::-1])
        return s*r * (r < 2**31)