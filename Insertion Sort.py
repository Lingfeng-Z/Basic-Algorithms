class Solution():
    # data: a list of integers
    def InsertionSort(self, data):
        i = 1
        while i < len(data):
            key = data[i]
            j = i-1
            while j >= 0 and data[j] > key:
                data[j+1] = data[j]
                data[j] = key
                j -= 1
            i += 1
        return data


if __name__ == "__main__":
    s = Solution()
    result = s.InsertionSort(list(map(int,input().split(','))))
    print (result)