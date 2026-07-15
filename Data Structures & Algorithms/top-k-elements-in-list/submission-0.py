class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frecuencias = {}
        for num in nums:
            if num in frecuencias:
                frecuencias[num] += 1
            else:
                frecuencias[num] = 1
        aux = []
        for i in range(k):
            top = max(frecuencias, key=lambda x: frecuencias[x])
            aux.append(top)
            frecuencias.pop(top)
        return aux