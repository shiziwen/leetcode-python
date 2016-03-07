class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ronum  = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
                  ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                  ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                  ['', 'M', 'MM', 'MMM', '  ', ' ', '  ', '   ', '    ', '  ']]
        res = ''
        index = 0
        
        while num:
            res = ronum[index][num % 10] + res
            num = num / 10
            index += 1
        
        return res

