//just to practice with scala lists
def circular_counter(input:List[Int]):List[Int] = {
    if (input.length < 3) return input
    var selection = List[Int]()
    var remainder = List[Int]()
    var haveToReorder = false //if it is necessary to put the tail of the list at the beginning
    var startingIndex = 0 //where is the tail
    for (i <- 1 to input.length){
        if (i % 3 == 0){
            selection = selection :+ input(i-1)
            haveToReorder = false
        }
        else{
            remainder = remainder :+ input(i-1)
            if (!haveToReorder){
                startingIndex = i-1
                haveToReorder = true
            }
        }
    }
    if (haveToReorder){
        val tail = remainder.slice(startingIndex - 1, remainder.length)
        val head = remainder.slice(0, startingIndex - 1)
        remainder = tail ++ head
    }
    return selection ++ circular_counter(remainder)
}

//same as before but with folds and lambdas
def circular_counter2(input:List[Int]):List[Int] = {
    if (input.length < 3) return input     
    var (selection, remainder) = input.zipWithIndex.foldLeft((List[(Int, Int)](), List[(Int,Int)]())){
        case ((s,r), (x,i)) => if ((i + 1) % 3 == 0) (s :+ (x,i+1), r) else (s, r :+ (x,i+1))
    }
    var lastIndex = selection.last._2
    var (head, tail) = remainder.foldLeft((List[Int](), List[Int]())){
        case ((h,t), (x,i)) => if (i < lastIndex) (h :+ x, t) else (h, t :+ x)
    }
    val remainder2 = tail ++ head
    return selection.map(_._1) ++ circular_counter2(remainder2)
}

//a middle ground between the previous two
def circular_counter3(input:List[Int]):List[Int] = {
    if (input.length < 3) return input
    var selection = List[(Int, Int)]()
    var remainder = List[(Int, Int)]()        
    for (i <- 1 to input.length){
        if (i % 3 == 0) selection = selection :+ (i, input(i-1))                    
        else remainder = remainder :+ (i, input(i-1))                                
    }
    val lastIndex = selection.last._1
    var head = List[Int]()
    var tail = List[Int]()
    for ((i,x) <- remainder){
        if (i < lastIndex) head = head :+ x
        else tail = tail :+ x
    }
    val remainder2 = tail ++ head
    return selection.map(_._2) ++ circular_counter3(remainder2)
}

//a much simpler implementation
def circular_counter4(input:List[Int]): List[Int] = {    
    val N = 3
    var used = Set[Int]()
    var remaining = input.length
    var index = 0
    var result = List[Int]()
    var steps = 0
    while (remaining > 0){        
        if (!used.contains(index)){
            if (steps == N - 1){                
                used += index
                result :+= input(index)
                remaining -= 1
            }
            steps = (steps + 1) % N
        }        
        index = (index + 1) % input.length        
    }
    return result
}