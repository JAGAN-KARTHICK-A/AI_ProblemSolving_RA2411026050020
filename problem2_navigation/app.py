
from flask import Flask,render_template,request,jsonify
from collections import deque
app=Flask(__name__)

def bfs(g,s,e):
 q=deque([[s]]);v=set();n=0
 while q:
  p=q.popleft();x=p[-1];n+=1
  if x==e:return p,n
  if x not in v:
   v.add(x)
   for i in g[x]:q.append(p+[i])
 return None,n

def dfs(g,s,e,p=[],n=0):
 p=p+[s];n+=1
 if s==e:return p,n
 for i in g[s]:
  if i not in p:
   r=dfs(g,i,e,p,n)
   if r[0]:return r
 return None,n

@app.route("/")
def h():return render_template("index.html")

@app.route("/solve",methods=["POST"])
def s():
 d=request.json
 g=d["graph"];s=d["start"];e=d["goal"]
 b=bfs(g,s,e);d2=dfs(g,s,e)
 return jsonify({"bfs":b,"dfs":d2})

if __name__=="__main__":
 app.run()
