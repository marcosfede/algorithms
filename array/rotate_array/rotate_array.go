package main

import "fmt"


func rotate (arr []int, k int) []int {
	n := len(arr)
	k = k % n
	return append(arr[n-k:], arr[:n-k]...)
}

func main () {
	a := []int{1, 2, 3, 4, 5, 6, 7}
	fmt.Println("in: ", a)
	fmt.Println("expected: ", []int{5, 6, 7, 1, 2, 3, 4})
	fmt.Println("out: ", rotate(a, 3))
}