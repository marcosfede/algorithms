package main

import "fmt"
import "strconv"

func summaryRanges(nums []int) []string {
	var res []string
	l := len(nums)
	if l == 1 {
		return []string{strconv.Itoa(nums[0])}
	}
	i := 0
	for i < l {
		start := nums[i]
		for i+1 < l && nums[i+1]-nums[i] == 1 {
			i++
		}
		if nums[i] != start {
			res = append(res, strconv.Itoa(start)+"->"+strconv.Itoa(nums[i]))
		} else {
			res = append(res, strconv.Itoa(start))
		}
		i++
	}
	return res
}

func main() {
	a := []int{0, 1, 2, 4, 5, 7}
	fmt.Println("input: ")
	fmt.Println(a)
	fmt.Println("output should be")
	fmt.Println([]string{"0->2", "4->5", "7"})
	fmt.Println("output: ")
	fmt.Println(summaryRanges(a))
}
