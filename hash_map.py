class Dict:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_item(self):
        return self.key, self.value

class HashMap:
    def __init__(self, size):

        self.size = size
        self.map = self.size*[None]

    def get_hash_idx(self, key):
        hash_value = 0
        if key is not None:
            for char in key:
                hash_value += ord(key)
            index = hash_value % self.size
            return index
        else:
            raise ValueError("invalid key")

    def put(self, key, value):
        index = self.get_hash_idx(key)

        if self.map[index] is None:
            self.map[index] = list([Dict(key, value)])
        else:
            for i in range(len(self.map[index])):

                k, v = self.map[index][i].get_item()
                if k==key:
                    self.map[index][i].value = value



    def get(self, key):

        index = self.get_hash_idx(key)







