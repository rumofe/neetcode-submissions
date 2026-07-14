class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = {}
        for palabra in strs:
            huella = ''.join(sorted(palabra))
            if huella not in grupos:
                grupos[huella] = []
            grupos[huella].append(palabra)
        return list(grupos.values())