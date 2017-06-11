permutations [] = [[]]
permutations t@(x:xs) = let ixs = zip [1..] t
                            partialLists = map (\(i,v) -> (v, map snd $ filter ((/= i) . fst) ixs)) ixs
                        in concatMap (\ (v, ys) -> map (v:) (permutations ys)) partialLists

main = print $ permutations [1..9]