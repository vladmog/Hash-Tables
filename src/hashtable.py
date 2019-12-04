# # '''
# # Linked List hash table key/value pair
# # '''
# class LinkedPair:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None


# class HashTable:
#     '''
#     A hash table that with `capacity` buckets
#     that accepts string keys
#     '''
#     def __init__(self, capacity):
#         self.capacity = capacity  # Number of buckets in the hash table
#         self.storage = [None] * capacity
#         # TODO: Add self.count to track table load and resize when needed.


#     def _hash(self, key):
#         '''
#         Hash an arbitrary key and return an integer.
#         You may replace the Python hash with DJB2 as a stretch goal.
#         '''
#         return hash(key)


#     def _hash_djb2(self, key):
#         '''
#         Hash an arbitrary key using DJB2 hash
#         OPTIONAL STRETCH: Research and implement DJB2
#         '''
#         pass


#     def _hash_mod(self, key):
#         '''
#         Take an arbitrary key and return a valid integer index
#         within the storage capacity of the hash table.
#         '''
#         return self._hash(key) % self.capacity


    # def insert(self, key, value):
    #     '''
    #     Store the value with the given key.
    #     Hash collisions should be handled with Linked List Chaining.
    #     '''
    #     index = self._hash_mod(key)
    #     if self.storage[index] is not None:
    #         print(f"WARNING: Overwriting data at {index}")
    #     self.storage[index] = LinkedPair(key, value)


#     def remove(self, key):
#         '''
#         Remove the value stored with the given key.
#         Print a warning if the key is not found.
#         '''
#         index = self._hash_mod(key)
#         if self.storage[index] is None:
#             print(f"WARNING: Key not found")
#             return
#         self.storage[index] = None


#     def retrieve(self, key):
#         '''
#         Retrieve the value stored with the given key.
#         Returns None if the key is not found.
#         '''
#         index = self._hash_mod(key)
#         if self.storage[index] is not None:
#             if self.storage[index].key == key:
#                 return self.storage[index].value
#             else:
#                 print(f"WARNING: Key doesn't match")
#                 return None
#         else:
#             return None


#     def resize(self):
#         '''
#         Doubles the capacity of the hash table and
#         rehash all key/value pairs.
#         '''
#         self.capacity *= 2
#         new_storage = [None] * self.capacity
#         for bucket_item in self.storage:
#             if bucket_item is not None:
#                 new_index = self._hash_mod(bucket_item.key)
#                 new_storage[new_index] = LinkedPair(bucket_item.key, bucket_item.value)
#         self.storage = new_storage


# if __name__ == "__main__":
#     ht = HashTable(2)
#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")
#     print("")
#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))
#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)
#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")
#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))
#     print("")



    # ==========================================================

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


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash

    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass

    # the _underscore before the method implies the function shouldn't be used outside of the class


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''

        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.retrieve(key) is not None:
            self.remove(key)

        if self.storage[index] != None:
            stack = []
            current = self.storage[index]
            stack.append(current.value)
            next = self.storage[index].next
            while next is not None:
                current = next
                next = next.next
                stack.append(current.value)
            current.next = LinkedPair(key, value)

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
            print("ERROR Element with given key not found")

        elif self.storage[index].key == key:
            self.storage[index] = None

        else:
            current = self.storage[index]
            prev = None
            while current.key != key:
                prev = current
                current = current.next
            if current.key == key:
                prev.next = current.next
                current = None
            elif current is None:
                print("Element not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        
        if self.storage[index] is None:
            return None
        elif self.storage[index].key == key:
            return self.storage[index].value
        elif self.storage[index].next is None:
            return None
        elif self.storage[index].next != None:
            current = self.storage[index]
            while current.key != key and current.next != None:
                current = current.next
            if current.key == key:
                return current.value
            else:
                return None


    def resize(self):
        print(f"RESIZE INIT")
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for bucket in self.storage:
            print(f"\nbucket {bucket}")
            if bucket:
                print(f"Val {bucket.value}")
            if bucket is None:
                # Empty bucket
                print(f"Empty bucket")
                continue
            elif bucket.next is None:
                # Occupied bucket with no next
                print(f"Occupied bucket with no next")
                new_index = self._hash_mod(bucket.key)
                new_storage[new_index] = LinkedPair(bucket.key, bucket.value)
            elif bucket.next is not None:
                # Occupied bucket with a next
                print(f"Occupied bucket with a next")
                current = bucket
                while current.next is not None:
                    print(f"Iterate {current.value}")
                    new_index = self._hash_mod(current.key)
                    new_storage[new_index] = LinkedPair(current.key, current.value)
                    current = current.next

        self.storage = new_storage









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

