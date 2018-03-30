function twoSum(nums, target) {
    const dic = new Map()
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i]
        if (dic.has(num)) {
            return [dic.get(num), i]
        }
            dic.set(target - num, i)

    }
}

const arr = [3, 2, 4]
const target = 6
const res = twoSum(arr, target)
console.log(res)
