function* product(arr, repeat) {
  if (repeat === 1) {
    for (let e of arr) {
      yield [e]
    }
  } else {
    for (let el of arr) {
      for (let prod of product(arr, repeat - 1)) {
        yield [el].concat(prod)
      }
    }
  }
}

function* solve(num, target) {
  const n = num.length
  for (let comb of product(["", "+", "*", "-"], n - 1)) {
    let solution = []
    for (let i = 0; i < n - 1; i++) {
      solution.push(num[i])
      solution.push(comb[i])
    }
    solution.push(num[n - 1])
    solution = solution.join("")
    if (eval(solution) === target) {
      yield solution
    }
  }
}

// "123", 6 -> ["1+2+3", "1*2*3"]
console.log(Array.from(solve("123", 6)))

// "232", 8 -> ["2*3+2", "2+3*2"]
console.log(Array.from(solve("232", 8)))

// "123045", 3 -> ['1+2+3*0*4*5', '1+2-3*0*4*5', '1*2+3*0-4+5', '1*2-3*0-4+5', '1-2+3+0-4+5', '1-2+3-0-4+5']
console.log(Array.from(solve("123045", 3)))

console.log(Array.from(solve("105", 5)))
