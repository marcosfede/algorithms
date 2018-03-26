function two_sum(nums, target) {
    const dic = new Map()
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i]
        if (dic.has(num)) {
            return [dic.get(num), i]
        } else {
            dic.set(target - num, i)
        }
    }
}

const arr = [3, 2, 4]
const target = 6
const res = two_sum(arr, target)
console.log(res)
