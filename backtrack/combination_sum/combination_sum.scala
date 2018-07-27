import scala.collection.mutable.ListBuffer

def dfs(nums: Array[Int], target: Int, index: Int, path: ListBuffer[Int], res: ListBuffer[ListBuffer[Int]]): Unit = {
  if (target == 0) {
    res += path
    return
  }
  for (i <- index to nums.length-1) {
    val next = target - nums(i)
    if (next < 0) {
      return
    }
    dfs(nums, next, i, path ++ ListBuffer[Int](nums(i)), res)
  }
}
def solve(candidates: Array[Int], target: Int): ListBuffer[ListBuffer[Int]] = {
  val res = new ListBuffer[ListBuffer[Int]]()
  val sorted_candidates = candidates.sorted
  dfs(sorted_candidates, target, 0, new ListBuffer[Int](), res)
  res
}
var a = Array(2, 3, 6, 7)
println(solve(a, 7))  // should be [[2, 2, 3], [7]]
