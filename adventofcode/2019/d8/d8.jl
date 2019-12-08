digits = [parse(Int64, x) for x  in readline("input.txt")]
width = 25
height = 6
size = width * height

layers = [digits[start:start + size - 1] for start in 1:size:length(digits)]

# p1
number_of_digits(digit::Int, arr::Vector{Int}) = sum([x == digit for x in arr])

layer = layers[argmin([number_of_digits(0, layer) for layer in layers])]
println(number_of_digits(1, layer) * number_of_digits(2, layer))

# p2
function print_image(image::Array{Int,2})
    for row in eachrow(image)
        for pixel in row
            if pixel == 0
                print("■")
            elseif pixel == 1
                print("□")
            end
        end
        print("\n")
    end
end

image = fill(2, height, width)
for layer in reverse(layers)
    layer2d = reshape(layer, width, height)' # row-major reshaping trick
    for coord in CartesianIndices(layer2d)
        if layer2d[coord] != 2
            image[coord] = layer2d[coord]
        end
    end
end
print_image(image)
