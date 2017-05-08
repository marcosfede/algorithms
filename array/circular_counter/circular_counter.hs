-- circular_counter :: [a] -> [a]
circular_counter [] = []
circular_counter [x] = [x]
circular_counter [x,y] = [x,y]
circular_counter xs = let ixs = zip [1..] xs
                          (selection, remainder) = foldl (\ (s,r) p@(i,x) -> if i `mod` 3 == 0 then (p:s, r) else (s, p:r)) ([], []) ixs                                                                             
                          lastIndex = length xs `div` 3 * 3                          
                          (fsthalf, sndhalf) = span (\ (i, x) -> i <= lastIndex) (reverse remainder)
                          sorted_remainder = map snd sndhalf ++ map snd fsthalf
                        in (reverse $ map snd selection) ++ circular_counter sorted_remainder
                        