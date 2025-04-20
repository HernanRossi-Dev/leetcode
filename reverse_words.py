

class Solution:

    @staticmethod
    def reverse_words(s: str) -> str:
        words = [w for w in s.split(' ') if w]
        pointer_1 = 0
        pointer_2 = len(words) - 1
        while pointer_1 <= pointer_2:
            temp_1 = words[pointer_1]
            words[pointer_1] = words[pointer_2]
            words[pointer_2] = temp_1
            pointer_1+=1
            pointer_2-=1
        return " ".join(words)


def main():
    input = "the sky is blue"
    expected = "blue is sky the"
    result = Solution.is_anagram(input)
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == "__main__":
    main()
