function mergeIntervals(arr) {
    arr.sort((a, b) => a.start - b.start)
    const newArr = [arr[0]]
    for (const i of arr.slice(1)) {
        const last = newArr.slice(-1)[0]
        if (i.start > last.end) {
            newArr.push(i)
        } else {
            newArr[newArr.length - 1] = {
                start: last.start,
                end: Math.max(i.end, last.end)
            }
        }
    }
    return newArr
}

const given = [[1, 3], [2, 6], [8, 10], [15, 18]]
const givenObj = given.map((interv) => ({
    start: interv[0],
    end: interv[1]
}))
const expected = [[1, 6], [8, 10], [15, 18]]
console.log("input: ", given)
console.log("result: ", mergeIntervals(givenObj).map(i => [i.start, i.end]))
console.log("output should be: ", expected)
