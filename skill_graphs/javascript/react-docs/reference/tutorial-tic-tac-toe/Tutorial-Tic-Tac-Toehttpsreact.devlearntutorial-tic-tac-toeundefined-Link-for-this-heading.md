# Tutorial: Tic-Tac-Toe[](https://react.dev/learn/tutorial-tic-tac-toe#undefined "Link for this heading")
You will build a small tic-tac-toe game during this tutorial. This tutorial does not assume any existing React knowledge. The techniques you’ll learn in the tutorial are fundamental to building any React app, and fully understanding it will give you a deep understanding of React.
This tutorial is designed for people who prefer to **learn by doing** and want to quickly try making something tangible. If you prefer learning each concept step by step, start with [Describing the UI.](https://react.dev/learn/describing-the-ui)
The tutorial is divided into several sections:
  * [Setup for the tutorial](https://react.dev/learn/tutorial-tic-tac-toe#setup-for-the-tutorial) will give you **a starting point** to follow the tutorial.
  * [Overview](https://react.dev/learn/tutorial-tic-tac-toe#overview) will teach you **the fundamentals** of React: components, props, and state.
  * [Completing the game](https://react.dev/learn/tutorial-tic-tac-toe#completing-the-game) will teach you **the most common techniques** in React development.
  * [Adding time travel](https://react.dev/learn/tutorial-tic-tac-toe#adding-time-travel) will give you **a deeper insight** into the unique strengths of React.


### What are you building? [](https://react.dev/learn/tutorial-tic-tac-toe#what-are-you-building "Link for What are you building? ")
In this tutorial, you’ll build an interactive tic-tac-toe game with React.
You can see what it will look like when you’re finished here:
App.js
App.js
ReloadClear Fork
999
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
import { useState } from 'react';


function Square({ value, onSquareClick }) {
return (
<button className="square" onClick={onSquareClick}>
{value}
</button>
);
}


function Board({ xIsNext, squares, onPlay }) {
function handleClick(i) {
if (calculateWinner(squares) || squares[i]) {
return;
}
const nextSquares = squares.slice();
if (xIsNext) {
nextSquares[i] = 'X';
} else {
nextSquares[i] = 'O';
}
onPlay(nextSquares);
}


const winner = calculateWinner(squares);
let status;
if (winner) {
status = 'Winner: ' + winner;
} else {
status = 'Next player: ' + (xIsNext ? 'X' : 'O');
}


return (
<>
<div className="status">{status}</div>
<div className="board-row">
If the code doesn’t make sense to you yet, or if you are unfamiliar with the code’s syntax, don’t worry! The goal of this tutorial is to help you understand React and its syntax.
We recommend that you check out the tic-tac-toe game above before continuing with the tutorial. One of the features that you’ll notice is that there is a numbered list to the right of the game’s board. This list gives you a history of all of the moves that have occurred in the game, and it is updated as the game progresses.
Once you’ve played around with the finished tic-tac-toe game, keep scrolling. You’ll start with a simpler template in this tutorial. Our next step is to set you up so that you can start building the game.
