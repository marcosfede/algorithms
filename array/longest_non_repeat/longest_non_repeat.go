package main

import "fmt"

func longestNonRepeat(s string) int {
	start, maxlen := 0, 0
	usedChar := make(map[string]int)
	for i, r := range s {
		// r holds a "rune" type, need to convert to string
		char := string(r)
		if val, ok := usedChar[char]; ok && start <= val {
			start = val + 1
			// go has no ternary or built int max
		} else if maxlen <= i+1-start {
			maxlen = i + 1 - start
		}
		usedChar[char] = i
	}
	return maxlen
}

func main() {
	a := "abcabcdefbb"
	fmt.Println("input: ", a)
	fmt.Println("result: ", longestNonRepeat(a))
	fmt.Println("output should be 6")
}
