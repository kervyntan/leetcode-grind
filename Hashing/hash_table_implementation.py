class HashItem:
    def __init__(self, key, value):
        # Each HashItem stores a key and a corresponding value
        self.key = key
        self.value = value
        
class HashTable:
    def __init__(self):
        # Initial size of 256 items
        self.size = 256
        # Actual storage of hashtable items
        self.slots = [None for i in range(self.size)]
        # How many ACTUAL items are currently in the hashtable
        self.count = 0
    
    def _hash(self, key):
        mult = 1
        hash_value = 0
        # Assuming key is a string
        # We'll return the sum of ordinal values (ASCII values) of characters in a string
        for ch in key:
            hash_value += mult * ord(ch)
            # Increasing the multiplier as we go through each char
            mult += 1
        
        # Need to modulo here
        # To ensure our hash value remains within the range 0 - self.size (number of slots in our hashtable)
        # Since remainder is never larger than it's divisor
        return hash_value % self.size