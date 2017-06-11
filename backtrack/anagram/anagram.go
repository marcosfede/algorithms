package main

import (
	"fmt"
)
type result struct {
	subperms []string
	letter string
}

func multiperm(word string) []string {
	var list []string
	ch := make(chan result, len(word))
	for i, l := range word {
		go func(i int, l string) {
			ch <- result{perm(word[:i] + word[i+1:]), l}
		}(i, string(l))
	}
	for i := 0; i< len(word); i++ {
		result := <- ch
		for _, p := range result.subperms {
			list = append(list, result.letter + p)
		}
	}
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
	fmt.Println(len(multiperm(word)))
}
