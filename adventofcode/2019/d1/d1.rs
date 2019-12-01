use std::cmp::max;

fn parse_input() -> Vec<i32> {
  let file = include_str!("./input.txt");

  file.lines()
    .map(|x| i32::from_str_radix(x, 10).unwrap())
    .collect()
}

fn calc_fuel(mass:&i32) -> i32 {
  max(mass / 3 - 2, 0)
}

fn calc_true_fuel(mass:&i32) -> i32 {
  match calc_fuel(mass) {
    0 => 0,
    fuel => fuel + calc_true_fuel(&fuel),
  }
}

fn main() {
  let masses = parse_input();

  // p1
  println!("{}", masses.iter().map(calc_fuel).sum::<i32>());

  // p2
  println!("{}", masses.iter().map(calc_true_fuel).sum::<i32>());
}
