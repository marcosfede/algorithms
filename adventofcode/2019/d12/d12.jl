import Base: ==, hash

mutable struct Body
  pos::Vector{Int}
  vel::Vector{Int}
end
==(a::Body, b::Body) = a.pos == b.pos && a.vel == b.vel
hash(a::Body, h) = hash(vcat(a.pos, a.vel), h)

function energy(b::Body)::Int
    sum(abs.(b.pos)) * sum(abs.(b.vel))
end

function calc_force(pos1::Vector{Int}, pos2::Vector{Int})::Vector{Int}
  collect((x < y ? 1 : x > y ? -1 : 0) for (x, y) in zip(pos1, pos2))
end

function step!(objects::Vector{Body})::Vector{Body}
  for (i1, m1) in enumerate(objects)
    for m2 in objects[i1+1:end]
      force = calc_force(m1.pos,m2.pos)
      m1.vel += force
      m2.vel -= force
    end
  end

  for m in objects
    m.pos += m.vel
  end
  return objects
end


initial = [
  Body([-14,-4,-11],[0,0,0]),
  Body([-9,6,-7],[0,0,0]),
  Body([4,1,4],[0,0,0]),
  Body([2,-14,-9],[0,0,0])
]
# p1
objects = deepcopy(initial)
for t in 1:1000
  step!(objects)
end
println(sum(energy.(objects)))

# p2
function find_loop_in_coord(objects::Vector{Body}, idx::Int)::Int
    initial_pos_for_coord = [obj.pos[idx] for obj in objects]
    initial_vel_for_coord = [obj.vel[idx] for obj in objects]

    t = 0
    while true
      t += 1
      step!(objects)

      pos_x = [obj.pos[idx] for obj in objects]
      vel_x = [obj.vel[idx] for obj in objects]

      if pos_x == initial_pos_for_coord && vel_x == initial_vel_for_coord
          return t
      end
    end
end


loops = [find_loop_in_coord(deepcopy(initial), coord) for coord in 1:3]
println(lcm(loops))
