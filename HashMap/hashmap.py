names = ['alice', 'brad', 'collin', 'brad', 'dylan', 'kim']

count_map = {}

# O(n) time
for name in names:
    if name not in count_map:
        count_map[name] = 1
    else:
        count_map[name] += 1

# Implementing a hashmap
# Hashing function -> to generate index
# to know where to put the object ((key, value) pair) in the array

# Possible hashing function: Modding by size of array