import string
from collections import defaultdict
from typing import List, Dict

# A map of the letter in the alphabet to its position in our 25 length list
CHAR_MAP = {c: i for (i, c) in enumerate(list(string.ascii_lowercase))}


class Solution:
    """sub_list_map: is a dict {index_in_original_list: [count_map]}"""
    _input_list: List[str] = []

    def remove_redundant_brackets(self, nested_list):
        if isinstance(nested_list, list) and len(nested_list) == 1 and isinstance(nested_list[0], list):
            return self.remove_redundant_brackets(nested_list[0])
        elif isinstance(nested_list, list):
            return [self.remove_redundant_brackets(item) for item in nested_list]
        else:
            return nested_list

    def recursive_check(self, index_list_map: Dict[int, List[int]], char_index: int) -> List[str]:
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
            return [final_return]
        # map the count for the current character to each string that matches on that character count
        matching_index_list_map: Dict[int, Dict[int, List[dict]]] = defaultdict(dict)
        # go through each list and get count for the current letter char_index
        for key, value in index_list_map.items():
            matching_index_list_map[value[char_index]].update({key: value})
        # we have reached the count for 'z' if it is equal return all the lists else one more recursion
        if char_index == 24:
            for matchs in matching_index_list_map.values():
                final_matches = [self._input_list[s_ind] for s_ind in matchs.keys()]
                print(f'Returning final matches {final_matches}')
                return final_matches
        return [self.recursive_check(sub_map, char_index + 1) for sub_map in matching_index_list_map.values()]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self._input_list = strs
        index_list_map: Dict[int, List[int]] = {}
        # enumerate all the input strings and map it to its index in the input list
        for idx, c_string in enumerate(strs):
            # this is a 25 length list for each letter in the alphabet initialize the char count list to 0
            index_list_map[idx] = [0 for _ in range(25)]
            for char in c_string:
                index_list_map[idx][CHAR_MAP[char]] = index_list_map[idx][CHAR_MAP[char]] + 1
            # we now have a dict from index in input string to list of char counts
        # print(f'Created the Character count grid {index_list_map}')
        final_result = self.remove_redundant_brackets([self.recursive_check(index_list_map, 0)])
        print(f'The final result is {final_result}')
        return final_result

    # def groupAnagramsOld(self, strs: List[str]) -> List[List[str]]:
    #     grouped_return: List[List[str]] = []
    #     ascii_map: Dict[int, List[str]] = dict()
    #     for word in strs:
    #         ascii_values = [ord(c) for c in word]
    #         total = sum(ascii_values)
    #         entry = ascii_map.get(total, [])
    #         entry.append(word)
    #         ascii_map[total] = entry
    #     # now that we have broken the problem down to just checking
    #     # strings that have the same ord value
    #     print(ascii_map)
    #     for sub_list in ascii_map.values():
    #         if len(sub_list) == 1:
    #             grouped_return.append(sub_list)
    #         else:
    #         # For each sublist make sure that they are in fact anagrams
    #             """
    #             TODO for each sub list go through it an verify that each item in
    #             For each string in the list make a grid to trach the counts of each
    #             character in the string and each count of that character int he string
    #             from a-z for each column for a constant 25 columns and a row for each string for an
    #             mx25 where m is the number of string
    #             This can be a recursive function where any matching string will go to the next call
    #             of the function and that function will break all the colums up depending on if they match in the
    #             next character or not
    #             for i in range(25):
    #                 if row[i]
    #              a - z
    #             1[   [2, 0, 3,...]
    #             -     [1, 2, 0,...]
    #                   [2, 1, 3,...]]
    #             m
    #             create a bucket map for each occurence to the sublist to send to the next check
    #             if a list only has one return it
    #             {2: [l1, l3], 6: [l2]}
    #             """

    #             while sub_list:
    #                 matching = []
    #                 non_matching = []
    #                 possible_match = []
    #                 char_map: Dict[str, int] = dict()
    #                 template_str = sub_list.pop(0)
    #                 matching.append(template_str)
    #                 # Slit the problem again from string of the same length with the template string the non matching will go through this loop again.
    #                 for string in sub_list:
    #                     if len(string) != sub_list:
    #                         non_matching.append(string)
    #                     else:
    #                         possible_match.append(string)
    #                 for char in template_str:
    #                     char_map[char] = char_map.get(char, 0) + 1
    #                 string_index_list = [idx for idx in len(sub_list)]
    #                 # [0 , 1, 2, 3]
    #                 char_idx_list = [idx for idx in template_str]
    #                 # [0 , 1, 2, 3, 4]
    #                 for
    #                 # we will use this list of character index to compare all
    #                 # lists at once with the template string, the hope is they
    #                 # all match the ones that do add to the template strings
    #                 # result array and start again with the remaining strings
    #                     check = sub_list[0]
    #                     for char in check:
    #     return ascii_map.values()

