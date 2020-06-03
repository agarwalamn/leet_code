class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost_for_city_a = 0
        diff=[]
        for i in costs:
            cost_for_city_a +=i[0]
            diff.append(i[1]-i[0])
        n = len(costs)//2
        diff.sort()
        for i in range(n):
            cost_for_city_a+=diff[i]
        return cost_for_city_a
