def two_sum(input:List[Int], target:Int) : (Int, Int) = {
    var result = (0,0)
    var stop = false
    for (i <- 0 to input.length -2; a = input(i) if !stop)
        for (j <- i + 1 to input.length -1; b = input(j) if !stop)
            if (a + b == target) {
                result = (a, b)
                stop = true
            }
    return result
}