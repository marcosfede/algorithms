package main

import "fmt"

func twoSum(nums []int, target int) []int {
	dic := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		if idx, ok := dic[num]; ok {
			return []int{idx, i}
		}
		dic[target-num] = i
	}
	return []int{}
}

func main() {
	arr := []int{3, 2, 4}
	target := 6
	res := twoSum(arr, target)
	fmt.Println(res)
}
