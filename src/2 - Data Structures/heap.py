

class MinHeap(object):
    def __init__(self, data = None):
        
        
        if data is None:
            self.A = []
            self.length = 0
        else:
            self.A = data
            self.length = len(data)
            self.build_heap()

        
    def build_heap(self):
        if self.A:
            self.building_heap = True
            self.swaps = []
            z = self.parent(self.size() - 1)
            for i in range(z, -1, -1):
                self.heapify_down(i)
            self.building_heap = False
            
    
    def put(self, newValue, i = None):
        if (i is None):
            self.A.append(newValue)
            self.length += 1
            self.heapify_up(self.length - 1)
        else:
            pass
    
    def extract_min(self):
        if not self.A:
            raise Exception("Heap is Empty")
        temp = self.A[0]
        self.length -= 1
        if self.length:
            self.A[0] = self.A.pop()
            self.heapify_down(0)
        else:
            self.A.pop()
        return temp
        
        
    
    def size(self):
        return self.length
    
    def isEmpty(self):
        return self.length == 0
    
    def heapify_up(self, i):
        if i < 0 or i >= self.length:
            raise Exception("Illegal Argument Exception")
        
        if i == 0:
            return
        
        p = self.parent(i)
        
        if self.A[p] > self.A[i]:
            ## exchange A[i] and A[p]
            temp = self.A[i]
            self.A[i] = self.A[p]
            self.A[p] = temp
            self.heapify_up(p)
    
    def heapify_down(self, i):
        l = self.left(i)
        r = self.right(i)
        
        if l < self.size() and self.A[l] < self.A[i]:
            smallest = l
        else:
            smallest = i
        
        if r < self.size() and self.A[r] < self.A[smallest]:
            smallest = r
        
        if smallest != i:
            ## exchange A[i] and A[smallest]
            
            if self.building_heap:
                self.swaps.append((i, smallest))
            temp = self.A[i]
            self.A[i] = self.A[smallest]
            self.A[smallest] = temp
            self.heapify_down(smallest)
        
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2
    
    def parent(self, i):
        return (i - 1) // 2




n = int(input("Enter the number of elements: "))

data = list(map(int, input().split()))

heap = MinHeap(data)
swaps = heap.swaps

print(len(swaps))
for i, j in swaps:
    print(i, j)












# if __name__ == "__main__":
#     # Running the tests will surface any issues in the MinHeap implementation.
#     # NOTE: If tests fail, read the assertion messages to see what behavior is not matching.
#     unittest.main()

# =========================
# Extra MinHeap tests (paste below your class)
# =========================
# import unittest
# import random

# class TestMinHeapEdgeCases(unittest.TestCase):
#     def assertHeapProperty(self, h: "MinHeap"):
#         # Parent value <= child value for all nodes (by size/length, not by len(A))
#         for i in range(1, h.size()):
#             p = h.parent(i)
#             self.assertLessEqual(h.A[p], h.A[i], f"Heap property violated at i={i}: {h.A[p]} > {h.A[i]}")

#     def assertInvariants(self, h: "MinHeap"):
#         # Core invariants we expect to hold
#         self.assertGreaterEqual(h.size(), 0, "size() should never be negative")
#         self.assertEqual(len(h.A), h.size(), "len(A) must equal reported size()")
#         if h.size() > 0:
#             self.assertHeapProperty(h)

#     def test_single_element_extract_leaves_empty(self):
#         h = MinHeap()
#         h.put(10)
#         self.assertInvariants(h)
#         m = h.extract_min()
#         self.assertEqual(m, 10)
#         # After removing last element:
#         self.assertEqual(h.size(), 0)
#         self.assertTrue(h.isEmpty())
#         self.assertEqual(len(h.A), 0, "Internal array should be empty after extracting the only element")

#     def test_extract_min_from_empty_raises(self):
#         h = MinHeap()
#         with self.assertRaises(Exception):
#             h.extract_min()

#     def test_init_with_list_then_extract_all_sorted(self):
#         data = [9, 1, 5, 3, 7, 2, 6, 4, 8, 0]
#         h = MinHeap(data[:])
#         self.assertInvariants(h)
#         out = []
#         while not h.isEmpty():
#             out.append(h.extract_min())
#             # Invariants must keep holding after each extract
#             if not h.isEmpty():
#                 self.assertInvariants(h)
#         self.assertEqual(out, sorted(data))

#     def test_put_duplicates_and_order(self):
#         h = MinHeap()
#         seq = [5, 1, 1, 3, 2, 2, 2, 0, 0]
#         for v in seq:
#             h.put(v)
#             self.assertInvariants(h)
#         out = []
#         while not h.isEmpty():
#             out.append(h.extract_min())
#             if not h.isEmpty():
#                 self.assertInvariants(h)
#         self.assertEqual(out, sorted(seq))

#     def test_randomized_stress(self):
#         for _ in range(5):
#             data = [random.randint(-50, 50) for _ in range(200)]
#             h = MinHeap()
#             for v in data:
#                 h.put(v)
#                 self.assertInvariants(h)
#             extracted = []
#             while not h.isEmpty():
#                 extracted.append(h.extract_min())
#                 if not h.isEmpty():
#                     self.assertInvariants(h)
#             self.assertEqual(extracted, sorted(data))

#     def test_build_heap_invariants_from_list(self):
#         data = [random.randint(0, 1000) for _ in range(123)]
#         h = MinHeap(data[:])
#         self.assertInvariants(h)
#         # Root must be global minimum
#         self.assertEqual(h.A[0], min(data))

# if __name__ == "__main__":
#     unittest.main()
