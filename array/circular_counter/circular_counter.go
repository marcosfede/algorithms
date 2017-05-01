package main

import "fmt"

func circCounter(arr []string, skip int){
	index := 0
	for len(arr) > 0 {
		index = (index + skip - 1) % len(arr)
		fmt.Println(arr[index])
		arr = append(arr[:index], arr[index+1:]...) // concat the two sides without a[i]
	}
}

func main () {
	a := []string{"1", "2", "3", "4", "5", "6", "7", "8", "9"}
	circCounter(a, 3)
}