import collections


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self._key_value_map = collections.OrderedDict()
        self._capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self._key_value_map:
            return -1
        value = self._key_value_map.pop(key)
        self._key_value_map[key] = value
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self._key_value_map:
            value = self._key_value_map.pop(key)
        elif len(self._key_value_map) == self._capacity:
            self._key_value_map.popitem(last=False)
        self._key_value_map[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
our_cache.get(9)  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
