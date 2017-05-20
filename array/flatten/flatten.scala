// input = List(2, 1, List(3, List(4, 5), 6), 7, List(8))

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