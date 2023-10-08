package main
import "fmt"

const a = "100"

type obj interface {
	swap()
	area() float64
}

type Circle struct {
	rad float64
}

type Square struct {
	side float64
}

func (c *Circle) area() {
	return 4*3.14*c.rad*c.rad
}

func (s *Square) area() {
	return s.side * s.side
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

