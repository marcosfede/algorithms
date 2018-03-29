package main

import (
	"fmt"
	"strconv"
	"strings"
)

func product(arr []string, repeat int) [][]string {
	if repeat == 1 {
		var sol [][]string
		for _, e := range arr {
			sol = append(sol, []string{e})
		}
		return sol
	}
	var solution [][]string
	for _, el := range arr {
		for _, prod := range product(arr, repeat-1) {
			solution = append(solution, append([]string{el}, prod...))
		}
	}
	return solution
}

func eval(num string) int {
	var splitted []string
	splitted = strings.Split(num, "+")
	if len(splitted) > 1 {
		total := 0
		for _, block := range splitted {
			total += eval(block)
		}
		return total
	}
	splitted = strings.Split(num, "-")
	if len(splitted) > 1 {
		total := eval(splitted[0])
		for _, block := range splitted[1:] {
			total -= eval(block)
		}
		return total
	}
	splitted = strings.Split(num, "*")
	if len(splitted) > 1 {
		total := 1
		for _, block := range splitted {
			total *= eval(block)
		}
		return total
	}
	numInt, _ := strconv.Atoi(num)
	return numInt
}

func solve(num string, target int) []string {
	n := len(num)
	var solutions []string
	for _, comb := range product([]string{"", "+", "*", "-"}, n-1) {
		var solution []string
		for i := 0; i < n-1; i++ {
			solution = append(solution, string(num[i]))
			solution = append(solution, comb[i])
		}
		solution = append(solution, string(num[n-1]))
		solutionStr := strings.Join(solution, "")
		if eval(solutionStr) == target {
			solutions = append(solutions, solutionStr)
		}
	}
	return solutions
}

func main() {
	fmt.Println(solve("123", 6))
	fmt.Println(solve("232", 8))
	fmt.Println(solve("123045", 3))
	fmt.Println(solve("105", 5))
}
