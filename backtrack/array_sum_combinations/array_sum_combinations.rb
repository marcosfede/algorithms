def Counter(iterable)
  hmap = Hash.new(0)
  iterable.each do |el|
    hmap[el] = hmap[el] + 1
  end
  hmap
end

def product(head, *tail)
  return head unless tail
  head.product(*tail)
end

def sum_combinations(target, *arrs)
  counter_last = Counter(arrs[-1])
  Enumerator.new do |enum|
    product(*arrs.slice(0, arrs.length - 1)).each do |combination|
      difference = target - combination.reduce(:+)
      next unless counter_last.key?(difference)
      (0...counter_last[difference]).each do |_repeated|
        enum.yield combination + [difference]
      end
    end
  end
end

A = [1, 2, 3, 3]
B = [2, 3, 3, 4]
C = [1, 2, 2, 2]
target = 7

solution = sum_combinations(target, A, B, C).to_a
p solution.length
solution.each do |sol|
  p sol
end
