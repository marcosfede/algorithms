def three_sum(input:List[Int]) : List[List[Int]] = {
    var result = Set[List[Int]]()
    for (i <- 0 to input.length -3; a = input(i))
        for (j <- i + 1 to input.length -2; b = input(j))
            for (k <- j + 1 to input.length -1; c = input(k))
                if (a + b + c == 0)
                    result = result + List(a,b,c).sorted
    return result.toList
}