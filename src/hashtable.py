
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
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for bucket in self.storage:
            # If bucket has no elements
            if bucket == None:
                continue

            else:
                # If bucket has one element
                if bucket.next is None:
                    new_index = self._hash_mod(bucket.key)
                    if new_storage[new_index] == None:
                        # If HashMod index empty, assign bucket element
                        new_storage[new_index] = LinkedPair(bucket.key, bucket.value)
                    else:
                        # If Hashmod index occupied, iterate to end then assign bucket element
                        check = new_storage[new_index]
                        while check.next is not None:
                            check = check.next
                        check.next = LinkedPair(bucket.key, bucket.value)

                # If bucket has multiple elements
                elif bucket.next is not None:
                    current = bucket
                    # Same as above but iterating through bucket
                    while current is not None:
                        new_index = self._hash_mod(current.key)
                        if new_storage[new_index] == None:
                            new_storage[new_index] = LinkedPair(current.key, current.value)
                        else:
                            check = new_storage[new_index]
                            while check.next is not None:
                                check = check.next
                            check.next = LinkedPair(current.key, current.value)

                            # Iterate bucket
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

