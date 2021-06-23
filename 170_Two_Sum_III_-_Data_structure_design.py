
# Link: https://leetcode.com/problems/two-sum-iii-data-structure-design/

# Solution A: Use list and hashmap (key = num, value = index)
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.strings = [] 

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.strings.append(number)
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        hashmap = {}
        for i in range(len(self.strings)):
            if value - self.strings[i] in hashmap:
                return True
            hashmap[self.strings[i]] = i


# Solution B: Use hashmap (key = number, value = frequency)
class TwoSum:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {} 
        
        
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.hashmap:
            self.hashmap[number] = 1
        else:
            self.hashmap[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key in self.hashmap.keys():
            temp = value - key
            if key != temp:
                if temp in self.hashmap:
                    return True
            elif self.hashmap[key] > 1:
                return True
        return False
                
        



# Solution C: Sorted the list and use two pointers to find the sum
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.strings = [] 
        self.is_sorted = False

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.strings.append(number)
        self.is_sorted = False #Q: Why can't I un-comment this line?
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if not self.is_sorted:
            self.strings.sort()
            self.is_sorted = True
            
        # Two pointers
        left, right = 0, len(self.strings) - 1

        while left < right:
            total = self.strings[left] + self.strings[right]
            if total == value:
                return True
            elif total > value:
                right -= 1
            elif total < value:
                left += 1
        return False




# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
