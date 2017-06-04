// var input = List(2, 1, List(3, List(4, 5), 6), 7, List(8))

// with guard expressions
def flatten(input:List[Any]):List[Int] = {
    var result = List[Int]()
    for (x <- input){
        x match {
            case _ if x.isInstanceOf[Int] => result = result :+ x.asInstanceOf[Int]
            case _ if x.isInstanceOf[List[Any]] => result = result ++ flatten(x.asInstanceOf[List[Any]])
            case _ => throw new IllegalArgumentException("input can only contain ints or lists of ints, with any level of nesting.")
        }
    }
    return result
}

// with pattern matching
def flatten2(input:List[Any]):List[Int] = {
    var result = List[Int]()
    for (x <- input){
        x match {
            case x:Int => result = result :+ x
            case x:List[Any] => result = result ++ flatten(x)
            case _ => throw new IllegalArgumentException("input can only contain ints or lists of ints, with any level of nesting.")
        }
    }
    return result
}