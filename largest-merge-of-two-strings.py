def largestMerge(self, word1: str, word2: str) -> str:
        ptr1 = 0
        ptr2 = 0
        merge = ""
        while ptr1 < len(word1) and ptr2 < len(word2):
            if word1[ptr1:] > word2[ptr2:]:
                merge += word1[ptr1]
                ptr1 += 1
            else:
                merge += word2[ptr2]
                ptr2 += 1
        merge += word1[ptr1:] + word2[ptr2:]
        return merge
