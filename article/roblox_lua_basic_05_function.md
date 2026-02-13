# Roblox Lua 基礎⑤  
# 関数（function）

------------------------------------------------------------------------

## 🎯 今日の目標

- 関数とは何かを理解する  
- 同じ処理をまとめて書けるようになる  
- Robloxでよく使う「処理の部品化」を体験する  

------------------------------------------------------------------------

# 1. 関数ってなに？

**関数（function）** とは、  
「よく使う処理を、ひとまとめにしたもの」。

たとえばゲームでは、こんな処理が何度も出てくる。

- ダメージを与える  
- HPを回復する  
- メッセージを表示する  

これらを毎回同じように書くのは大変。  
そこで **関数** を使う。

------------------------------------------------------------------------

# 2. 関数の基本の形

```lua
function 関数名()
    -- ここに処理を書く
end
```

例：

```lua
function sayHello()
    print("こんにちは！")
end
```

この時点では、まだ何も起きない。

------------------------------------------------------------------------

# 3. 関数を呼び出す

関数は **呼び出して** はじめて動く。

```lua
sayHello()
sayHello()
```

出力結果：

```
こんにちは！
こんにちは！
```

👉 同じ処理を何回でも使い回せる。

------------------------------------------------------------------------

# 4. 引数（ひきすう）

関数に **データを渡す** ことができる。  
このとき使うのが **引数**。

```lua
function sayHello(name)
    print("こんにちは、" .. name)
end

sayHello("たろう")
sayHello("はなこ")
```

------------------------------------------------------------------------

# 5. 複数の引数

```lua
function add(a, b)
    print(a + b)
end

add(3, 5)
add(10, 20)
```

------------------------------------------------------------------------

# 6. 戻り値（return）

関数は **結果を返す** こともできる。

```lua
function add(a, b)
    return a + b
end

local result = add(3, 5)
print(result)
```

👉 `return` は「この値を結果として返す」という意味。

------------------------------------------------------------------------

# 7. if文・演算子と組み合わせる

```lua
function calcDamage(hp, damage)
    local after = hp - damage

    if after < 0 then
        after = 0
    end

    return after
end

local hp = 100
hp = calcDamage(hp, 40)

print("残りHP: " .. hp)
```

------------------------------------------------------------------------

# 8. Robloxでよくある関数例

### ダメージを与える関数

```lua
function giveDamage(humanoid, damage)
    local hp = humanoid.Health
    hp = hp - damage

    if hp < 0 then
        hp = 0
    end

    humanoid.Health = hp
end
```

------------------------------------------------------------------------

# 9. Roblox Studioでやってみよう

触れたら関数を使ってダメージを与えるブロックを作ってみよう。

```lua
local part = script.Parent

function giveDamage(humanoid, damage)
    local hp = humanoid.Health
    hp = hp - damage

    if hp < 0 then
        hp = 0
    end

    humanoid.Health = hp
end

local function onTouched(hit)
    local character = hit.Parent
    if not character then return end

    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if not humanoid then return end

    giveDamage(humanoid, 40)
    print("残りHP: " .. humanoid.Health)
end

part.Touched:Connect(onTouched)
```

------------------------------------------------------------------------

# 10. まとめ

- 関数は処理をまとめるためのもの  
- 引数でデータを受け取れる  
- return で結果を返せる  
- Robloxでは関数を使うとコードがすっきりする  

------------------------------------------------------------------------

# 🎮 ミニチャレンジ

1. 回復する関数 `heal(humanoid, amount)` を作ってみよう  
2. ダメージ量を変えられるようにしてみよう  
3. HPが0のときはダメージを与えないようにしてみよう  

