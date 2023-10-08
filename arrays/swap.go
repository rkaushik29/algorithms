package main
import "fmt"

const a = "100"

type test interface {
	swap()
	area() int
}

func swap(sw []int) {
	for a,b := 0, len(sw)-1; a < b ; a,b = a+1, b-1 {
		sw[a], sw[b] = sw[b], sw[a]
	}
}

func area(a int, b int) (int) {
	return a * b
}

func main() {

	x := []int{3, 2, 1}
	swap(x)
	fmt.Println(x)
	fmt.Println(a)

}

