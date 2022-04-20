class SparseVector:
    def __init__1(self, elements):
        """ Store the vector elements efficiently,
        Only when element is non zero, since only those elements will potentially contribute
        towards the dot product.
        Hence using a hash map.
        """
        self.elements = {index: value for index, value in enumerate(elements) if value}

    def __init__(self, elements):
        self.elements = [(index, value) for index, value in enumerate(elements) if value]

    def dot_product_o(self, vector):
        """
        :param vector:
        :return: dot product result
        Time complexity : O(N)
        """
        result = sum(value * vector.elements[index]
                     for index, value in self.elements.iteritems()
                     if index in vector.elements)
        return result

    def dot_product(self, vector):
        """
        More efficient implementation with non zero tuple of index/element,
        when your hash function is not efficient.
        :param vector:
        :return:
        Time Complexity: O(N + M)
        """
        result, left, right = 0, 0, 0
        while left < len(self.elements) and right < len(vector.elements):
            left_idx, left_num = self.elements[left]
            right_idx, right_num = vector.elements[right]

            if left_idx == right_idx:
                result += (left_num * right_num)
                left += 1
                right += 1
            elif left_idx > right_idx:
                right += 1
            else:
                left += 1
        return result


if __name__ == '__main__':
    nums1, nums2 = [1, 0, 0, 2, 3], [0, 3, 0, 4, 0]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)

    print(v1.dot_product(v2))






