file = open("input")
lines = readlines(file)

function solve()
  twos = 0
  threes = 0
  for line in lines
    d = Dict{Char,Int64}()
    for char in line
      d[char] = get(d, char, 0) + 1
    end
    v = values(d)
    if 2 in v
      twos +=1
    end
    if 3 in v
      threes +=1
    end
  end
  println(twos)
  println(threes)
  twos*threes
end
print(solve())
