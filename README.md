<font face='Monaco'>
# 8-puzzle problem

> 1712950 杨添凯

## Goal
* It is played on a 3-by-3 grid with 8 square blocks labeled 1 through 8 and a blank square. Our goal is to rearrange the blocks so that they are in order. It is permitted to slide blocks horizontally or vertically into the blank square.
* Write a program that reads the initial board from standard input and prints to standard output a sequence of board positions that solves the puzzle in the fewest number of moves. Also print out the total number of moves and the total number of states ever enqueued.

## Algorithm

> **Astar**.
> 
> The key is the estimation function **'F = G + H'**.
> 
> **'G'** is the step done here.
>
> Calculate **'H'** by *Manhattan Distance*.
> 
> Every situation of the board is a *'Node'*. Or we can see it as a point in 'finding the shortest path'.
> 
> One step makes four situation. 
> 
> **'Table Open'** comprises all possible *'Nodes'* in the next step. We call them ***Set A***. And **'Tbale Close'** help us exclude unavaliable *'Node'*.
> 
> We choose the cost-minimum *'Node'* as the next selected *'Node'* by finding the smallest ***F***
> 
> If we find the *'Target Node'* in **'Table Open'**, print the path.

## Step
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

## Program

> Python 3.7
> 
> Test:

1. Input message: ![q](/Users/Raymond/Desktop/1.png)
    * Wrong format message: <img src='/Users/Raymond/Desktop/2.png' width=60%>
    * No answer situation: <img src='/Users/Raymond/Desktop/3.png' width=62%>
2. Show the 'path', 'step num' and 'time cost': ![q](/Users/Raymond/Desktop/4.png)<img src='/Users/Raymond/Desktop/5.png' width=50%><img src='/Users/Raymond/Desktop/6.png' width=50%>
3. And I set the max degree of searching (30).

## Problem

> It may speed very long time to get the result in some complex situation. (more the one minute...)
> 
> Can 'estimate function' be more accurate?

## Reflection
1. python中复杂数据结构的‘=’传递的是地址，指向的内存没有变化。
最开始没有使用`copy.deepcopy()`导致class中一些公有变量出乎意料的发生了变化。
2. 最开始Astar算法部分没有使用class，而是用的function。导致一些参数传递非常复杂，已修正。
3. 开始没注意到`list = string.split()`时，list中的元素不是数字，而是字符串。