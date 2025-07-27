class Solution(object):
    def findRestaurant(self, list1, list2):
        result = []
        for i in list1:
            if i in list2:
                result.append(i)

        if len(result) == 1:
            return result

        output = []
        min_value = float('inf')

        for i in result:
            index_sum = list1.index(i) + list2.index(i)
            if index_sum < min_value:
                min_value = index_sum
                output = [i] 
            elif index_sum == min_value:
                output.append(i)

        return output

        
        