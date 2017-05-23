def missing_ranges(arr:Array[Int], low:Int, high:Int): List[Int] = {
    var missing = List[Int]()
    val toExclude = arr.toSet
    for (x <- low until high)
        if (!toExclude.contains(x)) 
            missing = missing :+ x
    return missing
}