package main
import "fmt"

const a = "100"

func swap(sw []int) {
	for a,b := 0, len(sw)-1; a < b ; a,b = a+1, b-1 {
		sw[a], sw[b] = sw[b], sw[a]
	}
}

func main() {

	x := []int{3, 2, 1}
	swap(x)
	fmt.Println(x)
	fmt.Println(a)

}

