
def array_to_string(array):
    temp_array = f""
    for x in array:
        temp_array = temp_array + "[" + str(x) + "]"
    if array == []:
        return f"[ ]"
    else:
        return temp_array


class Sort:
    def __init__(self, array, name):
        self.array = array
        self.name = name

    def set_array(self, array):
        self.array = array

    def get_array(self):
        return self.array

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def __str__(self):
        temp_array = f"{self.name}"
        for x in self.array:
            temp_array = temp_array + "[" + str(x) + "]"
        return temp_array

    def quick_sort(self, array = None):
        if array is None:
            array = self.array

        if len(array) < 2: # Base Case
            return array

        pivot = array[-1]
        left = []
        right = []

        for x in array[:-1]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        #print(f"{array_to_string(left)} < [{pivot}] > {array_to_string(right)}")

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    def insertion_sort(self):
        array = self.array.copy()
        for x in range(1, len(array)):
            y = x
            while y > 0 and array[y] < array[y - 1]:
                array[y], array[y - 1] = array[y - 1], array[y]
                y -= 1
        return array

    def merge_sort(self, array = None):
        def merge(left, right):
            result = []
            x = y = 0

            # Compare elements from left and right
            while x < len(left) and y < len(right):
                if left[x] <= right[y]:
                    result.append(left[x])
                    x += 1
                else:
                    result.append(right[y])
                    y += 1

            # Append remaining elements
            result.extend(left[x:])
            result.extend(right[y:])
            #print(array_to_string(result))
            return result

        if array is None:
            array = self.array.copy()
        if len(array) <= 1: # base case
            return array

        # Step 1: Divide
        mid = len(array) // 2
        left_half = self.merge_sort(array[:mid])
        right_half = self.merge_sort(array[mid:])

        # Step 2: Merge
        #print(f"{array_to_string(left_half)} < > [{array_to_string(right_half)}]")
        return merge(left_half, right_half)

    def bubble_sort(self):
        array = self.array.copy()
        count = 0
        passes = 0
        while count < len(array):
            count = 0
            for x in range(len(array)):
                if x != len(array) - 1 and array[x] > array[x + 1]:
                    array[x], array[x + 1] = array[x + 1], array[x]
                else:
                    count += 1
            passes += 1
            #print(f"Pass {passes}: {array}")
        return array