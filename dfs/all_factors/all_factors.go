package main

import "fmt"

func getFactors(n int) [][]int {
  ans := [][]int{}
  stack := []int{}
  x := 2

  for {
    if x > n / x {
      if len(stack) == 0 {
        return ans
      }
      ans = append(ans, append(stack, n))
      x = stack[len(stack)-1]
      stack = stack[:len(stack)-1]
      n *= x
      x++
    } else if n % x == 0 {
      stack = append(stack, x)
      n /= x
    } else {
      x++
    }
  }
}

func main() {
  fmt.Printf("%v\n", getFactors(32))
}
