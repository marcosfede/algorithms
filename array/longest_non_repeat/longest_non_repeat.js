function longestNonRepeat(s) {
  let start = 0
  let maxlen = 0
  const usedChar = new Map()
  s.split('').forEach((char, i) => {
    if (usedChar.has(char) && start <= usedChar.get(char)) {
      start = usedChar.get(char) + 1
    } else {
      maxlen = Math.max(maxlen, i + 1 - start)
    }
    usedChar.set(char, i)
  })
  return maxlen
}

const a = 'abcabcdefbb'
console.log('input: ', a)
console.log('result: ', longestNonRepeat(a))
console.log('output should be 6')
