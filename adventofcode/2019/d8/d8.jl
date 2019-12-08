digits = [parse(Int64, x) for x  in readline("input.txt")]
width = 25
height = 6
size = width * height

layers = [digits[start:start + size - 1] for start in 1:size:length(digits)]

# p1
layer = layers[argmin([sum(layer .== 0) for layer in layers])]
println(sum(layer .== 1) * sum(layer .== 2))

# p2
function print_image(image::Array{Int,2})
    for row in eachrow(image)
        for pixel in row
            if pixel == 0
                print(" ")
            elseif pixel == 1
                print("#")
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
