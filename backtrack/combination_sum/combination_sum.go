package main

import (
	"fmt"
	"sort"
)
// this could actually be parallelizable spawning a new goroutine on recursive call
// need to figure out how to close the channel though...

func recurDfs(nums []int, target int, index int, path []int, res [][]int, ch chan []int) {
	if target == 0 {
		ch <- path
		return
	}
	for i := index; i < len(nums); i++ {
		next := target - nums[i]
		if next < 0 {
			return
		}
		recurDfs(nums, next, i, append(path, nums[i]), res, ch)
	}
}

func dfs(nums []int, target int, index int, path []int, res [][]int, ch chan []int) {
	defer close(ch)
	recurDfs(nums, target, index, path, res, ch)
}

func solve(candidates []int, target int) [][]int {
	var res [][]int
	sort.Ints(candidates)
	ch := make(chan []int)
	go dfs(candidates, target, 0, []int{}, res, ch)
	for elem := range ch {
		res = append(res, elem)
	}
	return res
}

func main() {
	A := []int{2, 3, 6, 7}
	target := 7
	result := solve(A, target)
	fmt.Println(result)
}
