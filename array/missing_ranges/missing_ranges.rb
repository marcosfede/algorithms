require 'set'

def missing_ranges(arr, low, hi)
    hashed = Set.new arr
    (low...hi).each do |n|
        puts n if !hashed.include?(n)
    end
end

inpt = [10, 12, 11, 15]
low, hi = 10, 15
p("input: ", inpt)
p("result: ")
missing_ranges(inpt, low, hi)