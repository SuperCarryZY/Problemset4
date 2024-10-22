# CMPS 6610 Problem Set 04
## Answers

**Name:**_______Yan Zhu__________________


Place all written answers from `assignment-05.md` here for easier grading.




- **1d.**

| File           | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length |
|----------------|---------------------|----------------|--------------------------|
| f1.txt         | 1340                | 826            | 0.616                    |
| alice29.txt    | 1039367             | 676374         | 0.65                     |
| asyoulik.txt   | 876253              | 606448         | 0.69                     |
| grammar.lsp    | 26047               | 17356          | 0.66                     |
| fields.c       | 78050               | 56206          | 0.72                     |


The ratio of Huffman coding to fixed-length coding is less than 1 for each file, indicating that Huffman coding is consistently more efficient. The ratios range from 0.616 to 0.72, meaning Huffman coding reduces the encoding cost by about 28% to 38%. In other words, Huffman coding uses fewer bits and saves a significant amount of space.

Regardless of the file content, the ratio between Huffman and fixed-length coding remains below 1, demonstrating the consistent advantage of Huffman coding in terms of compression efficiency.

- **1d.**
If we used Huffman coding on a document where every character has the same frequency, the cost would be about the same as fixed-length encoding. Since all characters appear equally often, Huffman coding wouldn’t be able to assign shorter codes to more frequent characters, so the encoding length for each character would be log_2(n), where  n  is the number of unique characters. This cost would stay consistent across different documents as long as the alphabet size and equal character frequency remain the same.

- **2a.**

We can use a bottom-up approach. Specifically, we first treat the given array as a complete binary tree, where each element of the array represents a node in the tree. Then, starting from the last non-leaf node in the tree, we move upwards, performing a heapify operation on each node. The heapify process involves adjusting the order between the node and its children, ensuring that the parent node’s value is not greater than its children’s values, thereby maintaining the min-heap property for the entire subtree.

Due to the structure of the complete binary tree, nodes near the leaf level have smaller subtree heights, meaning fewer adjustments are needed. On the other hand, nodes closer to the root have larger subtree heights and require more adjustments. However, the number of such nodes is smaller. As a result, the overall heapify process can be completed in  O(n)  time.


- **2b.**


The span of the bottom-up heap construction approach refers to the longest sequence of dependent operations, which limits how quickly the algorithm can complete with unlimited parallel resources. In this case, the span is determined by the depth of the tree, as the longest chain of dependent operations occurs when heapifying from the root to the deepest leaf. Since the height of a binary heap is  O(log n) , the span of this approach is  O(log n) . This represents the time it takes for the longest series of recursive heapify calls to complete, regardless of the number of processors available.

- **3a.**
Let’s consider a greedy strategy for minimizing the number of coins needed to make up  N  dollars, where the available coin denominations are powers of 2.

	1.	At each step, select the largest coin denomination that is less than or equal to  N .
	2.	Subtract that coin’s value from  N , and repeat the process with the remaining amount.
	3.	Continue this until  N  becomes 0.

For example, let’s take  N = 78 . The available coin denominations are  1, 2, 4, 8, 16, 32, 64 .

	•	Start by picking the largest coin less than or equal to 78, which is 64. Now,  N = 78 - 64 = 14 .
	•	The largest coin for  N = 14  is 8, so subtract 8, leaving  N = 14 - 8 = 6 .
	•	For  N = 6 , the largest coin is 4, so subtract 4, leaving  N = 6 - 4 = 2 .
	•	Finally, use a 2-dollar coin to get  N = 2 - 2 = 0 .

Thus, the algorithm uses 4 coins: one 64-dollar coin, one 8-dollar coin, one 4-dollar coin, and one 2-dollar coin.

- **3b.**
To show that this greedy algorithm is optimal, we need to demonstrate the greedy choice property and the optimal substructure property.

	•	Greedy Choice Property: This property means that the first decision—taking the largest possible coin—is the best decision. Since the coins are powers of 2, choosing the largest denomination reduces  N  by the biggest possible amount without overshooting. This minimizes the remaining amount, and we can still make optimal choices for the rest.
	•	Optimal Substructure: Once the largest coin is chosen, the problem reduces to finding the fewest coins for the remaining amount, which is smaller but still follows the same pattern. The smaller problem can be solved the same way—by repeatedly choosing the largest coin—leading to an optimal solution. So, the entire problem is solved optimally by solving these smaller subproblems.

Thus, by repeatedly making the best choice at each step, the algorithm guarantees the smallest number of coins.



- **3c.**
Work: Each time,find the largest coin that fits into  N  and subtract it. Since the denominations are powers of 2, this is related to the number of bits in the binary representation of  N , and thus, the work is  O(log N) , because you’re working with a number of coins proportional to the number of bits in  N .
Span: The span also  O(log N) . Each step of choosing a coin depends on the previous step because you need to reduce  N  before moving to the next coin. Since the number of dependent operations is tied to the number of coins chosen (which is proportional to the number of bits in  N ), the span is also  O(log N) .



- **4a.**

If you have 1, 3, and 4 dollar coins and need to make 6 dollars, the greedy algorithm does not find the optimal solution.
Greedy Algorithm Process:
	•	The greedy algorithm will first choose the largest coin, so it picks a 4-dollar coin, leaving  6 - 4 = 2  dollars.
	•	Then, it picks 1-dollar coin, leaving  2- 1 = 1  dollar.
	•	Finally, it uses a 1-dollar coin to make up the remaining 1 dollar.
The greedy algorithm uses a total of 3 coins (4,1,1).

Actual Optimal Solution:
The optimal solution is to use three 3-dollar coins, which perfectly make up 6 dollars, still using 3 coins but with a more efficient coin selection.Just use 2*3 coins.This example shows that although the greedy algorithm always picks the largest available coin, it does not always find the best coin combination. A different selection of coins can be more effective in solving the problem.

- **4b.**
The coin change problem demonstrates the optimal substructure property, which indicates that the optimal solution to a problem can be derived from the optimal solutions of its subproblems. Specifically, for the coin change problem, this means that if we want to find the minimum number of coins needed to make  N  dollars, we can break this down into smaller subproblems involving amounts less than  N

dp(N）=min(dp(N-D0),dp(N-D2),dp(N-Dk))+1

Base Case:
	For  N = 0 , no coins are needed, so  dp(0) = 0 . This serves as the foundation for our recursive approach.
	2.	Inductive Step:
	Assume dp(N)  has been optimally computed for all amounts  n < N . For amount  N , consider each coin denomination  Di . If we use a coin  Di , the remaining amount is  N - Di .
	Thus, we can express the relationship as:

dp(N）=min(dp(N-D0),dp(N-D2),dp(N-Dk))+1
 The  +1  accounts for the coin  Di  used.
	3.	Conclusion:
	By using the optimal solutions of smaller subproblems  N - Di , we ensure that the solution for  N  is also optimal, demonstrating the optimal substructure property of the problem.

Conclusion:

By utilizing the optimal solutions of the smaller subproblems  N - Di , we ensure that the solution for  N  is also optimal, demonstrating the optimal substructure property of the problem.

- **4c.**
Top-Down Approach

In this approach, we define a recursive function dp(N) to calculate the minimum number of coins needed to make  N  dollars. To avoid redundant calculations, we use a memoization table to store results that have already been computed. Specifically, when we call dp(N), if  N = 0 , it means no coins are needed, so we return 0 directly. If  N < 0 , it indicates that it’s impossible to make that amount, so we return infinity to signify that it cannot be done. For each coin denomination  Di , we recursively calculate the number of coins required, take the minimum value, and store this result in the memoization table for future use.

Bottom-Up Approach

In the bottom-up approach, we create an array dp, where dp[i] represents the minimum number of coins needed to make  i  dollars. We first initialize dp[0] to 0, indicating that no coins are needed to make 0 dollars, while the other values are initialized to infinity. Next, we iterate from 1 to  N , updating the dp array for each amount by considering each coin denomination  D_i  to calculate the required minimum number of coins.

Complexity Analysis

Work: The total work for both methods is  O(N times k) , where  N  is the target amount and  k  is the number of available coin denominations. Each subproblem is computed in constant time since we efficiently handle them through memoization or by filling the dp array iteratively.

Span: In the top-down approach, the span is  O(N)  because, although recursive calls can be processed in parallel to some extent, we ultimately need to wait for all subproblem calculations to complete. In the bottom-up method, the span is also  O(N)  since the calculation for each amount depends on the results of previous amounts, necessitating a sequential filling of the table.
