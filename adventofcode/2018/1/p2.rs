use std::fs;
use std::collections::HashSet;

fn main() {
    let mut set: HashSet<i32> = vec!().into_iter().collect();
    let mut sum = 0;

    'outer: loop {
        for n in fs::read_to_string("input").expect("Unable to read file")
            .lines()
            .filter_map(|s| s.parse::<i32>().ok()) {
            sum += n;
            if set.contains(&sum) {
                break 'outer;
            }
            set.insert(sum);
        }
    }
    println!("{}", sum);
}
