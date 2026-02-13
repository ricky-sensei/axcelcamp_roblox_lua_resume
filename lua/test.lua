function giveDamage(hp, damage)
    hp = hp - damage

    if hp < 0 then
        hp = 0
    end
    return hp
end

print(giveDamage(100, 20))
