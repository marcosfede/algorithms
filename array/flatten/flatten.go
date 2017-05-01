package main

import "fmt"

func listFlatten(l []interface{}) []int {
	var pv []int
	for _, cv := range l {
		switch t := cv.(type) {
		case int:
			pv = append(pv, t)
		case []interface{}:
			pv = append(pv, listFlatten(t)...)
		default:
			panic("unexpected type")
		}
	}
	return pv
}

func main() {
	// a = [2, 1, [3, [4, 5], 6], 7, [8]]
	// empty interface is needed to avoid type checking
	a := []interface{}{2, 1, []interface{}{3, []interface{}{4, 5}, 6}, 7, []interface{}{8}}
	fmt.Println(listFlatten(a))
	fmt.Println("output should be [2, 1, 3, 4, 5, 6, 7, 8]")
}
