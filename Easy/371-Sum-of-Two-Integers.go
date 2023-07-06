package main

import "fmt"

func main() {
    var a int = 5
    var b int = 2
    var c int = getSum(a, b)
    fmt.Println(c)
}

func getSum(a int, b int) int {
    var sum = a + b
    return sum
}