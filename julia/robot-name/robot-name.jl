letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
history = String[]
mutable struct Robot
    name::String
end

function Robot()
    name = join(rand(letters, 2)) * string(join(rand(0:9,3)))
    println(history)
    println(name)
    while in(name, history)
        name = join(rand(letters, 2)) * string(join(rand(0:9,3)))
    end
    push!(history, name)
    return Robot(name)
end

function reset!(instance::Robot)
    instance = Robot()
end

for x = 0:99
    r1 = Robot()
end
