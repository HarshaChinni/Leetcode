class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []

        for n in num:
            while(k > 0 and len(st) > 0 and st[-1] > n):
                st.pop()
                k -= 1

            if (len(st) == 0 and n == 0):
                continue
            else:
                st.append(n)

        while (k > 0 and len(st) > 0):
            st.pop()
            k -= 1

        return str(int(''.join(st))) if len(st) > 0 else '0'
