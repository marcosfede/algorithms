def getFactors(n: Int, i: Int = 2): List[List[Int]] = {
  val up_to = math.floor(math.sqrt(n)).toInt
  val divisors = (for (k <- i to up_to if n % k == 0) yield k).toList
  // calculate al decompositions starting with d
  divisors.flatMap(d => {
    // add n/d to the list of remaining factors
    (List(n / d) :: getFactors(n / d, d))
      // add d to the head of each subcombination
      .map(s => d :: s)
  }
  )
}


println(getFactors(16))
