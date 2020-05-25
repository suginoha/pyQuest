#構想　無体な100問を越えて勇者になるとpythonも理解できている
#2h.pyから自動的に問題を作る
import random
import unicodedata


def title():
    print("神殿の壁にポスターが貼ってある")
    print()
    print("勇者募集中")
    n = input("ちょっと稼いでみない？(y Enter)")
    if n == "y":return
    title()


def stage(n, e, miss):
    place, qn, q = e
    print("**************")
    print("stage", n + 1)
    print()
    print(place, qn, "問")
    print("**************")
    for i in range(qn):
        random.shuffle(q)
        if question(q[0]) == False:
            miss += 1
            if miss > 2:return miss
    return miss


def ending(e):
    global m, miss
    place, _, _ = e
    print()
    print("*" * 60)
    if miss > 2:
        print("勇者は" + place + " にて息絶え　謎の僧侶の決死の逃避行をする")
        if random.randint(1,10) < 4:
            print("残念ながら僧侶も息絶えたようだ")
            a = 0
            for i in range(10 ** 8):
                a += 1
            print()
            print("そして時が流れる")
        else:
            print("勇者は神殿にて復活した")
    if miss == 2:
        print("勇者はラスボスをついに倒し Pythonの銅のメダルをゲットした")
        m[2] += 1
    if miss == 1:
        print("勇者はラスボスを倒し Pythonの銀のメダルをゲットした")
        m[1] += 1
    if miss == 0:
        print("勇者はラスボスを軽々と倒し Pythonの金のメダルをゲットした")
        m[0] += 1
    print("*" * 60)
    miss = 0
    print()


def loadData():
    line = []
    with open("./2h.py") as f:#データ読み込み
        for l in f:
            if len(l) > 0 and l[0] != "#":line += [l[:-1]]
    return line


def lineWord(line):
    r = []
    for l in line:
        o = ""
        for i in l:
            if unicodedata.east_asian_width(i) == "W":continue
            if i.isalpha():o += i
            else: o += " "
        while o.count("  ") > 0:
            o = o.replace("  ", " ")
        r += [o.split()]
    return r


def setLvLine():
    global lineW, lv
    r = []
    for i, w in enumerate(lv):
        l = []
        for ii, h in enumerate(lineW):
            if w in h:l += [ii]
        r += [l]
    return r


def question(qn):
    global lvLine, line, lv
    random.shuffle(lvLine[qn])
    qLine = lvLine[qn][0]
    q = line[qLine]
    q = q.replace(lv[qn], "x" * len(lv[qn]))
    print(line[qLine - 2])
    print(line[qLine - 1])
    print(q)
    a = input("?")
    if a == lv[qn]:
        print("正解")
        print()
        return True
    else:
        print()
        print(lv[qn] + "にダメージをくらった")
        print()
        return False


m=[0, 0, 0]
lv="print for range int str ord chr len sum max replace if else import random randint sort enumerate join".split()
ev=[("世界挨拶", 2, [0]), ("輪廻転生", 5, [0, 1, 2]), ("交換の街角", 6, [3, 4, 5, 6]), ("賢者の塔", 8, [7, 8, 9, 10, 11, 12]), ("荒ぶる神々", 5, [13, 14, 15])]
ev+=[("三堕天使の教え", 5, [16, 17, 18]), ("四天王との戦い", 7, [2, 10, 15, 17]), ("ラスボス", 14, [2, 10, 11, 12, 13, 14, 15, 16, 17, 18])]
#テスト
#ev=[("天と地", 3, [0, 18] )]

miss = 0
line = loadData()
lineW = lineWord(line)
lvLine = setLvLine()
while True:
    title()
    for n, e in enumerate(ev):
        miss = stage(n, e, miss)
        if miss > 2:break
    ending(e)
