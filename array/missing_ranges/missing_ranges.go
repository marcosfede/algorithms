package main

import "fmt"

func missingRanges(arr []int, low int, hi int) {
	hashed := make(map[int]bool)
	for _, i := range arr {
		hashed[i] = true
	}
	for n := low; n < hi; n++ {
		if _, ok := hashed[n]; !ok {
			fmt.Print(n)
			fmt.Print(" ")
		}
	}
}

func main() {
	inpt := []int{10, 12, 11, 15}
	low, hi := 10, 15
	fmt.Println("input: ", inpt)
	fmt.Print("result: ")
	missingRanges(inpt, low, hi)
}
