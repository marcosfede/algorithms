function threeSum(nums) {
    const res = []
    nums.sort()
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue
        }
        let l = i + 1
        let r = nums.length - 1
        while (l < r) {
            const s = nums[i] + nums[l] + nums[r]
            if (s > 0) {
                r -= 1
            }
            else if (s < 0) {
                l += 1
            } else {
                res.push([nums[i], nums[l], nums[r]])
                while (l < r && nums[l] === nums[l + 1]) {
                    l++
                }
                while (l < r && nums[r] === nums[r - 1]) {
                    r -= 1
                }
                l++
                r--
            }
        }
    }
    return res
}

const x = [-1, 0, 1, 2, -1, -4]
console.log("input: ", x)
console.log("output should be: ", [[-1, -1, 2], [-1, 0, 1]])
console.log("output: ", threeSum(x))
