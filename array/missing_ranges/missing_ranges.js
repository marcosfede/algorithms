function missingRanges(arr, lo, hi) {
    const hashed = new Set(arr)
    for (let n = lo; n < hi; n++) {
        if (!hashed.has(n)) {
            console.log(n)
        }
    }
}

const inpt = [10, 12, 11, 15]
const low = 10
const hi = 15
console.log("input: ", inpt)
console.log("result: ")
missingRanges(inpt, low, hi)