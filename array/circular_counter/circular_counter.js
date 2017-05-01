let a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

function circCounter(arr, skip){
    let index = 0
    while (arr.length > 0){
        index = (index+skip-1) % arr.length
        console.log(arr.splice(index, 1)[0])
    }
}

circCounter(a, 3)