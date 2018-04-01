def product(arr: List[String], repeat: Int): List[List[String]] = repeat match {
  case 1 => for (el <- arr) yield List[String](el)
  case _ => for (el <- arr; prod <- product(arr, repeat - 1)) yield List[String](el) ++ prod
}

def solve(num: String, target: Int): List[List[String]] = {
  val operators = List[String]("", "+", "-", "*")
  product(operators, 3)
}



// "123", 6 -> ["1+2+3", "1*2*3"]
println(solve("123", 6))

// "232", 8 -> ["2*3+2", "2+3*2"]
println(solve("232", 8))

// "123045", 3 -> ['1+2+3*0*4*5', '1+2-3*0*4*5', '1*2+3*0-4+5', '1*2-3*0-4+5', '1-2+3+0-4+5', '1-2+3-0-4+5']
println(solve("123045", 3))

println(solve("105", 5))
