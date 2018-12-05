# https://adventofcode.com/2018/day/1
# docker run -it --rm -v "$PWD":/usr/myapp -w /usr/myapp julia julia script.jl

open(joinpath(@__DIR__,"input.txt")) do f
   global inputs = readlines(f)
end

output = nothing
sums = Set()
last_sum = 0
while output == nothing
    global sums
    global last_sum
    for n in inputs
        curr_sum = parse(Int, n) + last_sum
        if curr_sum in sums
            global output = curr_sum
            break
        end
        push!(sums, curr_sum)
        last_sum = curr_sum
    end
end

print(output, '\n')
