program = [parse(Int64, x) for x  in split(readline("input.txt"), ',')]

function run(program::Vector{Int64})::Int64
  program = program[:]
  i = 1
  while true
      operation = program[i:i+4]
      op = operation[1]
      if op == 99
          return program[1]
      end
      _ , a, b, to = operation
      if op == 1
          program[to+1] = program[a+1] + program[b+1]
      elseif op == 2
          program[to+1] = program[a+1] * program[b+1]
      end
      i += 4
    end
end

# p1
p1 = program[:]
p1[2] = 12
p1[3] = 2
println(run(p1))

# p2
for x in 1:100
  for y in 1:100
      p2 = program[:]
      p2[2] = x
      p2[3] = y
      if run(p2) == 19690720 # replace this with the number you're given
          println(100*x + y)
      end
  end
end
