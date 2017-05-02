package main

import (
	"fmt"
	"sort"
)

type interval struct {
	start int
	end   int
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func mergeIntervals(arr []interval) []interval {
	sort.Slice(arr, func(i, j int) bool {
		return arr[i].end < arr[j].end
	})
	n := []interval{arr[0]}
	for _, i := range arr[1:] {
		last := n[len(n)-1]
		if i.start > last.end {
			n = append(n, i)
		} else {
			n[len(n)-1] = interval{last.start, max(i.end, last.end)}
		}
	}
	return n
}

func main() {
	given := [][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}}
	var givenIntervals []interval
	for _, i := range given {
		givenIntervals = append(givenIntervals, interval{i[0], i[1]})
	}
	expected := [][]int{{1, 6}, {8, 10}, {15, 18}}
	fmt.Println("input: ", given)
	fmt.Println("result: ", mergeIntervals(givenIntervals))
	fmt.Println("output should be: ", expected)
}
