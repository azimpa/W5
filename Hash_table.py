class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        index = self._hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                self.table[index].remove(kv)
                return True
        return False

    def display(self):
        for bucket in self.table:
            if bucket:
                print(bucket)


hash_table = HashTable()
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
print(hash_table.get("apple"))  # Output: 1
hash_table.remove("apple")
print(hash_table.get("apple"))  # Output: None
hash_table.display()
