import tracemalloc


class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short_s = min([str1, str2], key=len)
        long_s = str1 if short_s == str2 else str2
        if str1 == str2:
            return str1
        div_result = self.recursive_split(list(short_s), list(long_s), 1)
        print(f"{div_result=}")
        if not div_result:
            return ""
        return "".join(list(short_s)[:div_result])

    def recursive_split(self, s_list, l_list, div_n: int) -> int:
        slicer = int(len(s_list) / div_n)
        sub_str = s_list[:slicer]
        long_check = l_list[: len(sub_str)]
        if not long_check:
            return 0
        if sub_str == long_check:
            if Solution.check_full(l_list, long_check) and Solution.check_full(
                s_list, sub_str
            ):
                return slicer
        return self.recursive_split(s_list, l_list, div_n + 1)

    @staticmethod
    def check_full(full_s, sub_s):
        divisor = len(full_s) / len(sub_s)
        if len(full_s) % int(divisor) == 0:
            full_concat = sub_s * int(divisor)
            if full_concat == full_s:
                return True
        return False


def main():
    tracemalloc.start()
    instance = Solution()
    instance.gcdOfStrings("ABABAB", "ABAB")
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()


if __name__ == "__main__":
    main()
