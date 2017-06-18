# http://www.lintcode.com/en/problem/k-edit-distance/
# http://www.jiuzhang.com/solution/k-edit-distance/
#
# Given a set of strings which just has lower case letters and a target string,
# output all the strings for each the edit distance with the target no greater than k.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Have you met this question in a real interview? Yes
# Example
# Given words = ["abc", "abd", "abcd", "adc"] and target = "ac", k = 1
# Return ["abc", "adc"]
#

# normal dp
def k_edit_distance(words, target, k):
    rst =[]
    for word in words:
        if is_k(word, target, k):
            rst.append(word)
    return rst


def is_k(word, target, k):

    pass

def _helper(src, dst, k):
    pass


##################
#
# Trie
#
##################

from Commons.TrieNode import TrieNode
def k_edit_distance_2(words, target, k):
    pass