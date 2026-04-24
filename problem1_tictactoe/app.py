
from flask import Flask, render_template, request, jsonify
import time, math

app = Flask(__name__)

def check(board, p):
    wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in wins)

def full(board): return " " not in board

nodes1=0
nodes2=0

def minimax(b, m):
    global nodes1
    nodes1+=1
    if check(b,"O"): return 1
    if check(b,"X"): return -1
    if full(b): return 0
    best=-999 if m else 999
    for i in range(9):
        if b[i]==" ":
            b[i]="O" if m else "X"
            val=minimax(b,not m)
            b[i]=" "
            best=max(best,val) if m else min(best,val)
    return best

def alphabeta(b,m,a,beta):
    global nodes2
    nodes2+=1
    if check(b,"O"): return 1
    if check(b,"X"): return -1
    if full(b): return 0
    best=-999 if m else 999
    for i in range(9):
        if b[i]==" ":
            b[i]="O" if m else "X"
            val=alphabeta(b,not m,a,beta)
            b[i]=" "
            if m:
                best=max(best,val); a=max(a,best)
            else:
                best=min(best,val); beta=min(beta,best)
            if beta<=a: break
    return best

def best(b):
    global nodes1,nodes2
    nodes1=nodes2=0
    bestv=-999; move=0
    for i in range(9):
        if b[i]==" ":
            b[i]="O"
            v=minimax(b,False)
            b[i]=" "
            if v>bestv: bestv=v; move=i
    t1=nodes1
    alphabeta(b,True,-999,999)
    return move, t1, nodes2

@app.route("/")
def home(): return render_template("index.html")

@app.route("/move",methods=["POST"])
def move():
    b=request.json["board"]
    m,n1,n2=best(b)
    b[m]="O"
    return jsonify({"board":b,"nodes_minimax":n1,"nodes_ab":n2})

if __name__=="__main__":
    app.run()
