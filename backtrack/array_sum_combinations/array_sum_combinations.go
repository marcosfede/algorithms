package main

import (
	"fmt"
)

// this could be lazy with goroutines
func product(arrs ...[]int) [][]int {
	ans := [][]int{[]int{}}
	for _, arr := range arrs {
		tmp := [][]int{}
		for _, x := range ans {
			for _, y := range arr {
				tmp = append(tmp, append(x, y))
			}
		}
		ans = tmp
	}
	return ans
}

func counter(iterable []int) map[int]int {
	m := make(map[int]int)
	for _, v := range iterable {
		m[v] = m[v] + 1
	}
	return m
}

func sum(iterable []int) int {
	ans := 0
	for _, v := range iterable {
		ans += v
	}
	return ans
}

func sumCombinations(target int, arrs ...[]int) [][]int {
	rest := arrs[0 : len(arrs)-1]
	last := arrs[len(arrs)-1]
	counterLast := counter(last)
	ans := [][]int{}
	for _, combination := range product(rest...) {
		difference := target - sum(combination)
		times, ok := counterLast[difference]
		if ok {
			for i := 0; i < times; i++ {
				ans = append(ans, append(combination, difference))
			}
		}
	}
	return ans
}

func main() {
	A := []int{1, 2, 3, 3}
	B := []int{2, 3, 3, 4}
	C := []int{1, 2, 2, 2}
	target := 7
	result := sumCombinations(target, A, B, C)
	fmt.Println(len(result))
	fmt.Println(result)
}
