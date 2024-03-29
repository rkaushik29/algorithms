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

func printArea(t test) {
    fmt.Println("Area:", t.area())
}

func main() {

	circle := &Circle{rad: 2}
    square := &Square{side: 2}
	
	x := []int{3, 2, 1}
	swap(x)
	fmt.Println(x)
	fmt.Println(a)
	fmt.printArea(circle)
	fmt.printArea(square)

}

