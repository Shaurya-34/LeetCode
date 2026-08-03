class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        freq = 1
        for num in nums:
            if num not in track:
                track[num] = 1
            else:
                track[num] += 1 
        track_sorted = dict(sorted(track.items(), key=lambda item: item[1], reverse=True))
        result = list(track_sorted.keys())[:k] 
        return result