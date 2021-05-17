class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))

        def mergeSort(strs):
            if len(strs) <= 1:
                return strs
            low, high = 0, len(strs)
            mid = low + (high - low) // 2
            l = mergeSort(strs[:mid])
            r = mergeSort(strs[mid:])

            i = j = 0
            newArray = []
            while i < len(l) or j < len(r):
                if i == len(l):
                    newArray.append(r[j])
                    j += 1
                elif j == len(r):
                    newArray.append(l[i])
                    i += 1
                elif l[i] + r[j] > r[j] + l[i]:
                    newArray.append(l[i])
                    i += 1
                elif r[j] + l[i] >= l[i] + r[j]:
                    newArray.append(r[j])
                    j += 1

            return newArray

        sortArray = mergeSort(strs)
        if sortArray[0] == "0":
            return "0"
        return "".join(sortArray)


