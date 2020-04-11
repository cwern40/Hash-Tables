# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.amount = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        djb2_hash = 5381
        for x in key:
            djb2_hash = (( djb2_hash << 5) + djb2_hash) + ord(x)
        return djb2_hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # Part 1
        # index = self._hash_mod(key)
        # if self.storage[index] is not None:
        #     return print(f"Err: There is already a value at index {index}")
        # else:
        #     self.storage[index] = value
        #     return
        index = self._hash_mod(key)
        self.amount += 1
        # if self.amount / self.capacity >= .7:
        #     self.resize()
        if self.storage[index] is not None:
            current = self.storage[index]
            while current.key is not key and current.next is not None:
                current = current.next
            if current.key == key:
                current.value = value
            else:
                prev_item = self.storage[index]
                self.storage[index] = LinkedPair(key, value)
                self.storage[index].next = prev_item
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            print(f"Warning: Key is not found.")
        else:
            current = self.storage[index]
            prev_item = None
            while current.key is not key and current.next is not None:
                prev_item = current
                current = current.next
            if current.key == key:
                if prev_item is None:
                    self.storage[index] = None
                else:
                    prev_item.next = current.next
            else:
                print(f"Warning: Key is not found.")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        current = self.storage[index]
        while current.key is not key and current.next is not None:
            current = current.next
        if current.key == key:
            return current.value
        else:
            return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for pair in old_storage:
            if pair is not None and pair.next == None:
                self.insert(pair.key, pair.value)
            else:
                current = pair
                while current is not None:
                    self.insert(current.key, current.value)
                    current = current.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")