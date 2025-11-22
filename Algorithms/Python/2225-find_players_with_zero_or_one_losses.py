class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = defaultdict(int)

        for match in matches:
            winner , loser =  match

            loss[loser] += 1
            loss[winner]
        
        zero = []
        one = []
        
        for player in sorted(loss):
            if loss[player] == 0:
                zero.append(player)
            
            elif loss[player] == 1:
                one.append(player)

        
        return [zero, one]
       