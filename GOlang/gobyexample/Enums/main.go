package main

import "fmt"

type serverState int

const (
	StateIdle serverState = iota
	StateConnected
	StateError
	StateRetrying
)

var stateName = map[serverState]string{
	StateIdle:      "idle",
	StateConnected: "connected",
	StateError:     "error",
	StateRetrying:  "retrying",
}

func (ss serverState) String() string {
	return stateName[ss]
}

func main() {
	var s serverState
	fmt.Println(s)

	fmt.Println(StateConnected)

	fmt.Println(stateName)

	for i, v := range stateName {
		println(i, v)
	}

	ns := transition(StateIdle)
	fmt.Println(ns)

	ns2 := transition(ns)
	fmt.Println(ns2)
}

func transition(s serverState) serverState {
	switch s {
	case StateIdle:
		return StateConnected
	case StateConnected, StateRetrying:
		return StateIdle
	case StateError:
		return StateError
	default:
		panic(fmt.Errorf("unknown state: %v", s))
	}
}
