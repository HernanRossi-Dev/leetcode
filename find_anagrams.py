import string
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict, Tuple

# A map of the letter in the alphabet to its position in our 25 length list
CHAR_MAP = {c: i for (i, c) in enumerate(list(string.ascii_lowercase))}


@dataclass
class AnagramGroup:
    anagrams: List[str]


class Solution:
    """sub_list_map: is a dict {index_in_original_list: [count_map]}"""

    _input_list: List[str] = []

    def recursive_check(
        self, index_list_map: Dict[int, List[Dict]], char_index: int
    ) -> list[AnagramGroup]:
        """
        Recurse through each list in the index_list_map and split the list up into
        the lists that match on the current letter at char_index
        inputs:
          index_list_map: A hashmap that maps the index to the location in the original input list of string
          char_index: as we move through the alphabet this is the index of that letter in out CHAR_MAP
        """
        if len(index_list_map) == 1:
            # we are at the base case for a single list with no matches
            final_return = self._input_list[list(index_list_map.keys())[0]]
            return [AnagramGroup([final_return])]
        # map the count for the current character to each string that matches on that character count
        matching_index_list_map: Dict[int, Dict[int, List[dict]]] = defaultdict(dict)
        # go through each list and get count for the current letter char_index
        for key, value in index_list_map.items():
            matching_index_list_map[value[char_index]].update({key: value})
        # we have reached the count for 'z' if it is equal return all the lists else one more recursion
        if char_index == 24:
            for matches in matching_index_list_map.values():
                final_matches = [self._input_list[s_ind] for s_ind in matches.keys()]
                anagram_group = AnagramGroup(final_matches)
                return [anagram_group]
        result = []
        for sub_map in matching_index_list_map.values():
            result.extend(self.recursive_check(sub_map, char_index + 1))
        return result

    def groupAnagramsRecursive(self, strs: List[str]) -> List[List[str]]:
        self._input_list = strs
        index_list_map: Dict[int, List[int]] = {}
        # enumerate all the input strings and map it to its index in the input list
        for idx, c_string in enumerate(strs):
            # this is a 25 length list for each letter in the alphabet initialize the char count list to 0
            index_list_map[idx] = [0 for _ in range(25)]
            count_list: List[int] = []
            for char in c_string:
                index_list_map[idx][CHAR_MAP[char]] = (
                    index_list_map[idx][CHAR_MAP[char]] + 1
                )
            # we now have a dict from index in input string to list of char counts
        anagram_groups = self.recursive_check(index_list_map, 0)
        final_result = [group.anagrams for group in anagram_groups]
        return final_result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pair_map: Dict[Tuple, List[str]] = dict()
        # enumerate all the input strings and map it to its index in the input list
        for c_string in strs:
            # this is a 25 length list for each letter in the alphabet initialize the char count list to 0
            count_list: List[int] = [0 for _ in range(26)]
            for char in c_string:
                count_list[CHAR_MAP[char]] = count_list[CHAR_MAP[char]] + 1
            # we now have a dict from index in input string to list of char counts
            tuple_list = tuple(count_list)
            if anagrams := pair_map.get(tuple_list):
                anagrams.append(c_string)
            else:
                anagrams = [c_string]
            pair_map[tuple_list] = anagrams
        return list(pair_map.values())
