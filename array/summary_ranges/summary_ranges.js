function summary_ranges(nums) {
    res = []
    const l = nums.length
    if (l == 1) {
        return [str(nums[0])]
    }
    let i = 0
    while (i < l) {
        let start = nums[i]
        while (i + 1 < l && nums[i + 1] - nums[i] == 1) {
            i++
        }
        if (nums[i] != start) {
            res.push(start.toString() + "->" + nums[i].toString())
        } else {
            res.push(start.toString())
        }
        i++
    }
    return res
}

const a = [0, 1, 2, 4, 5, 7]
console.log("input: ")
console.log(a)
console.log("output should be")
console.log(["0->2", "4->5", "7"])
console.log("output: ")
console.log(summary_ranges(a))