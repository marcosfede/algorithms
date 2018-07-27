function plusOne(digits) {
  const n = digits.length
  for (let i = n - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i]++
      return digits
    }
    digits[i] = 0
  }
  const newNum = Array(n + 1).fill(0)
  newNum[0] = 1
  return newNum
}

const a = [8, 8, 9]
console.log('input', a)
console.log('output', plusOne(a))

const b = [9, 9, 9, 9]
console.log('input', b)
console.log('output', plusOne(b))
