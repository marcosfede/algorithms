type FastList
  arr::Vector{Int}
  indexof::Dict{Int, Int}
  swaps::Int
  FastList(beg) = new(beg, Dict(v => i for (i, v) in enumerate(beg)), 0)
end
function get_index(fl::FastList, e::Int)
  return fl.indexof[e]
end
function swap(fl::FastList, e1::Int, e2::Int)
  i1 = fl.indexof[e1]
  i2 = fl.indexof[e2]
  # set element where 0 is to final element
  fl.arr[i1] = e2
  # update dict
  fl.indexof[e2] = i1
  # set 0 where the previous number was
  fl.arr[i2] = e1
  # update dict
  fl.indexof[e1] = i2
  fl.swaps += 1
  println(fl.arr)
end


function calc_moves(fl::FastList, en::Vector{Int})::Int
  while fl.arr != en
    i0 = get_index(fl, 0)
    if en[i0] != 0
      swap(fl, 0, en[i0])
      continue
    end
    for (ind, el) in enumerate(fl.arr)
      if el != en[ind]
        swap(fl, 0, el)
        break
      end
    end
  end
  return fl.swaps
end

function garage(beg::Vector{Int}, en::Vector{Int})
  fl = FastList(beg)
  return calc_moves(fl, en)
end

initial = [1, 2, 3, 0, 4]
final = [0, 3, 2, 1, 4]
println("initial:", initial)
println(garage(initial, final))
println("final should be:", final)
