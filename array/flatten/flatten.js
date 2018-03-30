function listFlatten(l) {
  return l.reduce((pv, cv) => {
    if (!Array.isArray(cv)) {
      return pv.concat(cv)
    }
    return pv.concat(listFlatten(cv))
  }, [])
}

console.log(listFlatten([2, 1, [3, [4, 5], 6], 7, [8]]))
console.log('output should be [2, 1, 3, 4, 5, 6, 7, 8]')
