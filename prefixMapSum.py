'''
Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.

sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.

For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3
mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
'''

'''
so there's a few ways to approach this:

One approach is more space-efficient on the insert() method, but less time efficient on the sum() method
-on this approach we insert values into dicitonary normaly, but when calling the suum() method, we iterate over
all key/value pairs and check if the prefix exists in each key, and if it does, we add its value to some accumulator

This approach would be good if there aren't many keys

Our other approach is less space and time efficient on the insert() but more time-efficient on the sum()
-here, whenever we insert, we keep a secondary dictionary of prefixes. Whenever we call insert(), we store
map the word to its value on our dictionary the way we do on our first appraoch, but then we use our second
dictionary to keep track of all possible prefixes of a word that just got added, and if the prefix already exists,
we add to it.
-This secondary dicitonary can then be used to achieve a O(1) runtime on the sum() method
'''
 class PrefixMapSum:
    def __init__(self):
        self.dict = {}
        self.prefixDict = {}

    def insert(self, key, val):
        self.dict[key] = val

    def sum(self, prefix):
        accumulator = 0
        for k,v in self.dict.items():
            if prefix in k:
                accumulator += v
        return accumulator

    def insert2(self,key, val):
        self.dict[key] = val
        for i in range(len(key)):
            if key[:i] in self.prefixDict:
                self.prefixDict[key[:i]] += val
            else:
                self.prefixDict[key[:i]] = val
    
    def sum2(self,prefix):
        if prefix in self.prefixDict:
            return self.prefixDict[prefix]
        else:
            return 0
