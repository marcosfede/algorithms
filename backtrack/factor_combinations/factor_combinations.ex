defmodule Solution do
  def divisors(n, i, up_to) do
    if up_to < i do
      []
    else
      i..up_to |> Enum.filter(fn k -> rem(n, k) === 0 end)
    end
  end

  def getFactors(n, i \\ 2) do
    up_to = Kernel.trunc(:math.floor(:math.sqrt(n)))
    divisors(n, i, up_to)
    |> Enum.flat_map(
        fn d ->
          [[div(n, d)] | getFactors(div(n,d), d)]
            |> Enum.map(fn s -> [d] ++ s  end)
        end
      )
  end
end


IO.inspect Solution.getFactors(16)
