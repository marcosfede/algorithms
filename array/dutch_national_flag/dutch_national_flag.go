package main

import "fmt"

func dutchNationalFlag(arr []int) {
    low, mid, high := 0, 0, len(arr)-1

    for mid <= high {
        switch arr[mid] {
        case 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low++
            mid++
        case 1:
            mid++
        case 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high--
        }
    }
}

func main() {
    arr := []int{2, 0, 1, 2, 1, 0}
    dutchNationalFlag(arr)
    fmt.Println(arr)  // Should print: [0 0 1 1 2 2]
}
