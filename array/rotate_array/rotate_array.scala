def rotate_array(input:Array[Int], k:Int):Array[Int] = {
    val N = input.length
    val K = k % N
    return input.slice(N - K, N) ++ input.slice(0, N - K)
}