import random
import time
import math

class LinkedListNode:
    def __init__(self, value, next=None) -> None:
        self.value: int = value
        self.next: LinkedListNode = next

    def print(self) -> None:
        print(f"{self.value} ", end="")
        if self.next != None:
            self.next.print()
        else:
            print("NULL")

def list_to_linked_list(nums: list[int]) -> LinkedListNode:
    head = None
    for num in nums[-1::-1]:
        head = LinkedListNode(num, head)
    return head


# # Approach 1
#         1 2 3 4 5 6 7 8 NULL 
# fast                    ^
# slow            ^

def fast_slow(ll: LinkedListNode):
    fast = ll
    slow = ll
    while fast.next != None:
        fast = fast.next
        if fast.next != None:
            fast = fast.next
        slow = slow.next

    return fast, slow

# # Approach 2
# 2 loops

def two_loops(ll: LinkedListNode):
    curr = ll
    n = 0
    # fast and get N
    while curr.next != None:
        curr = curr.next
        n += 1
    fast = curr
    # slow using N
    half_n = int(n//2 + n%2)
    slow = ll
    for i in range(half_n):
      slow = slow.next
    return fast, slow

# # Approach 3
# convert linked list to dict
def convert_to_dict(ll: LinkedListNode):
    curr = ll
    my_dict = dict()
    key = 0
    while curr.next != None:
      my_dict[key] = curr
      key = key + 1
      curr = curr.next
    return curr, my_dict[key//2 + key%2]

# # Approach 4
# convert linked list to list
def convert_to_list(ll: LinkedListNode):
    curr = ll
    my_list = list()
    n = 0
    while curr.next != None:
      my_list.append(curr)
      n = n + 1
      curr = curr.next
    return curr, my_list[n//2 + n%2]

import csv
def run_lab_and_write_to_csv():
    ns = [100,1000,10000,100000,1000000,2000000,5000000,10000000]#[i for i in range(5, 1000)]
    approaches = [
        {"name": "slow_fast", "function": fast_slow},
        {"name": "2 loop", "function": two_loops},
        {"name": "linked list to dict", "function": convert_to_dict},
        {"name": "linked list to array", "function": convert_to_list}
    ]
    with open('results.csv', 'w+', newline='') as f:
        writer = csv.writer(f)
        row = ["n" for i in range(len(approaches)+1)]
        for i, approach in enumerate(approaches):
            row[i+1] = approach["name"]
        writer.writerow(row)
    with open('results.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        for n in ns:
            results = [-1 for i in range(len(approaches)+1)]
            results[0] = n
            arr = [random.randint(1, 100) for i in range(n)]
            slow_answer = arr[math.ceil((len(arr) - 1)/2)]
            fast_answer = arr[-1]
            ll: LinkedListNode = list_to_linked_list(arr)
            for i, approach in enumerate(approaches):
                start = time.time()
                fast, slow = approach["function"](ll)
                end = time.time()
                if (fast.value != fast_answer) or (slow.value != slow_answer):
                    print(f"Approach: {approach['name']}")
                    print(f" n: {n}")
                    print(f" fast: {fast.value} fast_answer: {fast_answer}")
                    print(f" slow: {slow.value} slow_answer: {slow_answer}")
                    raise Exception("Answer not correct")
                elapsed = end - start
                results[i+1] = elapsed
            writer.writerow(results)

if __name__ == "__main__":
    run_lab_and_write_to_csv()

#       1 2 3 4 5 6 7 NULL 
# Slow:       ^ 
# Fast:             ^.next































# Predictions 
#   Jason:
#       I predict #1 will be the fastest when N is large. 
#       When N is small #3 will be the fastest. 
#       #2 will be consistently the slowest.
#   Martin: 
#       #1 faster regardless of N 
#       #2 faster than #3 when N is small
#       #3 faster than #2 when N is large
#   Colton:
#       #1 faster than #3
#       #3 faster than #2

# # Approach 1
#         1 2 3 4 5 6 7 8 NULL 
# fast                    ^
# slow 

# # Approach 2
# 2 loops

# # Approach 3
# convert linked list to dict