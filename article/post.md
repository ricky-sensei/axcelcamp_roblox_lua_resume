この記事は、岩手県八幡平市のプログラミング教室「アクセルキャンプ」の公開教材です。
[アクセルキャンプ(フリースペースプラウド)のリンク](https://freespaceproud.com)
教材の作成依頼等も承っております。ご意見等は、リンク先の問い合わせ欄からお願いします。
教材の転用・利用等は自由ですが、コメント等で一声いただけますと幸いです。  

------------------------------------------------------------------------
# Roblox Lua 基礎② 計算と演算子

# Lua( Luau ) について
**lua**はプログラミング言語で、ゲーム開発に限らず、世の中のいろんな便利なツールで使われているもの。 **luau** とは、それをrobloxでプログラミングするのに便利になるように改良したもの。
みんながこれから勉強していくものの一部は正確に言うとluauなんだけど、このシリーズの中ではluaとして統一するよ。

以下のリンクはluaの細かい仕様が書いてある。最初は意味不明な言葉の羅列に感じるかもだけど、なにかわからないときに見てみると解決するかも。
[lua公式ドキュメント(日本語)](https://inzkyk.xyz/lua_5_4/)
[roblox クリエイターハブ](https://create.roblox.com/landing)
[luau ドキュメント(roblox クリエイターハブ)](https://create.roblox.com/docs/ja-jp/luau)


# 大タイトル

------------------------------------------------------------------------

## 🎯 今日の目標

- 足し算・引き算などの計算ができるようになる
- データを「くらべる」ことができるようになる
- true / false を使った判断を理解する
------------------------------------------------------------------------

# 1. 計算してみよう
robloxの中では、めちゃくちゃたくさんの計算が行われている。たとえば
- ダメージを受けたらHPを減らす  
- コインを取ったらスコアを増やす  
- 時間を数える  

これらは足し算や引き算のたんじゅんな計算でなんとかなりそうだけど、例えばバトルロイヤルゲームの弾の弾道計算とかは、高校や大学の数学で習うような高度な計算もしなくちゃいけない。(だから、算数や数学の勉強って超大事!)

Robloxには、そんな計算を簡単にできるようにしたり、やりやすくしてくれる仕組みがたくさんあるから、安心してほしい。でもそれを使うために、簡単な計算のやり方を覚えとかなくちゃいけないから、この章で覚えちゃおう



------------------------------------------------------------------------

# 2. 算術演算子(計算の記号)
プログラミングの処理の中で使う記号のことを **演算子** といって、その中でも計算に使うやつのことを **算術演算子** という。算数や数学で使うものと同じのもあれば、違うのや、プログラミングでしか使わない記号もある。
## ① 四則演算
| 記号 | 意味   | 例     |
| ---- | ------ | ------ |
| +    | 足す   | 5 + 3  |
| -    | 引く   | 10 - 4 |
| *    | かける | 2 * 3  |
| /    | 割る   | 8 / 2  |

### 実際に計算してみよう
```lua
local a = 10
local b = 3

print(a + b)  -- 13
print(a - b)  -- 7
print(a * b)  -- 30
print(a / b)  -- 3.333...
```

### 変数の中身を増やしたり、減らしたり
例えば｢りんごが5つありましたが、そこから2つ取って食べちゃいました。残りはいくつでしょう｣みたいな問題があったとする。
こんな感じの計算をして答えを出すのも一応正解
```lua
local apple = 5
print(apple - 2)
```
でもちょっと考えてみよう。現在持っているりんごの数によってもらえるアイテムが変わってくるゲームを作ったとする。りんごを食べたりもらったりするたびに計算すればいいけど。それだと今何個りんごを持ってるかわからなくなってしまうし、式がどんどん長くなってしまう!
```lua
local apple = 5
-- 2個たべる
print(apple - 2)
-- 3個もらう
print(apple - 2 + 3)
-- 5個食べる
print(apple - 2 + 3 - 5)
-- 2個もらう
print(apple + 2 + 3 - 5 + 2)
-- 7こもらう
print(apple + 2 + 3 - 5 + 2 + 7)
```
そこで、計算した結果を変数にいれなおしてみよう。
```lua
local apple = 5
-- 2個たべる
apple = apple - 2
print(apple)
-- 3個もらう
apple = apple + 3
print(apple)
-- 5個食べる
apple = apple - 5
print(apple)
-- 2個もらう
apple = apple + 2
print(apple)
-- 7個もらう
apple = apple + 7
print(apple)
```
### 練習問題
上のりんごのプログラムをつかって
```
･りんごを食べたorもらったときに、その時持っているりんご x20 のポイントが貰える
```
というプログラムを実装してみよう。
<details><summary>例</summary>

```lua
local apple = 5
local point = 0

-- 2個たべる
apple = apple - 2
point = point + apple * 20
print(apple)
print(point)

-- 3個もらう
apple = apple + 3
point = point + apple * 20
print(apple)
print(point)

-- 5個食べる
apple = apple - 5
point = point + apple * 20
print(apple)
print(point)

-- 2個もらう
apple = apple + 2
point = point + apple * 20
print(apple)
print(point)

-- 7こもらう
apple = apple + 7
point = point + apple * 20
print(apple)
print(point)

```

</details>

------------------------------------------------------------------------

# 3. 比較演算子
2つの**データ**を比べる演算子
比較をした結果、式が正しい(**true**)か、間違っている(**false**)かが返ってくる

| 記号 | 意味   | 例       | 結果  |
| ---- | ------ | -------- | ----- |
| ==   | 同じ   | 10 == 12 | false |
| ~=   | ちがう | 10 ~= 12 | true  |
| >    | 大きい | 10 > 12  | false |
| <    | 小さい | 10 < 12  | true  |
| >=   | 以上   | 10 >= 12 | false |
| <=   | 以下   | 10 <=10  | true  |

## 比較してみよう

```lua
local score = 100

print(score == 100)   -- true
print(score ~= 50)    -- true
print(score > 80)     -- true
print(score < 80)     -- false
```

## ⚠ 超重要な注意

```lua
score = 100    -- 代入:右のデータを左に入れる
score == 100   -- 比較:右と左が同じかどうかチェック
```

`=` と `==` は **まったく別物**。

---

------------------------------------------------------------------------
# 5. 論理演算子
2つの論理式(trueかfalseか)を組み合わせて、複雑な処理を行うための演算子
次回以降の内容でじゅうようになってくる

| 書き方 | 意味       | 例                      | 結果                                                |
| ------ | ---------- | ----------------------- | --------------------------------------------------- |
| and    | どっちもOK | `10 < 20` and `20 < 30` | どちらもtrueなので <br> `true`                      |
| or     | どっちかOK | `10 > 20` or `20 < 30`  | 左側はfalseだけど <br> 右側はtrueなので <br> `true` |
| not    | 反対       | not 10 < 20             | 10 < 20はtrueなので、<br>その逆の`false`            |

## 条件を組み合わせる例

```lua

local hp = 50
local item = true

-- ｢hpが80以上で、**かつ(and)** アイテムを持ってる(true)のときだけ必殺技が打てる｣とする場合
print(hp >= 80 and item)   -- hpが足りないのでfalse: 必殺技がうてない

-- ｢hpが80以上、**または(or)** アイテムを持ってる(true)のときだけ必殺技が打てる｣とする場合
print(hp >= 80 or item)  -- hpは足りないけどアイテムを持ってるのでtrue: 必殺技がうてる
```
------------------------------------------------------------------------
# 6. コレを使って何ができるの?
来週の内容になるので説明はしないけど、試しにこのコードを動かして、アレンジしてみよう
```lua
local hp = 0

if hp <= 0 then
    print("ゲームオーバー")
end
```

------------------------------------------------------------------------

# 7. まとめ
- `+ - * /` で計算できる  
- `== ~= > <` でくらべられる  
- 結果は true / false  
- if文はこの上に成り立っている  


------------------------------------------------------------------------

# 8. Roblox Studioでやってみよう。

```lua
-- 触れたら40ダメージを受けるブロック
local part = script.Parent

local DAMAGE = 40
local COOLDOWN = 1.0  -- 1秒以内の連続ヒットを防ぐ

-- プレイヤーごとの「最後にダメージを受けた時刻」を保存
local lastHitTimeByPlayer = {}

local function onTouched(hit)
    -- 触れた相手（hit）から、プレイヤーのキャラかどうか判定する
    local character = hit.Parent
    if not character then return end

    local humanoid = character:FindFirstChildOfClass("Humanoid")
    if not humanoid then return end

    -- Character から Player を取得（NPCだと nil になることもある）
    local player = game.Players:GetPlayerFromCharacter(character)
    if not player then return end

    -- クールダウン判定
    local now = os.clock()
    local last = lastHitTimeByPlayer[player] or 0
    if (now - last) < COOLDOWN then
        return
    end
    lastHitTimeByPlayer[player] = now

    -- ここにコードを追加して、ダメージを受けたあとのHPをhpAfterにいれよう
    -- hpAfter は「ダメージを受けたあとのHP」
    local hpBefore = humanoid.Health
    local hpAfter = ???

    -- ここにコードを追加して、hpが0より小さくなったときは、hpが0になるようにしよう
    if ??? then
        hpAfter = 0
    end

    humanoid.Health = hpAfter

    print(player.Name .. " のHP: " .. hpBefore .. " → " .. hpAfter)
end

part.Touched:Connect(onTouched)
```

# 🎮 チャレンジ

1. HPを100にして、30ダメージを2回与えてみよう  
2. score が 50 以上かどうかを print してみよう  
3. 「HPが0以下 かつ ゲームオーバーでない」条件を考えてみよう  

