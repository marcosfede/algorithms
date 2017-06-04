def findMatch(interval:(Int, Int), intervals:Array[(Int, Int)]) : Option[Int] = {
    var matchFound = false
    var result:Option[Int] = None
    for (i <- 0 until intervals.length; t = intervals(i) if !matchFound){
        matchFound = !((t._2 < interval._1) || (interval._2 < t._1))
        if (matchFound) result = Some(i)
    }
    return result
}

def merge_intervals(input: List[(Int,Int)]) : List[(Int, Int)] = {
    var result = Array[(Int, Int)]()
    for (i <- 0 until input.length; interval = input(i)) {
        val best = findMatch(interval, result)
        best match {
            case None => result = result :+ interval            
            case Some(i) => result(i) = (math.min(interval._1, result(i)._1), math.max(interval._2, result(i)._2))
        }    
    }
    return result.toList    
}

