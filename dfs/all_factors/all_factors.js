function get_factors(n) {
    function factor(n, i, combi, res){
        while (i * i <= n){
            if (n % i == 0){
                res.push(combi.concat(i, n / i))
                factor(n / i, i, combi.concat(i), res)
            }
            i += 1
        }
        return res
    }
    return factor(n, 2, [], [])
}

console.log(get_factors(32))