// list to number and back to list
def plus_one(input:List[Int]) : List[Int] = {
    var number = input.foldLeft(0){(t,x) => t * 10 + x}
    number += 1
    var result = List[Int]()
    while (number > 9){
        result = (number % 10) :: result 
        number /= 10
    }
    result = number :: result 
    return result
}

//digit arithmetic over the list
def plus_one2(input:List[Int]): List[Int] = {
    var result = input.toArray
    var stop = false
    for (i <- input.length-1 to 0 by -1 if !stop){
        if (result(i) == 9){
            result(i) = 0
            if (i > 0)
                result(i - 1) += 1
            else
                result = 1 +: result
        }
        else{
            result(i) += 1
            stop = true
        }
    }
    return result.toList
}