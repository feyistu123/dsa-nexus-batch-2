def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ptr1 = len(players) - 1
        ptr2 = len(trainers) - 1
        count_matching = 0
        while ptr1 >= 0 and ptr2 >= 0:
            if players[ptr1] <= trainers[ptr2]:
                count_matching += 1
                ptr1 -= 1
                ptr2 -= 1
            else:
                ptr1 -= 1
        return count_matching
