package main

import (
	"io/ioutil"
	"strconv"
	"strings"
)

func calcTotalFuel(mass int) int {
	fuel := calcFuel(mass)
	if fuel <= 0 {
		return 0
	}
	return fuel + calcTotalFuel(fuel)
}

func calcFuel(mass int) int {
	return (mass / 3) - 2
}

func castToInts(vs []string) []int {
	arr := make([]int, len(vs))
	for i, v := range vs {
		casted, _ := strconv.Atoi(v)
		arr[i] = casted
	}
	return arr
}

func main() {
	content, _ := ioutil.ReadFile("./input.txt")
	masses := castToInts(strings.Split(string(content), "\n"))

	// p1
	p1sum := 0
	for _, v := range masses {
		p1sum += calcFuel(v)
	}
	println(p1sum)

	// p2
	p2sum := 0
	for _, v := range masses {
		p2sum += calcTotalFuel(v)
	}
	println(p2sum)

}
