{-
initial: [1, 2, 3, 0, 4]
[0, 2, 3, 1, 4]
[2, 0, 3, 1, 4]
[2, 3, 0, 1, 4]
[0, 3, 2, 1, 4]
4
final should be: [0, 3, 2, 1, 4]

-}

-- getSteps [1, 2, 3, 0, 4] [0, 3, 2, 1, 4]
-- getSteps :: [Int] -> [Int] -> [[Int]]
getSteps initial final | initial == final = []
                       | otherwise = step : (getSteps step final)
                        where iInitial = zip [0..] initial
                              iFinal = zip [0..] final
                              zeroPos = fst $ head $ filter ((==0) . snd) iInitial -- where is zero
                              idealPos = map (\x -> fst $ head $ filter ((==x) . snd) iFinal) initial -- where everyone should be                              
                              benefit = map (\i -> abs(i - (idealPos !! i)) - abs(zeroPos - (idealPos !! i))) [0..length initial-1] -- what advantage if switching places with zero
                              minPos = fst $ head $ filter ((== (maximum benefit)) . snd) $ filter ((/=zeroPos) . fst) $ zip [0..] benefit -- the one with higher advantage, other than zero
                              step = map (\(i,x) -> if i == zeroPos then initial !! minPos else if i == minPos then 0 else x) iInitial --swapping zero and the closer



garage :: [Int] -> [Int] -> IO()
garage initial final = do
    putStrLn ("initial: " ++ (show initial))
    let steps = getSteps initial final
    sequence $ map (\x -> putStrLn $ show x) steps
    print $ length steps
    putStrLn ("final should be: " ++ (show final))