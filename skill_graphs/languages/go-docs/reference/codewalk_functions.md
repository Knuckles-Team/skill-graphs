[ ![Go](https://go.dev/images/go-logo-white.svg) ](https://go.dev/)
[ Skip to Main Content ](https://go.dev/doc/codewalk/functions/#main-content)
  * [ Why Go _arrow_drop_down_ ](https://go.dev/doc/codewalk/functions/)
Press Enter to activate/deactivate dropdown
    * [ Case Studies ](https://go.dev/solutions/case-studies)
Common problems companies solve with Go
    * [ Use Cases ](https://go.dev/solutions/use-cases)
Stories about how and why companies use Go
    * [ Security ](https://go.dev/security/)
How Go can help keep you secure by default
  * [ Learn ](https://go.dev/learn/)
Press Enter to activate/deactivate dropdown
  * [ Docs _arrow_drop_down_ ](https://go.dev/doc/codewalk/functions/)
Press Enter to activate/deactivate dropdown
    * [ Go Spec ](https://go.dev/ref/spec)
The official Go language specification
    * [ Go User Manual ](https://go.dev/doc)
A complete introduction to building software with Go
    * [ Standard library ](https://pkg.go.dev/std)
Reference documentation for Go's standard library
    * [ Release Notes ](https://go.dev/doc/devel/release)
Learn what's new in each Go release
    * [ Effective Go ](https://go.dev/doc/effective_go)
Tips for writing clear, performant, and idiomatic Go code
  * [ Packages ](https://pkg.go.dev)
Press Enter to activate/deactivate dropdown
  * [ Community _arrow_drop_down_ ](https://go.dev/doc/codewalk/functions/)
Press Enter to activate/deactivate dropdown
    * [ Recorded Talks ](https://go.dev/talks/)
Videos from prior events
    * Meet other local Go developers
    * [ Conferences _open_in_new_ ](https://go.dev/wiki/Conferences)
Learn and network with Go developers from around the world
    * [ Go blog ](https://go.dev/blog)
The Go project's official blog.
    * [ Go project ](https://go.dev/help)
Get help and stay informed from Go
    * Get connected


[ ![Go.](https://go.dev/images/go-logo-blue.svg) ](https://go.dev/)
  * [Why Go _navigate_next_](https://go.dev/doc/codewalk/functions/)
[_navigate_before_ Why Go](https://go.dev/doc/codewalk/functions/)
    * [ Case Studies ](https://go.dev/solutions/case-studies)
    * [ Use Cases ](https://go.dev/solutions/use-cases)
    * [ Security ](https://go.dev/security/)
  * [Learn](https://go.dev/learn/)
  * [Docs _navigate_next_](https://go.dev/doc/codewalk/functions/)
[_navigate_before_ Docs](https://go.dev/doc/codewalk/functions/)
    * [ Go Spec ](https://go.dev/ref/spec)
    * [ Go User Manual ](https://go.dev/doc)
    * [ Standard library ](https://pkg.go.dev/std)
    * [ Release Notes ](https://go.dev/doc/devel/release)
    * [ Effective Go ](https://go.dev/doc/effective_go)
  * [Packages](https://pkg.go.dev)
  * [Community _navigate_next_](https://go.dev/doc/codewalk/functions/)
[_navigate_before_ Community](https://go.dev/doc/codewalk/functions/)
    * [ Recorded Talks ](https://go.dev/talks/)
    * [ Conferences _open_in_new_ ](https://go.dev/wiki/Conferences)
    * [ Go blog ](https://go.dev/blog)
    * [ Go project ](https://go.dev/help)
    * Get connected


# Codewalk: First-Class Functions in Go
[ ![Pop Out Code](https://go.dev/doc/codewalk/popout.png) ](https://go.dev/doc/codewalk/pig.go) doc/codewalk/pig.go
```
// Copyright 2011 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package main

import (
	"fmt"
	"math/rand"
)

const (
	win            = 100 // The winning score in a game of Pig
	gamesPerSeries = 10  // The number of games per series to simulate
)

// A score includes scores accumulated in previous turns for each player,
// as well as the points scored by the current player in this turn.
type score struct {
	player, opponent, thisTurn int
}

// An action transitions stochastically to a resulting score.
type action func(current score) (result score, turnIsOver bool)

// roll returns the (result, turnIsOver) outcome of simulating a die roll.
// If the roll value is 1, then thisTurn score is abandoned, and the players'
// roles swap.  Otherwise, the roll value is added to thisTurn.
func roll(s score) (score, bool) {
	outcome := rand.Intn(6) + 1 // A random int in [1, 6]
	if outcome == 1 {
		return score{s.opponent, s.player, 0}, true
	}
	return score{s.player, s.opponent, outcome + s.thisTurn}, false
}

// stay returns the (result, turnIsOver) outcome of staying.
// thisTurn score is added to the player's score, and the players' roles swap.
func stay(s score) (score, bool) {
	return score{s.opponent, s.player + s.thisTurn, 0}, true
}

// A strategy chooses an action for any given score.
type strategy func(score) action

// stayAtK returns a strategy that rolls until thisTurn is at least k, then stays.
func stayAtK(k int) strategy {
	return func(s score) action {
		if s.thisTurn >= k {
			return stay
		}
		return roll
	}
}

// play simulates a Pig game and returns the winner (0 or 1).
func play(strategy0, strategy1 strategy) int {
	strategies := []strategy{strategy0, strategy1}
	var s score
	var turnIsOver bool
	currentPlayer := rand.Intn(2) // Randomly decide who plays first
	for s.player+s.thisTurn < win {
		action := strategies[currentPlayer](s)
		s, turnIsOver = action(s)
		if turnIsOver {
			currentPlayer = (currentPlayer + 1) % 2
		}
	}
	return currentPlayer
}

// roundRobin simulates a series of games between every pair of strategies.
func roundRobin(strategies []strategy) ([]int, int) {
	wins := make([]int, len(strategies))
	for i := 0; i < len(strategies); i++ {
		for j := i + 1; j < len(strategies); j++ {
			for k := 0; k < gamesPerSeries; k++ {
				winner := play(strategies[i], strategies[j])
				if winner == 0 {
					wins[i]++
				} else {
					wins[j]++
				}
			}
		}
	}
	gamesPerStrategy := gamesPerSeries * (len(strategies) - 1) // no self play
	return wins, gamesPerStrategy
}

// ratioString takes a list of integer values and returns a string that lists
// each value and its percentage of the sum of all values.
// e.g., ratios(1, 2, 3) = "1/6 (16.7%), 2/6 (33.3%), 3/6 (50.0%)"
func ratioString(vals ...int) string {
	total := 0
	for _, val := range vals {
		total += val
	}
	s := ""
	for _, val := range vals {
		if s != "" {
			s += ", "
		}
		pct := 100 * float64(val) / float64(total)
		s += fmt.Sprintf("%d/%d (%0.1f%%)", val, total, pct)
	}
	return s
}

func main() {
	strategies := make([]strategy, win)
	for k := range strategies {
		strategies[k] = stayAtK(k + 1)
	}
	wins, games := roundRobin(strategies)

	for k := range strategies {
		fmt.Printf("Wins, losses staying at k =% 4d: %s
",
			k+1, ratioString(wins[k], games-wins[k]))
	}
}

```

code on [left](https://go.dev/doc/codewalk/functions/) • [right](https://go.dev/doc/codewalk/functions/) code width 70% filepaths [shown](https://go.dev/doc/codewalk/functions/) • [hidden](https://go.dev/doc/codewalk/functions/)
[](https://go.dev/doc/codewalk/?fileprint=/doc%2fcodewalk%2fpig.go&lo=0&hi=0#mark)
Introduction
Go supports first class functions, higher-order functions, user-defined function types, function literals, closures, and multiple return values.

This rich feature set supports a functional programming style in a strongly typed language.

In this codewalk we will look at a simple program that simulates a dice game called
doc/codewalk/pig.go
[](https://go.dev/doc/codewalk/?fileprint=/doc%2fcodewalk%2fpig.go&lo=17&hi=21#mark)
Game overview
Pig is a two-player game played with a 6-sided die. Each turn, you may roll or stay.
  * If you roll a 1, you lose all points for your turn and play passes to your opponent. Any other roll adds its value to your turn score.
  * If you stay, your turn score is added to your total score, and play passes to your opponent.

The first person to reach 100 total points wins.

The `score` type stores the scores of the current and opposing players, in addition to the points accumulated during the current turn.
doc/codewalk/pig.go:17,21
[](https://go.dev/doc/codewalk/?fileprint=/doc%2fcodewalk%2fpig.go&lo=23&hi=24#mark)
User-defined function types
In Go, functions can be passed around just like any other value. A function's type signature describes the types of its arguments and return values.

The `action` type is a function that takes a `score` and returns the resulting `score` and whether the current turn is over.

If the turn is over, the `player` and `opponent` fields in the resulting `score` should be swapped, as it is now the other player's turn.
doc/codewalk/pig.go:23,24
[](https://go.dev/doc/codewalk/?fileprint=/doc%2fcodewalk%2fpig.go&lo=26&hi=41#mark)
Multiple return values
Go functions can return multiple values.

The functions `roll` and `stay` each return a pair of values. They also match the `action` type signature. These `action` functions define the rules of Pig.
doc/codewalk/pig.go:26,41
[](https://go.dev/doc/codewalk/?fileprint=/doc%2fcodewalk%2fpig.go&lo=43&hi=44#mark)
Higher-order functions
A function can use other functions as arguments and return values.

A `strategy` is a function that takes a `score` as input and returns an `action` to perform.
(Remember, an `action` is itself a function.)
doc/codewalk/pig.go:43,44
[](https://go.dev/doc/codewalk/?fileprint=/doc%2fcodewalk%2fpig.go&lo=48&hi=53#mark)
Function literals and closures
Anonymous functions can be declared in Go, as in this example. Function literals are closures: they inherit the scope of the function in which they are declared.

One basic strategy in Pig is to continue rolling until you have accumulated at least k points in a turn, and then stay. The argument `k` is enclosed by this function literal, which matches the `strategy` type signature.
doc/codewalk/pig.go:48,53
[](https://go.dev/doc/codewalk/?fileprint=/doc%2fcodewalk%2fpig.go&lo=56&hi=70#mark)
Simulating games
We simulate a game of Pig by calling an `action` to update the `score` until one player reaches 100 points. Each `action` is selected by calling the `strategy` function associated with the current player.
doc/codewalk/pig.go:56,70
[](https://go.dev/doc/codewalk/?fileprint=/doc%2fcodewalk%2fpig.go&lo=72&hi=89#mark)
Simulating a tournament
The `roundRobin` function simulates a tournament and tallies wins. Each strategy plays each other strategy `gamesPerSeries` times.
doc/codewalk/pig.go:72,89
[](https://go.dev/doc/codewalk/?fileprint=/doc%2fcodewalk%2fpig.go&lo=91&hi=94#mark)
Variadic function declarations
Variadic functions like `ratioString` take a variable number of arguments. These arguments are available as a slice inside the function.
doc/codewalk/pig.go:91,94
[](https://go.dev/doc/codewalk/?fileprint=/doc%2fcodewalk%2fpig.go&lo=110&hi=121#mark)
Simulation results
The `main` function defines 100 basic strategies, simulates a round robin tournament, and then prints the win/loss record of each strategy.

Among these strategies, staying at 25 is best, but the
doc/codewalk/pig.go:110,121
[previous step](https://go.dev/doc/codewalk/functions/) • [next step](https://go.dev/doc/codewalk/functions/)
[ Why Go ](https://go.dev/solutions/) [ Use Cases ](https://go.dev/solutions/use-cases) [ Case Studies ](https://go.dev/solutions/case-studies)
[ Get Started ](https://go.dev/learn/) [ Playground ](https://go.dev/play) [ Tour ](https://go.dev/tour/) [ Help ](https://go.dev/help/)
[ Packages ](https://pkg.go.dev) [ Standard Library ](https://go.dev/pkg/) [ About Go Packages ](https://pkg.go.dev/about)
[ About ](https://go.dev/project) [ Download ](https://go.dev/dl/) [ Blog ](https://go.dev/blog/) [ Release Notes ](https://go.dev/doc/devel/release) [ Brand Guidelines ](https://go.dev/brand) [ Code of Conduct ](https://go.dev/conduct)
Opens in new window.
![The Go Gopher](https://go.dev/images/gophers/pilot-bust.svg)
  * [Copyright](https://go.dev/copyright)
  * [Terms of Service](https://go.dev/tos)
  * [ Report an Issue ](https://go.dev/s/website-issue)
  * ![System theme](https://go.dev/images/icons/brightness_6_gm_grey_24dp.svg) ![Dark theme](https://go.dev/images/icons/brightness_2_gm_grey_24dp.svg) ![Light theme](https://go.dev/images/icons/light_mode_gm_grey_24dp.svg)


go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic.
Okay
