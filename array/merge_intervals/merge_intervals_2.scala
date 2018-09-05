object MergeIntervals extends App {

  def time[R](block: => R): R = {
    val t0 = System.currentTimeMillis()
    val result = block // call-by-name
    val t1 = System.currentTimeMillis()
    println("Elapsed time: " + (t1 - t0) + "ns")
    result
  }

  implicit val orderRanges: Ordering[Range] = {
    new Ordering[Range] {
      def compare(x: Range, y: Range): Int = {
        (x, y) match {
          case (_, _) if x.head < y.head => -1
          case (_, _) if x.head > y.head => 1
          case _ => 0
        }
      }
    }
  }

  trait Overlap[Range] {
    def overlap(a: Range): Boolean
  }

  implicit class RangeOps[A](a: Range) {
    def overlap(implicit b: Range): Boolean = {
      (a, b) match {
        case (_, _) if a.last < b.head => false
        case _ => true
      }
    }
  }

  def mergeIntervals(input: Vector[Range]): Vector[Range] = {
    input.sorted.foldLeft[Vector[Range]](Vector())((acc: Vector[Range], next: Range) => {
      acc.lastOption match {
        case None => Vector(next)
        case Some(value) if value.overlap(next) && next.last > value.last => {
          Vector(Range(value.head, next.last) union acc.diff(Vector(value))
        }
        case Some(value) if value.overlap(next) && next.last <= value.last => acc
        case Some(value) => acc union Vector(next)
      }
    })
  }

  val input = Vector(1 to 3, 2 to 6, 8 to 10, 8 to 10, 15 to 18)
  val output = time {
    mergeIntervals(input)
  }
  
  println(s" Los intervalos resultantes son: ${output.sorted}")
}

// For example, Given [1,3],[2,6],[8,10],[15,18], return [1,6],[8,10],[15,18].
