def tupleToString(t:(Int,Int)):String = {
    return t match {
        case (a:Int, b:Int) if a != b => a + "->" + b
        case (a:Int, b:Int) if a == b => a.toString 
    }
}

def summary_ranges(input:List[Int]) : List[String] = {
    var ranges = List[String]()
    var t = (input(0), input(0))
    for (i <- 1 until input.length; v = input(i)){
        if (v == t._2 + 1) 
            t = (t._1, v)
        else {
            ranges = ranges :+ tupleToString(t)
            t = (v, v)
        }
    }    
    ranges = ranges :+ tupleToString(t)
    return ranges
}