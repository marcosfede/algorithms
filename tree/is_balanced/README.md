A tree is only balanced if:

The left and right subtrees' heights differ by at most one, AND
The left subtree is balanced, AND
The right subtree is balanced

     A
   /   \
  B     C  
 /     / \  
D     E   F  
     /  
    G  
The next one is not balanced because the subtrees of C differ by 2 in their height:

     A
   /   \
  B     C   <-- difference = 2
 /     /
D     E  
     /  
    G  

Write an algorithm to find if a tree is balanced