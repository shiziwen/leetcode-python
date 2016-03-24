class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ln = list(str(1))
        for i in range(1, n):
            tn = []
            count = 1
            prev = None
            for c in ln:
                if prev == c:
                    count += 1
                if prev is not None and prev != c:
                    tn.append(str(count))
                    tn.append(str(prev))
                    count = 1
                prev = c
            tn.append(str(count))
            tn.append(str(prev))
            ln = tn
        return ''.join(ln)
