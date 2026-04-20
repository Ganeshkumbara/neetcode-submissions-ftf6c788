class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = sorted(
            [[p,s] for p, s in zip(position, speed)], reverse=True
            )

        time_taken = [(target-p)/s for p, s in position_speed]

        fleets = []

        for time in time_taken:
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        
        return len(fleets)