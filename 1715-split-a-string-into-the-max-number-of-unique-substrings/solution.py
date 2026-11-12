
class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        seen = set()
        self.mas = 0

        '''

        abaaa


        '''

        def b2t(i):

            if i == len(s):
                self.mas = max(self.mas, len(seen))
                return
            
            if len(seen) + len(s) - i <= self.mas:
                return

            for n in range(i + 1, len(s) + 1):

                if s[i:n] in seen:
                    continue

                seen.add(s[i:n])

                b2t(n)

                seen.remove(s[i:n])

        b2t(0)
        return self.mas

