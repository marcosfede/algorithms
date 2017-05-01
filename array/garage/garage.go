package main

import "fmt"

type fastList struct {
	arr []int
    // dict for O(1) lookups by value
	indexof map[int]int
	moves int
}
// kind of a constructor for the dict
func (l *fastList) initMap () {
	l.indexof = make(map[int]int)
	for i, v := range l.arr {
		l.indexof[v] = i
	}
}
func (l *fastList) swap (e1 int, e2 int){
	i1 := l.indexof[e1]
	i2 := l.indexof[e2]
	// set element where 0 is to final element
	l.arr[i1] = e2
	// update dict
	l.indexof[e2] = i1
	// set 0 where the previous number was
	l.arr[i2] = e1
	// update dict
	l.indexof[e1] = i2
	l.moves++
}
func (l *fastList) equals (other []int) bool {
	if len(l.arr) != len(other) {
		return false
	}
	for i, v := range l.arr {
		if v != other[i] {
			return false
		}
	}
	return true
}
func (l *fastList) calcMoves (end []int) int {
	l.moves = 0
	for !l.equals(end) {
		i0 := l.indexof[0]
		if end[i0] != 0 {
			l.swap(0, end[i0])
			fmt.Println(l.arr)
			continue
		}
		for ind, el := range l.arr {
			if el != end[ind] {
				l.swap(0, el)
				fmt.Println(l.arr)
				break
			}
		}
	}
	return l.moves
}

func garage (beg []int, end []int) int {
	var l fastList
	l.arr = beg
	l.initMap()
	return l.calcMoves(end)
}

func main () {
	initial := []int{1, 2, 3, 0, 4}
	final := []int{0, 3, 2, 1, 4}
	fmt.Println("initial", initial)
	fmt.Println(garage(initial, final))
	fmt.Println("final should be: ", final)
}