'''

Collision Handling
When two different inputs produce the same output, then we have a collision. Our implementation of get_hash_code()
function is satisfactory. However, because we are using compression function, we are prone to collisions.

Consider the following scenario.

We have a bucket array of length 10 and we get two different hash codes for two different inputs, say 355, and 1095.
Even though the hash codes are different in this case, the bucket index will be same because of the way we have
implemented our compression function. Such scenarios where multiple entries want to go to the same bucket are
very common. So, we introduce some logic to handle collisions.

There are two popular ways in which we handle collisions.

    1. Closed Addressing or Separate chaining
    2. Open Addressing

Closed addressing is a clever technique where we use the same bucket to store multiple objects. The bucket in this
case will store a linked list of key-value pairs. Every bucket has it's own separate chain of linked list nodes.

In open addressing, we do the following:

If, after getting the bucket index, the bucket is empty, we store the object in that particular bucket

If the bucket is not empty, we find an alternate bucket index by using another function which modifies the current
hash code to give a new code

Separate chaining is a simple and effective technique to handle collisions and that is what we discuss here.

Implement the put and get function using the idea of separate chaining.

'''


class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets  # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets  # compress coefficient

        return hash_code % num_buckets  # one last compression before returning

    def size(self):
        return self.num_entries


hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))