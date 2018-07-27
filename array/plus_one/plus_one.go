package main

import "fmt"

func plusOne(digits []int) []int {
	n := len(digits)
	for i := n - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}
	newNum := make([]int, n+1)
	newNum[0] = 1
	for x := 1; x < n+1; x++ {
		newNum[x] = 0
	}
	return newNum
}
func main() {
	a := []int{8, 8, 9}
	fmt.Println("input", a)
	fmt.Println("output", plusOne(a))

	b := []int{9, 9, 9, 9}
	fmt.Println("input", b)
	fmt.Print("output", plusOne(b))
}
