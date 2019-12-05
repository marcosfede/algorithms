use std::collections::HashMap;

fn counter(iter: &str) -> HashMap<char, usize> {
  let mut d = HashMap::new();
  for elem in iter.chars() {
    let count = d.entry(elem).or_insert(0);
    *count += 1;
  }
  d
}

fn valid<F>(code: usize, pred: F) -> bool
where
  F: Fn(&Vec<&usize>) -> bool,
{
  let scode = code.to_string();
  if !scode[..]
    .chars()
    .zip(scode[1..].chars())
    .all(|(a, b)| b >= a)
  {
    return false;
  }
  let c = counter(&scode);
  let counts: Vec<&usize> = c.values().collect();
  pred(&counts)
}

fn main() {
  let a = 284639;
  let b = 748759;

  println!(
    "{}",
    (a..b)
      .map(|n| valid(n, |counts| counts.iter().any(|&c| *c > 1)))
      .map(|b| b as usize)
      .sum::<usize>()
  );

  println!(
    "{}",
    (a..b)
      .map(|n| valid(n, |counts| counts.iter().any(|&c| *c == 2)))
      .map(|b| b as usize)
      .sum::<usize>()
  );
}
