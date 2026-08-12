class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = sum(tickets) - tickets[k]
        time = 0
        if k > len(tickets):
            return -1
        else:
            for i,t in enumerate(tickets):
                if i<= k:
                    time += min(t, tickets[k])
                else:
                    time += min(t, tickets[k] -1) 
        return time