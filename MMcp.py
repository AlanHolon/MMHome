import os

tw,th = os.get_terminal_size()
ro = th - 6
co = int(tw/25)

def resizeprint():
    global ro,co,tw,th
    tw,th = os.get_terminal_size()
    ro = th - 6
    co = int(tw/20)

def clscreen():
    print('\033c')

def gotoxy(x,y,s):
    print('\033['+str(x)+';'+str(y)+'H'+s)

def xy(x,y):
    return '\033['+str(x)+';'+str(y)+'H' 

def mess(x):
    if messtf: input("\033[2;4HMessaggio:> "+x)

def color(x):
    if x in corvet:
        return '\033[1;31m'
    elif x > nf:
        return '\033[1;33m'
    else:
        return '\033[1;32m'

def status(x,y):
    if x == -1:
        if y < 4: return "&#10068"
        elif y == 4: return "&#9888"
        elif y == 5: return "&#9940"
    elif x == 0:
        return "&#11088"
    elif x == 3:
        return "&#129351"
    elif x == 2:
        return "&#129352"
    elif x == 1:
        return "&#129353"

def errcont(x):
    if x < 5: 
        return "&#10060"*x
    else:
        return ""

def prlifes(x):
    return sqemo[x]*lif[x]

def prmat(x,y):
    if mat[x][y] != 0: return '\033[1;32m '+str(mat[x][y])
    elif erm[x][y] < 5: return '\033[1;33m --'
    else: return '\033[1;31m XX'

def prsta(x,y):
    if erm[x][y] != 0: return '\033[1;31m('+str(erm[x][y])+')'
    elif sta[x][y] != 0 and sta[x][y] != -1: return '\033[1;32m('+str(4-sta[x][y])+')'
    else: return ''

def prpt(x):
    return '\033[1;32m'+' '*(4-len(str(pt[x])))+str(pt[x])

def twochars(x):
    return ' '*(2-len(str(x)))+str(x)

def repod(x):
    pod.remove(x)
    if pt[x] <= pt[pod[len(pod)-1]]:
        pod.append(x)
    else:
        for i in range(0,len(pod)):
            if pt[x] > pt[pod[i]]:
                pod.insert(i,x)
                break

def printpod(x,f):
    if pt[pod[x]] != 0: return str(f[pod[x]])
    else: return ''

def printgrad():
    clscreen()
    for i in range(0, len(sq)):
        print(xy(i+3,3)+str(pod[i]+1)+": "+sqdim[pod[i]]+" "+printpod(i,pt))
    input(xy(len(sq)+4,3)+"Premi INVIO per continuare ...")

def printall():
    clscreen()
    for i in range(0, len(sq)):
        print(xy(3,9+11*i)+str(i+1)+" : "+sqdim[i])
    for i in range(0, len(an)):
        print(xy(5+i+int(i/4),3)+" "*(2-len(str(i+1)))+str(i+1)+".")
    print(xy(5+len(an)+4,3)+"TOT")
    for i in range(0, len(sq)):
        for j in range(0, len(an)):
            print(xy(5+j+int(j/4),9+11*i)+prmat(i,j)+" "+prsta(i,j))
    for i in range(0, len(sq)):
        print(xy(5+len(an)+4,8+11*i)+prpt(i))
    input(xy(7+len(an)+4,3)+"Premi INVIO per continuare ...")

def htmlize():
    global model
    t = ""
    u = ""
    rang = []
    for i in range(0,len(sq)):
        rang.append(i) 
    rang = rang + [0, 1, 2, 3]
    u = u + '<div class="main" id="cont"><div id="podio"></div>'
    for i in range(0,3):
        u = u + '<div id="p'+str(i+1)+'"></div><div id="pt'+str(i+1)+'">&#12935'+str(i+1)+'</div><div id="pe'+str(i+1)+'">'+printpod(i,sqemo)+'</div><div id="pn'+str(i+1)+'">'+printpod(i,sqdim)+'</div><div id="pp'+str(i+1)+'">'+printpod(i,pt)+'</div>'
    u = u + '</div>'
    for i in rang:
        t = t + '<div class="spa"><div class="circ" style="border-color:'+sqcol[i]+';"><span class="ico">'+sqemo[i]+'</span> '+sqdim[i]+'</div><div class="nam">'+sq[i]+'</div><div class="line" style="background-color:'+sqcol[i]+';">'
        for j in range(0,len(an)):
            t = t + '<div class="cel"><div class="m">' + status(sta[i][j],erm[i][j]) + '</div><div class="d">' + errcont(erm[i][j])  + '</div></div>'
        t = t + "</div></div>"
    if os.path.isdir("/run/user/1000/MateMajorana"): f_in = open("/run/user/1000/MateMajorana/index.html", "w+")
    else: f_in = open("index.html", "w+")
    f_in.write(model.replace("[#tab#]",t).replace("[#pod#]",u))
    f_in.close()

def htmlinizio():
    f_mo = open("modelinizio.html")
    if os.path.isdir("/run/user/1000/MateMajorana"): f_in = open("/run/user/1000/MateMajorana/index.html", "w+")
    else: f_in = open("index.html", "w+")
    f_in.write(f_mo.read())
    f_in.close()

def htmlfine():
    f_mo = open("modelfinal.html")
    if os.path.isdir("/run/user/1000/MateMajorana"): f_in = open("/run/user/1000/MateMajorana/index.html", "w+")
    else: f_in = open("index.html", "w+")
    f_in.write(f_mo.read())
    f_in.close()

def htmlpodio():
    f_mo = open("modelpodio.html")
    modelpodio = f_mo.read()
    f_mo.close()
    u = ""
    u = u + '<div class="main" id="cont"><div id="podio"></div>'
    for i in range(0,3):
        u = u + '<div id="p'+str(i+1)+'"></div><div id="pt'+str(i+1)+'">&#12935'+str(i+1)+'</div><div id="pe'+str(i+1)+'">'+printpod(i,sqemo)+'</div><div id="pn'+str(i+1)+'">'+printpod(i,sqdim)+'</div><div id="pp'+str(i+1)+'">'+printpod(i,pt)+'</div>'
    u = u + '</div>'
    if os.path.isdir("/run/user/1000/MateMajorana"): f_in = open("/run/user/1000/MateMajorana/index.html", "w+")
    else: f_in = open("index.html", "w+")
    f_in.write(modelpodio.replace("[#pod#]",u))
    f_in.close()

def prmoves():
    l = min(ro*co, len(mov))
    if cortf: print(xy(3,4)+'\033[1;31mPer ripristinare digita "reinit"')
    for t in range(0,l):
        u = len(mov)-1-t
        cif = 4-len(str(n-t))
        tint = int(t/ro)
        rind = t-tint*ro
        cind = 3+25*int(t/ro)+cif
        print(color(u+1)+xy(6+rind,cind)+str(n-t)+" : "+mov[u])

def udfile():
    global nf
    f_ga = open("gara.txt", "a")
    for t in range(nf,n):
        f_ga.write(mov[t]+"\n")
    f_ga.close()
    nf = n

def correct(x):
    global nf, cortf, corvet
    y, z = x.split(":")
    if int(y) <= n:
        mov[int(y)-1] = z.strip()
        corvet.append(int(y))
        cortf = True

def reinit():
    f_ga = open("gara.txt", "w")
    for t in range(0,n):
        f_ga.write(mov[t]+"\n")
    f_ga.close()
    init()    

def analize(x):
    global n
    s, q, a = x.split("-")
    s = s.strip()
    q = q.strip()
    a = a.strip()
    if s.isnumeric() and q.isnumeric() and int(s)<=len(sq) and int(q)<=len(an) and int(s)>0 and int(q)>0:
        if erm[int(s)-1][int(q)-1] < 5 and mat[int(s)-1][int(q)-1] == 0:
            if a == an[int(q)-1].strip():
                mat[int(s)-1][int(q)-1] = int(60/(erm[int(s)-1][int(q)-1]+1))
                pt[int(s)-1] = pt[int(s)-1] + mat[int(s)-1][int(q)-1]
                ach[int(s)-1][int((int(q)-1)/4)] = ach[int(s)-1][int((int(q)-1)/4)] + 1
                if ach[int(s)-1][int((int(q)-1)/4)] == 4: pt[int(s)-1] = pt[int(s)-1] + 30
                sta[int(s)-1][int(q)-1] = 0
                if erm[int(s)-1][int(q)-1] == 0 and pri[int(q)-1] > 0:
                   mat[int(s)-1][int(q)-1] = mat[int(s)-1][int(q)-1] + 5*pri[int(q)-1]
                   pt[int(s)-1] = pt[int(s)-1] + 5*pri[int(q)-1]
                   sta[int(s)-1][int(q)-1] = pri[int(q)-1]
                   pri[int(q)-1] = pri[int(q)-1] - 1
                repod(int(s)-1)
            else:
                erm[int(s)-1][int(q)-1] = erm[int(s)-1][int(q)-1] + 1
        else:
            mess("Risposta non accettabile")
        n = n + 1
        mov.append(twochars(s) + " - " + twochars(q) + " - " + a)
    else:
        mess("Errore di sintassi")

def inscom():
    global qu
    com = input(xy(2,4)+"\033[1;32mLinea di Comando:> ")
    if len(com.split(":")) == 2:
        correct(com)
    elif len(com.split("-")) == 3:
        analize(com)
    elif com == "":
        udfile()
        htmlize()
    elif com == "file" or com == "f":
        udfile()
    elif com == "html" or com == "h":
        htmlize()
    elif com == "quad" or com == "q":
        printall()
    elif com == "resize":
        resizeprint()
    elif com == "grad":
        printgrad()
    elif com == "reinit":
        reinit()
    elif com == "inizio":
        htmlinizio()
    elif com == "fine":
        htmlfine()
    elif com == "podio":
        htmlpodio()
    elif com == "exit":
        qu = True

def init():
    global sq, lensq, sqdim, sqcol, sqemo, pt, an, lenan, mat, erm, sta, pri, lif, ach, pod, n, nf, mov, qu, model, messtf, cortf, corvet
    n = 0
    mov = []
    qu = False
    messtf = False
    cortf = False
    corvet = []
    f_sq = open("squadre.txt")
    sq = []
    sqdim = []
    sqcol = []
    sqemo = []
    pt = []
    for t in f_sq.readlines():
        if t.strip() != "":
            sq.append(t.strip().split(";")[0])
            sqdim.append(t.strip().split(";")[1])
            sqcol.append(t.strip().split(";")[2])
            sqemo.append(t.strip().split(";")[3])
    f_sq.close()
    lensq = len(sq)
    f_an = open("risposte.txt")
    an = []
    for t in f_an.readlines():
        if t.strip() != "":
            an.append(t.strip())
    lenan = len(an)
    mat = [ [ 0 for j in range(len(an)) ] for x in range(len(sq)) ]
    erm = [ [ 0 for j in range(len(an)) ] for x in range(len(sq)) ]
    sta = [ [ -1 for j in range(len(an)) ] for x in range(len(sq)) ]
    ach = [ [ 0 for j in range(4) ] for x in range(len(sq)) ]
    pt = [ 0 for i in range(len(sq)) ]
    lif = [ 3 for i in range(len(sq)) ]
    pri = [ 3 for i in range(len(an)) ]
    pod = [ i for i in range(len(sq)) ]
    f_an.close()
    f_ga = open("gara.txt")
    for t in f_ga.readlines():
        analize(t.strip())
    nf = n
    f_ga.close()
    f_mo = open("model.html")
    model = f_mo.read()
    f_mo.close()
    messtf = True

clscreen()
init()
prmoves()
while qu == False:
   inscom()
   clscreen()
   prmoves()
clscreen()
