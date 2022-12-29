# Intuition
Binary search (similar to Coco q)

# Approach
For each key, we store an array of tuples where the first index is the value, and the second index is the timestamp. It's important to note that everytime we set(), the timestamps are strictly increasing, so when we're trying to find the highest timestamp that's <= the target timestamp for a given key, we can do a binary search.

For the binary search, if we find a vlid timestamp that's less than the target timestamp, we store it as our res. We also want to ensure there isn't a higher valid timestamp, so move the left pointer in. Otherwise if the chosen timestamp is less than the target timestamp, we move the right pointer in

# Complexity
- Time complexity:
    - set(): $O(1)$
    - get(): $O(log($#of times set() has been called)), which worst case where the same/different key is used every time

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O($#of times set() has been called), same case as get(), for the hashmap
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class TimeMap:

    def __init__(self):
        self.hashmap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(value, timestamp)]
        else:
            self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        val_timestamp = self.hashmap[key]
        l, r = 0, len(val_timestamp) - 1

        res = ""

        while l <= r:
            mid = (l + r) // 2

            if timestamp >= val_timestamp[mid][1]:
                res = val_timestamp[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```
