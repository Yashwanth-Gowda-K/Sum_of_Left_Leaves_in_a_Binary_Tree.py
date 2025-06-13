# Sum_of_Left_Leaves_in_a_Binary_Tree.py

Problem Statement
Given the root of a binary tree, return the sum of all left leaves—leaf nodes that are the left child of their parent.

Example
Input:
     3
    / \
   9  20
     /  \
    15   7
Output: 24 *(9 + 15)*

Approaches
1. Recursive DFS (Depth-First Search)
Idea: Traverse the tree recursively, checking if a node is a left leaf.
Time Complexity: O(n)
Space Complexity: O(h) (h = tree height)

2. Iterative BFS (Breadth-First Search)
Idea: Use a queue to traverse level-by-level, summing left leaves.

Time Complexity: O(n)
Space Complexity: O(m) (m = max nodes in a level)

3. Morris Traversal (O(1) Space)
Idea: Threaded traversal without extra memory (advanced).
Time Complexity: O(n)
Space Complexity: O(1)

Key Concepts
✔ Left Leaf Definition: A node with no children that is its parent’s left child.
✔ Edge Cases: Empty tree, single-node tree, skewed trees.
✔ Tradeoffs:

DFS: Simple but uses call stack.
BFS: Level-order insight, uses queue.
Morris: Memory-optimal but complex.

How to Use
Clone the repository.
Implement the TreeNode structure (provided in code files).
Run the desired solution (DFS/BFS/Morris).

Contributing
Add test cases (edge/normal cases).
Optimize existing solutions.
Propose alternative approaches.
Open a PR with your improvements!
Follow-Up Questions
How would you sum right leaves instead?
Can you solve this iteratively without a queue/stack? (Hint: Morris Traversal)
