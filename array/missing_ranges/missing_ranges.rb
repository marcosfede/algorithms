require 'set'

def missing_ranges(arr, low, high)
  hashed = Set.new arr
  (low...high).each do |n|
    puts n unless hashed.include?(n)
  end
end

inpt = [10, 12, 11, 15]
low = 10
hi = 15
p('input: ', inpt)
p('result: ')
missing_ranges(inpt, low, hi)
