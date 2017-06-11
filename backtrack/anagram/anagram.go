package main

import (
	"fmt"
	"sync"
)

func perm(word string) []string {
	if len(word) <= 1 {
		return []string{word}
	}
	var list []string
	var wg sync.WaitGroup
	for i, l := range word {
		wg.Add(1)
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

func main() {
	word := "abcdefghi"
	fmt.Println(perm(word))
}
