'''
Here's the algorithm for constructing the postorder traversal from the given preorder traversal:

- Initialize an empty stack.
- Initialize an empty list to store the postorder traversal.
- Push the root node of the tree onto the stack.
- While the stack is not empty:
-     Pop the top node from the stack and add it to the postorder traversal list.
-     If the popped node has a right child, push the right child onto the stack.
-     If the popped node has a left child, push the left child onto the stack.
- Reverse the postorder traversal list to get the final postorder traversal sequence.
- Return the postorder traversal list.
'''

def constructPostorder(preorder):
    if not len(preorder): return None

    stack, postorder = preorder[0], []


    while stack:
        node = stack.pop(0)
        postorder.append(node.val)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)
