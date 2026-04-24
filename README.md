# AI Problem Solving Assignment

This repository contains the implementation of two Artificial Intelligence problem-solving systems developed as part of the academic assignment. The goal of this project is to understand and apply core AI search techniques through practical, interactive applications.

---

## 📌 Problems Implemented

### 1. Tic-Tac-Toe AI (Game Playing System)

This module implements an intelligent Tic-Tac-Toe opponent that always makes the optimal move.

#### Key Features:
- Interactive web-based game interface
- AI plays optimally against the user
- Two algorithms implemented:
  - Minimax Algorithm
  - Alpha-Beta Pruning
- Performance comparison based on:
  - Number of nodes explored
  - Decision efficiency

---

### 2. Smart Navigation System (Graph Traversal)

This module simulates a navigation system that finds a path between two locations in a graph.

#### Key Features:
- Dynamic graph input through UI
- Pathfinding using:
  - Breadth-First Search (BFS) – guarantees shortest path
  - Depth-First Search (DFS) – explores deeply
- Comparison of:
  - Path found
  - Nodes explored
  - Efficiency of traversal

---

## 🛠 Technologies Used

- Python 3
- Flask (for web interface)
- HTML, CSS, JavaScript (frontend)

---

## 📂 Project Structure

AI_ProblemSolving_<RegisterNumber>/
│
├── problem1_tictactoe/
│   ├── app.py
│   └── templates/
│
├── problem2_navigation/
│   ├── app.py
│   └── templates/
│
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies
pip install -r requirements.txt

---

### Step 2: Run Tic-Tac-Toe AI
cd problem1_tictactoe
python app.py

Then open your browser and go to:
http://127.0.0.1:5000

---

### Step 3: Run Navigation System
cd problem2_navigation
python app.py

Open the same URL in browser.

---

## 📊 Sample Outputs

### Tic-Tac-Toe
- User plays as X
- AI responds as O
- Displays:
  - Nodes explored by Minimax
  - Nodes explored by Alpha-Beta

---

### Navigation System

Input Graph Example:
{"A":["B","C"],"B":["D"],"C":["E"],"D":[],"E":[]}

Output:
BFS Path: ['A', 'C', 'E']
DFS Path: ['A', 'B', 'D']

---

## 🧠 Key Learnings

- Understanding how decision trees work in games
- Importance of pruning in reducing computation
- Difference between uninformed search strategies
- Trade-offs between optimality and speed

---

## 🚀 Future Enhancements

- Add graphical visualization of search trees
- Improve UI with better styling and animations
- Deploy project online for public access
- Extend navigation system with weighted graphs (A* algorithm)

---

## 👨‍💻 Author

A. Jagan Karthick

---

## 📅 Submission

- Course: Artificial Intelligence
- Assignment: Problem Solving using AI Techniques
- Deadline: April 25, 2026
