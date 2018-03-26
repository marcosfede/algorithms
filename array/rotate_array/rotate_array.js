function rotate(arr, k) {
    const n = arr.length
    k = k % n
    return arr.slice(n - k).concat(arr.slice(0, n - k))
}


a = [1, 2, 3, 4, 5, 6, 7]
console.log("in: ", a)
console.log("expected: ", [5, 6, 7, 1, 2, 3, 4])
console.log("out: ", rotate(a, 3))