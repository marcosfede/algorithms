fn run(program: Vec<usize>) -> usize {
  let mut arr = program.clone();
  let mut i = 0;
  loop {
    let op = arr[i];
    if op == 99 {
      return arr[0];
    }
    let a = arr[i + 1];
    let b = arr[i + 2];
    let to = arr[i + 3];
    if op == 1 {
      arr[to] = arr[a] + arr[b]
    } else if op == 2 {
      arr[to] = arr[a] * arr[b]
    }
    i += 4
  }
}

fn main() {
  let program: Vec<usize> = include_str!("./input.txt")
    .split(",")
    .map(|i| i.parse::<usize>().unwrap())
    .collect();

  // p1
  let mut p1 = program.clone();
  p1[1] = 12;
  p1[2] = 2;
  println!("{}", run(p1));

  // p2
  for x in 0..100 {
    for y in 0..100 {
      let mut p2 = program.clone();
      p2[1] = x;
      p2[2] = y;
      if run(p2) == 19690720 {
        println!("{}", 100 * x + y)
      }
    }
  }
}
