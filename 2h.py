#こんな夢をみた
#オフィスで新人女性社員にPythonの何かしらの研修を受けさせようという話が決まる
#私は少しサポートすればなんとかなるだろうという認識
#彼女が出社してくる
#別の社員が説明のあと彼女に質問する「Pythonの経験は？」
#返ってきた答えは「ないです」
#研修は午後1時半から現在時刻は10時
#今の所なんのアイデアもないけど2時間でなんとかなるだろうと基礎を教えることにした

#夢から目が覚めた　時間は8時 ...　10時までに簡単な教材を作っておこう
# 8時半開始　9:56 終了
# 勢いあまって午後の研修まで作ってしまった
# あとは夢の中の私にこの資料を届けるだけだ


#Pythonの特徴
#プログラムの開始位置を揃える　プログラムのひとまとまりは開始位置をまとめて下げる

#0 お約束
print("good morning")

#1 ループ
for time in range(8, 13):
    print(time)

#2 四則演算
print(99 + 1, 100 * 10, 8 - 5, 81 / 9)

#2' 割ると割り切れても小数点がつく小数点以下をカットするなら //
print(99 + 1, 100 * 10, 8 - 5, 81 // 9)

#3 文字列と数値
a = "123456"
print(a + a)
a = int(a)
print(a + a)

#4 訂正
a = "こんにちは"
a = a.replace("は", "わ")
print(a)

#5 配列の連結
h = ["朝飯"]
h += ["まだだ"]
print(h[0] + "が" + h[1])
print("が".join(h))

#6 いくつ　ごうけい　さいだい
h1 = [1, 2, 3, 4, 8, 5, 6]
print(len(h1)) #数
print(sum(h1)) #合計
print(max(h1)) #最大

#7 操作王スライス
#  012345678
m = "slice use"
print("はじめは0", m[0])
print("はじめから5つ", m[0:5])
print("2から4", m[2:5])
print("おしまい", m[-1])
print("逆転", m[::-1])

#8 X次元の配列
data = [[1, 2, 3, 4], [5, 6, 7, 8]]
data += [[9, "a", "b", "c"]]
for d in data:
    print(d)

#9 くっつけ星人タプル
x = 10
y = 20
z = -10
a = (x, y, z)
print(a)
print(sum(a)) #合計
c, d, e = a
print(c, d, e)

#10 3の倍数だとnyao
for i in range(10):
    if i % 3 == 0:
        print("nyao")
    else:
        print(i)

#11　午後の研修課題　次のデータから取引の多い順にならべよ
import random #乱数用
h = []
for i in range(100):
    h += [(random.randint(1, 100), chr(ord("a") + random.randint(0, 25)))]
print(h)

#answer
h.sort() #並び替え
print(h[::-1])

#12　次に同じアルファベットはまとめよ
#answer
o = []
for j in "abcdefghijklmnopqrstuvwxyz":
    total = 0
    for k in h:
        num, name = k
        if name == j:total += num
    if total > 0:o += [(total, j)]
print(o)

#13 取引の多い8つのアルファベットを多い順にならべよ
#answer
o.sort()
o = o[::-1]
for n, i in enumerate(o[:8]):
    money, name = i
    print(n + 1, name, money)

#14 表っぽくかこっておしまい
mp = ["o" + "-" * 10 + "o"]
for n, i in enumerate(o):
    money, name = i
    mp += ["| " + (str(n + 1) + " " + name + " " + str(money) + "   ")[:9] + "|"]
mp += ["o" + "-" * 10 + "o"]
for s in mp:
    print(s)
print("(億ドル)")

