import Data.List

longest_non_repeat str = let sequences n xs = filter ((==n) . length) $ takeWhile (not . null) $ map (take n) $ iterate (drop 1) xs                             
                             allSequences = map (\n -> sequences n str) [1..(length str)]                             
                             nonRepeats = filter (not . null) $ map (\xs -> filter (\x -> x == nub x) xs) allSequences
                             longest xs = head $ filter (\x -> length x == (maximum $ map length xs)) xs
                             longestStr = longest $ map longest nonRepeats
                         in longestStr

