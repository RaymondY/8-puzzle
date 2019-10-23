# 8-puzzle problem

> 人工智能概论课作业-1
> 
> It is played on a 3-by-3 grid with 8 square blocks labeled 1 through 8 and a blank square. Your goal is to rearrange the blocks so that they are in order. You are permitted to slide blocks horizontally or vertically into the blank square.
> 
> Write a program that reads the initial board from standard input and prints to standard output a sequence of board positions that solves the puzzle in the fewest number of moves. Also print out the total number of moves and the total number of states ever enqueued.
> 
> **The input will consist of the board dimension N followed by the N-by-N initial board position. The input format uses 0 to represent the blank square.**

## 采用Astar算法
1. 建立‘open’和‘close’表. **采用什么数据结构？**
2. F = G + H. **H采用什么评估函数？**
3. *加入判断函数（通过奇偶序列判断是否有解）*
4. 棋盘状态如何表示？**serialization**

> 使用Python，为了进一步熟悉。因为最近需要用，但是我从来没学过。

## 步骤
1. 判断是否有解
2. 建立空的open、close表，将初始状态放入table open
3. 将table open中最小F状态取出，放入table close
    * 若到达目标状态，则结束，此时G即为最少步骤
    * 否则生成下一步所有能转移的状态集S
4. 计算状态集S的所有F = G + H，G取父状态G+1*(使每个节点指向起始状态，便于计算最下步骤)*
    * 若当前状态在table close中，则omit
    * 若在table open中 && new F smaller，则update F = G + H
    * 否则加入table open
5. 返回step 2.

## 结果
基本达成了目的，缺少更多的测试

## 反思
1. python中复杂数据结构的‘=’传递的是地址，指向的内存没有变化。
最开始没有使用`copy.deepcopy()`导致class中一些公有变量出乎意料的发生了变化。
2. 最开始Astar算法部分没有使用class，而是用的function。导致一些参数传递非常复杂，已修正。
3. 开始没注意到`list = string.split()`时，list中的元素不是数字，而是字符串。