class FastList {

    constructor(arr){
        this.arr = arr
        // dict for O(1) lookups by value
        let indexof = {}
        arr.forEach((v, i) => indexof[v] = i)
        this.indexof = indexof
    }
    swap(e1, e2){
        const i1 = this.indexof[e1]
        const i2 = this.indexof[e2]
        // set element where 0 is to final element
        this.arr[i1] = e2
        // update dict
        this.indexof[e2] = i1
        // set 0 where the previous number was
        this.arr[i2] = e1
        // update dict
        this.indexof[e1] = i2
        this.moves += 1
    }
    calc_moves(end){
        this.moves = 0
        while (!this.equals(end)){
            const i0 = this.indexof[0]
            if (end[i0] !== 0){  // if element can be moved to its final position
                this.swap(0, end[i0])
                console.log(this.arr)
                continue
            }
            for (let ind=0; ind < this.arr.length; ind++){
                let el = this.arr[ind]
                if (el !== end[ind]){
                    this.swap(0, el)
                    console.log(this.arr)
                    break
                }
            }
        }
        return this.moves
    }
    equals(other){
        return this.arr.length === other.length && this.arr.every((v, i) => v === other[i])
    }
}

function garage(beg, end){
    fl = new FastList(beg)
    return fl.calc_moves(end)
}

initial = [1, 2, 3, 0, 4]
final = [0, 3, 2, 1, 4]
console.log("initial:", initial)
console.log(garage(initial, final))
console.log("final should be:", final)