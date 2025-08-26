def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        sums = skill[l] + skill[r]
        while l < r:
            l += 1
            r -= 1
            if sums != skill[l] + skill[r]:
                return -1
        result = 0
        while l < len(skill) and r >= 0:
            result += skill[r] * skill[l]
            l += 1
            r -= 1
        return result
        
