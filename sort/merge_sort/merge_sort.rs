fn merge(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
    let mut merged: Vec<i32> = Vec::with_capacity(a.len() + b.len());
    let mut ai: usize = 0;
    let mut bi: usize = 0;
    while ai < a.len() && bi < b.len() {
        if a[ai] <= b[bi] {
            merged.push(a[ai]);
            ai += 1;
        }
        else {
            merged.push(b[bi]);
            bi += 1;
        }
    }
    for i in ai..a.len() {
        merged.push(a[i]);
    }
    for i in bi..b.len() {
        merged.push(b[i]);
    }
    merged
}

fn merge_sort(v: Vec<i32>) -> Vec<i32> {
    if v.len() <= 1 {
        v
    }
    else {
        let mid = v.len() / 2;
        let parts = v.split_at(mid);
        let a = merge_sort(parts.0.to_vec());
        let b = merge_sort(parts.1.to_vec());
        merge(a, b)
    }
}

fn main() {
    let a = vec![1, 5, 7, 4, 3, 2, 1, 9, 0, 10, 43, 64];
    let b = merge_sort(a);
    println!("{:?}", b);
}

#[test]
fn test() {
    assert_eq!(
        merge_sort(vec![1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100, 4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]),
        vec![-5, -2, -1, 0, 1, 1, 2, 4, 5, 9, 10, 23, 32, 43, 57, 64, 65, 100, 242, 423, 564, 999, 1232]
    );
}
