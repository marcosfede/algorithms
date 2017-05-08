-- needed due to Haskell's lack of heterogeneous lists
data Tree a = Leaf a | Node [Tree a] deriving Show 

input = Node [Leaf 2,Leaf 1,Node [Leaf 3,Node [Leaf 4,Leaf 5],Leaf 6],Leaf 7,Node [Leaf 8]]

-- flatten
flatten (Leaf x) = [x]
flatten (Node xs) = concat $ map flatten xs


