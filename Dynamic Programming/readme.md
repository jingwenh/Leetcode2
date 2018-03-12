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
## 动态规划四要素
* 状态
* 状态转移方程
* 初始化：最小的状态
* 终点：最大的状态
## Example: Triangle (DP Top-down approach)
* 状态： f[i][j]表示从(0, 0)到(i, j)的最短距离
* 状态转移方程：   
    左边：f[i][0] = f[i - 1][0] + triangle[i][0]
    右边：f[i][i] = f[i - 1][i - 1] + triangle[i][i]  
    中间：f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]   
    注意：计算dp[i][j]时每个节点只能计算一次，一定要记得跳过已经得到状态了的节点（比如说初始化过了，或者先算了左边右边，算中间的时候不能再算第二次）
* 初始化：f[0][0] = triangle[0][0]
* 终点：min(f[-1])
   
