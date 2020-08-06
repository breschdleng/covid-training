import unittest
from hash_map import HashMap

class TestHashMap(unittest.TestCase):
    def test_put(self):
        hash_map = HashMap(10)
        dict = {'one':1, 'two':2, 'three':3, 'four':4, 'four':5}

        for key in dict.keys():
            hash_map.put(key, dict[key])
            self.assertEqual(hash_map.get(key), dict[key])


    def test_get(self):
        hash_map = HashMap(10)
        dict = {'one':1, 'two':2, 'three':3, 'four':4, 'four':5}

        for key in dict.keys():
            hash_map.put(key, dict[key])

        for key in dict.keys():
            value = hash_map.get(key)
            self.assertEqual(dict[key], value)

    def test_contains(self):
        hash_map = HashMap(10)
        dict = {'one':1, 'two':2, 'three':3, 'four':4, 'four':5}
        test_keys = ['zero', 'fifteen', 'one', 'two', 'seven']

        for key in dict.keys():
            hash_map.put(key, dict[key])

        for key in test_keys:
            self.assertEqual(dict.__contains__(key), hash_map.contains(key))

    def test_delete(self):
        hash_map = HashMap(20)
        dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'four': 5}
        delete_keys = ['one', 'two']

        for key in dict.keys():
            hash_map.put(key, dict[key])

        for key in delete_keys:
            hash_map.delete(key)
            dict.pop(key)

        for key in dict.keys():
            value = hash_map.get(key)
            self.assertEqual(dict[key], value)
            self.assertEqual(dict.__contains__(key), hash_map.contains(key))

    def test_get_items(self):
        hash_map = HashMap(10)
        dict = {'one':1, 'two':2, 'three':3, 'four':4, 'four':5}

        for key in dict.keys():
            items = hash_map.get_items()
            for keyval in items:
                _key, _val = keyval.get_item()
                self.assertEqual(_val, dict[key])

    def test_keys(self):
        hash_map = HashMap(10)
        dict = {'one':1, 'two':2, 'three':3, 'four':4, 'four':5}
        for key in dict.keys():
            hash_map.put(key, dict[key])
        keys = hash_map.keys()
        dict_keys = dict.keys()
        for key in dict_keys:
            self.assertEqual((key in keys), (key in dict_keys))


if __name__ == '__main__':
    unittest.main()
