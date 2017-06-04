/*
val input = List(1,2,3,0,4)
val output = List(0,3,2,1,4)
*/

def garage(input:List[Int], output:List[Int]): List[List[Int]] = {
    var result = List[List[Int]]()
    var step = for (i <- input) yield i
    while (step != output){
        val ideal = step.map(output.indexOf)
        val zeroPos = step.indexOf(0)
        val benefit = List.range(0, input.length).map(i => math.abs(i - ideal(i)) - math.abs(zeroPos - ideal(i)))
        val bestPos = benefit.zipWithIndex.filter(_._2 != zeroPos).max._2
        step = step.map(x => x match{
            case _ if x == 0 => step(bestPos)
            case _ if x == step(bestPos) => 0
            case _ => x
        })
        result = result :+ step
    }
    return result
}