fn rotate_array(v: &Vec<i32>, n: usize) -> Vec<i32> {
    let mut a = v.clone();
    let len = a.len();
    let mut b = a.split_off(len - n);
    b.append(&mut a);
    b
}

fn main() {
    let a = vec![1, 2, 3, 4, 5, 6, 7];
    let b = rotate_array(&a, 3);
    println!("{:?}", b);
}
