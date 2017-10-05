package main 
import(
		"fmt"
)

func binarySearch(list [] int,n int) bool {
	
	first := 0
	last := len(list)-1
	found := false
	
	for first <= last {
		mp := (first + last) / 2
		if list[mp]==n{
			found = true
		}
		
		if n < list[mp]{
			last = mp-1
		}	else {
			first = mp+1
		}			
	}
	return found
	
}

func  main() {
	list := []int{1, 4, 6, 10, 15, 17, 20}
	fmt.Println(binarySearch(list,15)) 
	
}