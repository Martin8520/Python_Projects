def canCompleteCircuit(gas, cost):
    total_gas = 0
    total_cost = 0
    tank = 0
    start_index = 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        if tank < 0:
            start_index = i + 1
            tank = 0

    return start_index if total_gas >= total_cost else -1


gas1 = [1, 2, 3, 4, 5]
cost1 = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas1, cost1))  # 3

gas2 = [2, 3, 4]
cost2 = [3, 4, 3]
print(canCompleteCircuit(gas2, cost2))  # -1
