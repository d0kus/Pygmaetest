from collections import deque

#Task1
def sumTwo(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        compl = target - n
        if compl in seen:
            return [seen[compl], i]
        seen[n] = i

#Task2
def firstUniq(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for i, n in enumerate(s):
        if count[n] ==1:
            return i
    return -1

#Task3
def is_isomorph(s, t):
    s_to_t = {}
    t_to_s = {}
    for c1, c2 in zip(s, t):
        if c1 in s_to_t and s_to_t[c1] != c2:
            return False
        if c2 in t_to_s and t_to_s[c2] != c1:
            return False
        s_to_t[c1] = c2
        t_to_s[c2] = c1
    return True

#Task4
def is_happy(n):
  seen = set()
  while n != 1:
    n = sum(int(d) ** 2 for d in str(n))
    if n in seen:
      return False
    seen.add(n)
  return True

#Task5
class treeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def level_ord(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

#Task6
def max_depth(root):
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1

#Task7
def is_symmetric(root):
    def mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and mirror(left.left, right.right) and mirror(left.right, right.left)
    return mirror(root.left, root.right)

#Task8
def longest_consecutive(root):
    def dfs(node, parent, length):
        if not node:
            return length
        if node.val == parent + 1:
            length += 1
        else:
            length = 1
        left = dfs(node.left, node.val, length)
        right = dfs(node.right, node.val, length)
        return max(length, left, right)
    return dfs(root, root.val, 0)

#Task9
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

#Task10
def quick_sort(nums, low, high):
    if low < high:
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        pi = i + 1
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)

#Task11
def merge_sort(nums):
    if len(nums) <= 1:
        return
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

#Task12
def heap_sort(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)

def heapify(nums, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)

#task1
nums = [2,7,11,15]
target = 9
print(sumTwo(nums, target), '\n')
#task2
s = "loveleetcode"
print(firstUniq(s), '\n')
#task3
s = "egg"
t = "add"
print(is_isomorph(s, t), '\n')
#task4
n = 19
print(is_happy(n), '\n')
#task5
root = treeNode(3)
root.left = treeNode(9)
root.right = treeNode(20)
root.right.left = treeNode(15)
root.right.right = treeNode(7)
print(level_ord(root), '\n')
#task6
print(max_depth(root), '\n')
#task7
root2 = treeNode(1)
root2.left = treeNode(2)
root2.right = treeNode(2)
root2.left.left = treeNode(3)
root2.left.right = treeNode(4)
root2.right.left = treeNode(4)
root2.right.right = treeNode(3)
print(is_symmetric(root2), '\n')
#task8
root3 = treeNode(1)
root3.right = treeNode(3)
root3.right.left = treeNode(2)
root3.right.right = treeNode(4)
root3.right.right.right = treeNode(5)
print(longest_consecutive(root3), '\n')
#task9
nums = [2, 0, 2, 1, 1, 0]
sort_colors(nums)
print(nums, '\n')
#task10
nums = [3, 6, 8, 10, 1, 2, 1]
quick_sort(nums, 0, len(nums) - 1)
print(nums, '\n')
#task11
nums = [3, 6, 8, 10, 1, 2, 1]
merge_sort(nums)
print(nums, '\n')
#task12
nums = [3, 6, 8, 10, 1, 2, 1]
heap_sort(nums)
print(nums)

