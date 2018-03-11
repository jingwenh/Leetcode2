# Dynamic Programming
## 可能要使用DP的情况
在所有方案中：
* 求最大最小值
* 判断方案是否可行
* 统计（某种）方案个数
## 极不可能使用DP的情况
* 求出所有具体方案（通常是用DFS或者BFS）
* 输入的是集合而不是序列（除了背包问题）
* 暴力解的时间复杂度已经是多项式级别（DP通常是将exponential或factorial的时间复杂度优化到polynomial）
