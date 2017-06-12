package main

import (
	"fmt"
)

func permconc(word string, ch chan string) {
	defer close(ch)
	if len(word) <= 1 {
		ch <- word
		return
	}
	c := make(chan string)
	go permconc(word[1:], c)
	for per := range c {
		for i := 0; i < len(word); i++ {
			ch <- per[:i] + word[0:1] + per[i:]
		}
	}
}
func permsingle(word string) []string {
	if len(word) <= 1 {
		return []string{word}
	}
	var res []string
	for _, per := range permsingle(word[1:]) {
		for i := 0; i < len(word); i++ {
			res = append(res, per[:i]+word[0:1]+per[i:])
		}
	}
	return res
}

func main() {
	word := "abcdefghi"
	// ch := make(chan string)
	// go perm(word, ch)
	// var results []string
	// for perm := range ch {
	// 	results = append(results, perm)
	// }
	// fmt.Println(len(results))
	fmt.Println(len(permsingle(word)))
}
