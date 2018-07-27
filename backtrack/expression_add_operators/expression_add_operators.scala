import scala.collection.mutable.ListBuffer

def product(arr: List[String], repeat: Int): List[List[String]] = repeat match {
  case 1 => for (el <- arr) yield List(el)
  case _ => for (el <- arr; prod <- product(arr, repeat - 1)) yield el :: prod
}

def eval(string: String): Int = {
  var splitted = string.split("\\+")
  if (splitted.length > 1) {
    return splitted.map(eval).sum
  }
  splitted = string.split("\\-")
  if (splitted.length > 1) {
    return -1*splitted.map(eval).sum + 2*eval(splitted(0))
  }
  splitted = string.split("\\*")
  if (splitted.length > 1) {
    return splitted.map(eval).product
  }
  string.toInt
}

def solve(num: String, target: Int): List[String] = {
  val operators = List[String]("", "+", "-", "*")
  val n = num.length
  product(operators, n - 1)
    .map(comb => {
      val solution = ListBuffer[String]()
      for (i <- 0 until n - 1) {
        solution.append(num(i).toString)
        solution.append(comb(i))
      }
      solution += num.last.toString
      solution.toList.mkString("")
    })
    .filter(sol => eval(sol) == target)
}


// "123", 6 -> ["1+2+3", "1*2*3"]
println(solve("123", 6))

// "232", 8 -> ["2*3+2", "2+3*2"]
println(solve("232", 8))

// "123045", 3 -> ['1+2+3*0*4*5', '1+2-3*0*4*5', '1*2+3*0-4+5', '1*2-3*0-4+5', '1-2+3+0-4+5', '1-2+3-0-4+5']
println(solve("123045", 3))

println(solve("105", 5))
