class Sort:
    def __init__(self, array):
        self.array = array

    def set_array(self, array):
        self.array = array

    def get_array(self):
        return self.array

    def quick_sort(self, array = None):
        left = []
        right = []
        if array is None:
            array = self.array[:]
        if len(array) < 2:
            return
        pivot = array[-1]
        for index in self.array:
            if index < pivot:
                left.append(index)
            elif index > pivot:
                right.append(index)
        print(f"{left} [{pivot}] {right}")
        return self.quick_sort(left), self.quick_sort(right)
