# Intuition
Algorithms

# Approach
<!-- Describe your approach to solving the problem. -->
Realize that we can prefix each string with the length of it and a delimiter such as #. Then when decoding, we can concat all numbers until we reach a delimeter, and then extract the word from the string based on the length

# Complexity
- Time complexity: $O(n)$

- Space complexity: $O(1)$

# Code
```python3
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + '#' + word
        return encoded
        # write your code here

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        i = 0
        output = []
        while i < len(str):
            length = ""
            while i != '#':
                length += str[i]
                i += 1
            length = int(length)
            output.append(str[i + 1: i + length + 1])
            i += length + 1
        return output                
```
