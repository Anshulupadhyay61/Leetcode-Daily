class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        original = [first]

        for i in range(len(encoded)):
            next_value = original[i] ^ encoded[i]
            original.append(next_value)

        return original