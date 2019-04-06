object MergeIntervals extends App {

  def time[R](block: => R): R = {
    val t0 = System.currentTimeMillis()
    val result = block // call-by-name
    val t1 = System.currentTimeMillis()
    println("Elapsed time: " + (t1 - t0) + "ms")
    result
  }

  implicit val orderRanges = Ordering.by {range: Range => range.head}

  implicit class RangeOps(a: Range) {
    def overlaps(b: Range): Boolean = {
      a.last >= b.head
    }
    def merge(b: Range): Range = {
      val start = Math.min(a.head, b.head)
      val end = Math.max(a.last, b.last)
      start to end
    }
  }

  def mergeIntervals(input: Vector[Range]): Vector[Range] = {
    input.sorted.foldLeft[Vector[Range]](Vector())((acc, next) => {
      acc match {
        case ranges :+ lastRange if lastRange.overlaps(next) => ranges :+ lastRange.merge(next)
        case _ => acc :+ next
      }
    })
  }

  val input = Vector(1 to 3, 2 to 6, 8 to 10, 8 to 10, 15 to 18)
  val output = time {
    mergeIntervals(input)
  }

  assert(output == Vector(1 to 6, 8 to 10, 15 to 18))
}
