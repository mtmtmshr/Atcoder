package main

import (
    "fmt"
	"strings"
)

func main() {
	var str string
	var a int
	fmt.Scan(&a)
	fmt.Scan(&str)
	for {
		if !strings.Contains(str, "fox") { break }
		str = strings.Replace(str, "fox", "", -1)
	}
	fmt.Println(len(str))
}
