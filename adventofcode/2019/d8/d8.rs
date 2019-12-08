
fn main() {
  let nums: Vec<u32> = include_str!("./input.txt")
    .chars()
    .map(|i| i.to_digit(10).unwrap())
    .collect();

  const W: usize = 25;
  const H: usize = 6;
  const SIZE: usize = W * H;

  // p1
  let best = nums
    .chunks(SIZE)
    .min_by_key(|&layer| layer.iter().filter(|&x| *x == 0).count())
    .unwrap();

  let count_1s = best.iter().filter(|&x| *x == 1).count();
  let count_2s = best.iter().filter(|&x| *x == 2).count();

  println!("Part 1: {}", count_1s * count_2s);

  // p2
  let mut img = vec![2u32; SIZE];
  nums.chunks(SIZE).rev().for_each(|c| {
    c.iter().enumerate().for_each(|(i, x)| {
      if *x != 2 {
        img[i] = *x;
      }
    })
  });

  show(img.chunks_exact(W).collect());
}

fn show(chunks: Vec<&[u32]>) {
  chunks.iter().for_each(|l| {
    let line: String = l
      .iter()
      .map(|p| match p {
        1 => '#',
        _ => ' ',
      })
      .collect();
    println!("{}", line);
  })
}
