package main

import "fmt"
import "sort"

func threeSum(nums []int) [][]int {
	var res [][]int
	sort.Ints(nums)
	for i := 0; i < len(nums)-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		l := i + 1
		r := len(nums) - 1
		for l < r {
			s := nums[i] + nums[l] + nums[r]
			if s > 0 {
				r--
			} else if s < 0 {
				l++
			} else {
				res = append(res, []int{nums[i], nums[l], nums[r]})
				for l < r && nums[l] == nums[l+1] {
					l++
				}
				for l < r && nums[r] == nums[r-1] {
					r--
				}
				l++
				r--
			}
		}
	}
	return res
}

func main() {
	x := []int{-1, 0, 1, 2, -1, -4}
	fmt.Println("input: ", x)
	fmt.Println("output should be: ", [][]int{{-1, -1, 2}, {-1, 0, 1}})
	fmt.Println("output: ", threeSum(x))
}
