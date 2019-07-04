fn circular_counter(a: &Vec<i32>) -> Vec<i32> {
    let mut a2 = a.clone();
    let mut i = 0;
    let mut b = vec![];
    while a2.len() > 0 {
        i = (i + 2) % a2.len();
        b.push(a2[i]);
        a2.remove(i);
    }
    b
}

fn main() {
    let a = vec![1, 2, 3, 4, 5, 6, 7, 8, 9];
    let b = circular_counter(&a);
    println!("{:?}", b);
}
