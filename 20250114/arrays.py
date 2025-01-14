# Implement a vector (mutable array with automatic resizing):
# * New raw data array with allocated memory
#   can allocate int array under the hood, just not use its features
#   start with 16, or if the starting number is greater, use power of 2 - 16, 32, 64, 128
# * size() - number of items
# * capacity() - number of items it can hold
# * is_empty()
# * at(index) - returns the item at a given index, blows up if index out of bounds
# * push(item)
# * insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
# * prepend(item) - can use insert above at index 0
# * pop() - remove from end, return value
# * delete(index) - delete item at index, shifting all trailing elements left
# * remove(item) - looks for value and removes index holding it (even if in multiple places)
# * find(item) - looks for value and returns first index with that value, -1 if not found
# * resize(new_capacity) // private function
#    when you reach capacity, resize to double the size
#    when popping an item, if the size is 1/4 of capacity, resize to half
# 
# Implement unit tests to test each feature.

import unittest

# Class Definition of a Dynamic Array
class DynamicArray:
    # Initialization
    def __init__(self):
        self._capacity = 16 # Initial capacity
        self._size = 0      # Number of elements in the array
        self._array = [0] * self._capacity # Backing array for storage

    # Methods to return the current size and capacity of the array.
    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def is_empty(self):
        return self._size == 0

    # Method to access elements and handle out-of-bounds access.
    def at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]

    # Method to add an item to the end of the array.
    def push(self, item):
        if self._size == self._capacity:
            self.resize(2 * self._capacity) # Double the capacity
        self._array[self._size] = item
        self._size += 1

    # Method to insert an item at a specified index.
    def insert(self, index, item):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        if self._size == self._capacity:
            self.resize(2 * self._capacity)
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = item
        self._size += 1

    # Method to add an item at the start.
    def prepend(self, item):
        self.insert(0, item)

    # Method to remove an element from the end of the array.
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty array")
        value = self._array[self._size - 1]
        self._size -= 1
        if self._size <= self._capacity // 4 and self._capacity > 16:
            self.resize(self._capacity // 2)
        return value

    # Method to remove an element at a specified index.
    def delete(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1

    # Method to look for a value and remove it.
    def remove(self, item):
        for i in range(self._size):
            if self._array[i] == item:
                self.delete(i)
                return

    # Method that returns the first index of the value or -1 if not found.
    def find(self, item):
        for i in range(self._size):
            if self._array[i] == item:
                return i
        return -1

    # Method to adjust the size of the backing array.
    def resize(self, new_capacity):
        new_array = [0] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity


# Class Definition for Testing a Dynamic Array
class TestDynmaicArray(unittest.TestCase):
    def setUp(self):
        self.array = DynamicArray()

    # Test for Initial Capacity and Size
    def test_initial_capacity_and_size(self):
        self.assertEqual(self.array.capacity(), 16)
        self.assertEqual(self.array.size(), 0)
        self.assertTrue(self.array.is_empty())

    # Test for Adding Elements (Push)
    def test_push_and_size(self):
        self.array.push(10)
        self.assertEqual(self.array.size(), 1)
        self.assertEqual(self.array.at(0), 10)

    # Test for Accessing Elements (at)
    def test_at_valid_index(self):
        self.array.push(20)
        self.assertEqual(self.array.at(0), 20)

    def test_at_invalid_index(self):
        with self.assertRaises(IndexError):
            self.array.at(1) # Accessing out of bounds

    # Test for Inserting Elements (insert)
    def test_insert_valid_index(self):
        self.array.push(30)
        self.array.insert(0, 25) # Insert at index 0
        self.assertEqual(self.array.at(0), 25)
        self.assertEqual(self.array.size(), 2)

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.array.insert(2, 40)

    # Test for Prepending Elements (prepend)
    def test_prepend(self):
        self.array.push(50)
        self.array.prepend(45)
        self.assertEqual(self.array.at(0), 45)

    # Test for Removing Elements (pop)
    def test_pop(self):
        self.array.push(60)
        popped_value = self.array.pop()
        self.assertEqual(popped_value, 60)
        self.assertEqual(self.array.size(), 0)

    def test_pop_empty_array(self):
        with self.assertRaises(IndexError):
            self.array.pop() # Pop empty array

    # Test for Deleting Elements (delete)
    def test_delete_valid_index(self):
        for i in range(5): # Push elements 0 to 4
            self.array.push(i)

        # Delete element at index 2 (which is '2')
        self.array.delete(2)

        # Now array should be [0, 1, 3, 4], size should be 4
        self.assertEqual(self.array.size(), 4)
        self.assertEqual(self.array.at(2),  3) # Ensure we can access what was previously at index 3

        # Check that accessing index 4 raises IndexError (out of bounds)
        with self.assertRaises(IndexError):
            self.array.at(4)

    # Test for Removing Specific Item (remove)
    def test_remove_item(self):
        for i in range(5):
            self.array.push(i)
        self.array.remove(3)
        self.assertEqual(self.array.find(3), -1)

    # Test for Finding Items (find)
    def test_find_item_exists(self):
        for i in range(5):
            self.array.push(i)
        index = self.array.find(3)
        self.assertEqual(index, 3)

    def test_find_item_not_exists(self):
        index = self.array.find(10)
        self.assertEqual(index, -1)

    # Test Resizing Logic
    def test_resize_upward(self):
        for i in range(16):
            self.array.push(i)
        initial_capacity = self.array.capacity()
        self.array.push(16)
        new_capacity = self.array.capacity()
        self.assertGreater(new_capacity, initial_capacity)

    def test_resize_downward(self):
        for i in range(32):
            self.array.push(i)
        initial_capacity = self.array.capacity()

        for _ in range(28):
            self.array.pop()
        new_capacity = self.array.capacity()

        self.assertLess(new_capacity, initial_capacity)


# Run the tests
if __name__ == '__main__':
    unittest.main()