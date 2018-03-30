class FastList
  def initialize(arr)
    @arr = arr
    @indexof = Hash[arr.map.with_index { |e, i| [e, i] }]
  end

  def swap(el1, el2)
    i1 = @indexof[el1]
    i2 = @indexof[el2]
    # set element where 0 is to final element
    @arr[i1] = el2
    # update dict
    @indexof[el2] = i1
    # set 0 where the previous number was
    @arr[i2] = el1
    # update dict
    @indexof[el1] = i2
    @moves += 1
  end

  def calc_moves(final)
    @moves = 0
    until @arr == final
      i0 = @indexof[0]

      if final[i0] != 0 # if element can be moved to its final position
        swap(0, final[i0])
        p @arr
        next
      end

      @arr.each.with_index do |el, ind|
        if el != final[ind]
          swap(0, el)
          p @arr
          break
        end
      end
    end
    @moves
  end
end

def garage(beg, final)
  fl = FastList.new beg
  fl.calc_moves(final)
end

initial = [1, 2, 3, 0, 4]
final = [0, 3, 2, 1, 4]
print 'initial:'
p initial
p(garage(initial, final))
print 'final should be:'
p final
