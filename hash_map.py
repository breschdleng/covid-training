class KeyVal:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_item(self):
        return self.key, self.value

class HashMap:

    def __init__(self, size):
        self.size = size
        if self.size is None or self.size==0:
            raise ValueError('invalid size')
        self.list = self.size*[None]
        self.key_list = []


    def get_hash_idx(self, key):
        hash_value = 0
        if key is not None:
            for char in str(key):
                hash_value += ord(char)
            index = hash_value % self.size
            return index
        else:
            raise ValueError("invalid key")

    def contains(self, key):

        if key in self.key_list:
            return True
        else:
            return False

    def put(self, key, value):
        index = self.get_hash_idx(key)

        if self.list[index] is None:
            self.list[index] = list([KeyVal(key, value)])
            self.key_list.append(key)
        else:
            value_updated = False
            for pair in self.list[index]:

                _key, _val = pair.get_item()
                if _key == key:
                    value_updated = True
                    pair.value = value
            if not value_updated:
                self.list[index].append(KeyVal(key, value))
                self.key_list.append(key)

    def get(self, key):
        index = self.get_hash_idx(key)
        if self.list[index] is not None:
            for pair in self.list[index]:
                _key, _val = pair.get_item()
                if _key == key:
                    return pair.value
        else:
            raise ValueError("no such key")
        return None

    def get_items(self):
        if self.key_list is None:
            raise  ValueError('empty dictionary')
        else:
            key_val_list = []
            for key in self.key_list:
                val = self.get(key)
                key_val_list.append(KeyVal(key, val))
            return key_val_list

    def delete(self, key):
        index = self.get_hash_idx(key)
        if self.list[index] is None:
            return
        for i in range(len(self.list[index])):
            pair = self.list[index][i]
            _key, _val = pair.get_item()
            if _key == key:
                self.list[index].pop(i)
                self.key_list.remove(_key)
                return

    def keys(self):
        if len(self.key_list) == 0:
            raise  ValueError("empty key list")
        else:
            return self.key_list

if __name__ == '__main__':

    hash_map = HashMap(1)
    hash_map.put('one', 1)
    hash_map.put('two', 2)
    hash_map.put('three', 3)
    hash_map.put('four', 4)

    keys = ['one', 'two', 'three', 'four']

    hash_map.delete('four')
    for key in keys:
        print(key, hash_map.get(key))
    print(hash_map.contains('three'))
