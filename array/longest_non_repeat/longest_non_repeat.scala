def longest_non_repeat(input:String): String = {
    var longest = ""
    for (i <- 0 until input.length) {
        var str = ""
        var used = Set[Char]()
        var goOn = true
        for (j <- i until input.length if goOn){
            if (! used.contains(input(j))){
                str += input(j)           
                used += input(j)
            } 
            else{
                str = input(j).toString
                goOn = false
            }
            if (str.length > longest.length)
                longest = str
        }
    }
    return longest
}