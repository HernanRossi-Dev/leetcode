from typing import Dict


class Solution:

    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        # Anagrams need to have the same number of characters
        if len(s) != len(t):
            return False
        map_s: Dict[str, int] = dict()
        map_t: Dict[str, int] = dict()
        for c in s:
            count = map_s.get(c, 0)
            map_s[c] = count + 1
        for c in t:
            count = map_t.get(c, 0)
            map_t[c] = count + 1
        for c, count in map_s.items():
            if map_t.get(c) != count:
                return False
        return True


def main():
    s = "racecar"
    t = "carrace"
    result = Solution.is_anagram(s, t)
    print(f"{result=}")


if __name__ == "__main__":
    main()
