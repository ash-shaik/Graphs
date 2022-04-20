class SparseVector:
    def __init__(self, elements):
        """ Store the vector elements efficiently,
        Only when element is non zero, since only those elements will potentially contribute
        towards the dot product.
        Hence using a hash map.
        """
        self.elements = {index: value for index, value in enumerate(elements) if value}

    def dot_product(self, vector):
        """
        :param vector:
        :return: dot product result
        Time complexity : O(N)
        """
        result = sum(value * vector.elements[index]
                     for index, value in self.elements.iteritems()
                     if index in vector.elements)
        return result
