defmodule Solution do
  def getFactors(n, i = 2) do
    up_to = Kernel.trunc(:math.floor(:math.sqrt(n), 0))
    divisors = i..up_to |> Enum.filter(fn k -> rem(n, k) == 0 end)

  end
end


IO.inspect Solution.getFactors(16)
