defmodule Solution do
  def dfs(_, target, _, _) when target < 0 do
    [[]]
  end
  def dfs(_, target, _, path) when target == 0 do
    [path]
  end
  def dfs(nums, target, index, path) do
    Enum.slice(nums, index..-1)
    |> Enum.with_index
    |> Enum.flat_map(fn {num, idx} -> dfs(nums, target - num, idx, path ++ [num]) end)
    |> Enum.filter(fn x -> length(x) != 0 end)
  end

  def solve(candidates, target) do
    candidates = Enum.sort(candidates)
    dfs(candidates, target, 0, [])
  end
end


a = [2, 3, 6, 7]
IO.inspect Solution.solve(a, 7), charlists: :as_lists  # should be [[2, 2, 3], [7]]
