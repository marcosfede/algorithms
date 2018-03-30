function longestNonRepeat(s) {
    let start = 0
    let maxlen = 0
    const used_char = new Map()
    s.split("").forEach((char, i) => {
        if (used_char.has(char) && start <= used_char.get(char)) {
            start = used_char.get(char) + 1
        } else {
            maxlen = Math.max(maxlen, i + 1 - start)
        }
        used_char.set(char, i)
    })
    return maxlen
}

a = "abcabcdefbb"
console.log("input: ", a)
console.log("result: ", longestNonRepeat(a))
console.log("output should be 6")
