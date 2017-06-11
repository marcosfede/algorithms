package main

import (
	"fmt"
	"sync"
)

func multiperm(word string) []string {
	var list []string
	var wg sync.WaitGroup
	wg.Add(len(word))
	for i, l := range word {
		go func(i int, l rune) {
			defer wg.Done()
			subperm := perm(word[:i] + word[i+1:])
			for _, c := range subperm {
				list = append(list, string(l)+c)
			}
		}(i, l)
	}
	wg.Wait()
	return list
}
func perm(word string) []string {
	if len(word) <= 1 {
		return []string{word}
	}
	var list []string
	for i, l := range word {
		subperm := perm(word[:i] + word[i+1:])
		for _, c := range subperm {
			list = append(list, string(l)+c)
		}
	}
	return list
}
func main() {
	word := "abcdefghi"
	fmt.Println(multiperm(word))
}
