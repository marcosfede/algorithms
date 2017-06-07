-- subsets :: [a] -> [[a]]
subsets [] = [[]]
subsets (x:xs) = let ys = subsets xs
				 in (map (x:) ys) ++ ys
				 
 


