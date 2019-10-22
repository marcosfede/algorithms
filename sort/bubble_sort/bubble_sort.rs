fn bubble_sort(v: &Vec<i32>) -> Vec<i32> {
    let mut a = v.clone();
    let mut swapped = true;
    while swapped {
        swapped = false;
        for i in 1..(v.len()) {
            if a[i - 1] > a[i] {
                let aux = a[i];
                a[i] = a[i - 1];
                a[i - 1] = aux;
                swapped = true;
            }
        }
    }
    a
}

fn main() {
    let a = vec![
        1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
        4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999,
    ];
    let b = bubble_sort(&a);
    println!("{:?}", b);
}

#[test]
fn test() {
    assert_eq!(
        bubble_sort(&vec![1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100, 4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]),
        vec![-5, -2, -1, 0, 1, 1, 2, 4, 5, 9, 10, 23, 32, 43, 57, 64, 65, 100, 242, 423, 564, 999, 1232]
    );
}
