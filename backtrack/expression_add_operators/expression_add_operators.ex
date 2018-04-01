defmodule Solution do
  def product(arr, repeat) when repeat == 1 do
    for el <- arr, do: [el]
  end

  def product(arr, repeat) do
    for el <- arr, prod <- product(arr, repeat - 1), do: [el] ++ prod
  end

  def solve(num, target) do
    n = String.length(num)
    num_arr = String.split(num, "", trim: true)
    product(["", "+", "*", "-"], n - 1)
    |> Enum.map(fn comb ->
      interleaved = Enum.flat_map(Enum.zip(num_arr, comb), fn x -> Tuple.to_list(x) end)
      interleaved = interleaved ++ [List.last(num_arr)]
      interleaved
    end)
    |> Enum.map(fn x -> Enum.join(x, "") end)
    |> Enum.filter(fn solution ->
      {res, _} = Code.eval_string(solution)
      res == target
    end)
  end
end

# "123", 6 -> ["1+2+3", "1*2*3"]
IO.inspect Solution.solve("123", 6)

# "232", 8 -> ["2*3+2", "2+3*2"]
IO.inspect Solution.solve("232", 8)

# "123045", 3 ->
# ["1+2+3*0*4*5", "1+2-3*0*4*5", "1*2+3*0-4+5",
# "1*2-3*0-4+5", "1-2+3+0-4+5", "1-2+3-0-4+5"]
IO.inspect Solution.solve("123045", 3)

IO.inspect Solution.solve("105", 5)
