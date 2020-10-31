function get_factors(n)
  function factor(n, i, combi, res)
    while i * i <= n
      if n % i == 0
        push!(res, [combi ; [i, n ÷ i]])
        factor(n ÷ i, i, [combi ; [i]], res)
      end
      i += 1
    end
    return res
  end

  return factor(n, 2, [], [])
end


println(get_factors(32))