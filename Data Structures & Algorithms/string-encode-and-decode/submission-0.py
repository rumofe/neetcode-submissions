class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for palabras in strs:
            encoded_string += str(len(palabras)) + "#" + palabras 
        print(encoded_string)
        return(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            pos_hash = s.index("#", i)
            longitud = int(s[i:pos_hash])
            palabra = s[pos_hash + 1 : pos_hash + 1 + longitud]
            decoded_strs.append(palabra)
            i = pos_hash + 1 + longitud
        return decoded_strs