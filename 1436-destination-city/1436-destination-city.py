class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = []

        for i in range (len(paths)):
            source.append(paths[i][0])
        for j in range (len(paths)):
            if paths[j][1] not in source:
                return paths[j][1]