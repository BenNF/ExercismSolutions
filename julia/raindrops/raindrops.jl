function raindrops(number::Int)
    val = ""
    if number % 3 == 0
        val *= "Pling"
    end
    if number % 5 == 0
        val *= "Plang"
    end
    if number % 7 == 0
        val *= "Plong"
    end
    if val == ""
        val *= string(number)
    end
    return val
end

println(raindrops(28))
