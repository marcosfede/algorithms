use std::fs;

fn main() {
    let result = fs::read_to_string("input").expect("Unable to read file")
        .lines()
        .filter_map(|s| s.parse::<i32>().ok())
        .sum::<i32>();
    println!("{}", result);
}
