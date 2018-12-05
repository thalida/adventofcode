# https://adventofcode.com/2018/day/1
# docker run -it --rm -v "$PWD":/usr/myapp -w /usr/myapp julia julia script.jl

open(joinpath(@__DIR__,"input.txt")) do f
   global inputs = readlines(f)
end

output = mapreduce(n->parse(Int, n), +, inputs)
print(output, '\n')
