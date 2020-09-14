
from arg_to_hash.hashing import ToHash, TestCase
TestCase().test_to_hash()

# 0
print('#0\t', ToHash(12.0, 'b',  te=13).get_hash_code())

# 1
hsh1 = ToHash(12.0, 'b',  te=13)
print('#1\t', hsh1.get_hash_code())

# 2
hsh1.set_parameters(12.00001, 'b', te=13)
print('#2\t', hsh1.get_hash_code())


