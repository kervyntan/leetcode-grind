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
        self.MAXLOADFACTOR = 0.65 # n / k, n = number of used slots & k = total number of slots
    
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
    
    def growth(self):
        new_hash_table = HashTable()
        new_hash_table.size = 2 * self.size
        new_hash_table.slots = [None for i in range(new_hash_table.size)]
        
        for i in range(self.size):
            # If existing hashtable has value at that index
            # Populate it into the new hashtable
            if self.slots[i] != None:
                new_hash_table.put(self.slots[i].key, self.slots[i].value)
        
        self.size = new_hash_table.size
        self.slots = new_hash_table.slots
    
    def check_growth(self):
        loadfactor = self.count / self.size
        if loadfactor > self.MAXLOADFACTOR:
            self.growth()
    
    # Inserting elements into the hashtable
    def put(self, key, value):
        item = HashItem(key, value)
        hash = self._hash(key)
        while self.slots[hash] != None:
            if self.slots[hash].key == key:
                # If the key already exists
                break
            
            hash = (hash + 1) % self.size # Linear probing 
        if self.slots[hash] == None:
            # Add to the count since new item added 
            self.count += 1
        self.slots[hash] = item
        self.check_growth()
            