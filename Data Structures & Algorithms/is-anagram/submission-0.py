class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frecuenciasA = {}

        for car in s:
            frecuenciasA[car] = frecuenciasA.get(car, 0) + 1

        frecuenciasB = {}

        for car in t:
            frecuenciasB[car] = frecuenciasB.get(car, 0) + 1


        return frecuenciasA==frecuenciasB
