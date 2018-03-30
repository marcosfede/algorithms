"use strict"

// Sigh JS ...

// cute two line generator although it reverses order
function* product(head, ...tail) {
    const remaining = tail.length > 0 ? product(...tail) : [[]]
    for (const r of remaining) for (const h of head) yield [h, ...r]
}

function Counter(iterable) {
    const hmap = new Map()
    for (const el of iterable) {
        hmap.set(el, (hmap.get(el) || 0) + 1)
    }
    return hmap
}

const sum = iterable => iterable.reduce((pv, cv) => pv + cv)

function* sumCombinations(target, ...arrs) {
    const last = arrs[arrs.length - 1]
    const rest = arrs.slice(0, -1)
    const counterLast = new Counter(last)
    for (const combination of product(...rest)) {
        const difference = target - sum(combination)
        if (counterLast.has(difference)) {
            const times = counterLast.get(difference).length
            for (let i=0; i< times; i++){
              yield combination.concat(difference)
            }
        }
    }
}

const A = [1, 2, 3, 3]
const B = [2, 3, 3, 4]
const C = [1, 2, 2, 2]
const target = 7

for (const combination of sumCombinations(target, A, B, C)) {
    console.log(combination)
}
