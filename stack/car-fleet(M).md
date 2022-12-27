# Intuition
Stack and physics

# Approach
The main idea here is we can determine the amount of time it takes for a car to reach the finish line based on its current position and speed. We sort the positions from lowest (furthest from finish) to highest (closest to finish)

Lets say the first car we look at takes 5 seconds. We will push that value onto a stack. Lets now consider scenarios for the second car, which is AHEAD of the first car. 

If the second car takes more than or equal to 5 seconds to finish, the first car will catch up to it and form a fleet. So, we can pop the first car's time off the stack and put the second car's time on the stack, since it is the deciding factor for the speed of the fleet. In a more general sense, we can pop all the previous cars/fleets that are going faster than the current car, as they will all form one giant fleet. Once that it is finished, we can push the time of the current car on the stack, since it decides the speed of the fleet.

If the second car takes less than 5 seconds to finish, the first car will never catch up to it, and a new fleet will never be formed. So, we can push this car's time onto the stack and essentially form a new fleet consisting of itself. This also applies to a more general sense, where we can just push the current car's time onto the stack if it will finish before the car/fleet behind it.

At the end, the number of times on the stack will be the number of different fleets that exist.

# Complexity
- Time complexity: $O(nlogn)$ due to sorting
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$ for stack, which is worse case if every car forms its own fleet
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed.sort()
        stack = []

        for pos, spd in pos_speed:
            time_to_finish = (target - pos) / spd
            while len(stack) != 0 and time_to_finish >= stack[-1]:
                stack.pop()
            stack.append(time_to_finish)

        return len(stack)
```
