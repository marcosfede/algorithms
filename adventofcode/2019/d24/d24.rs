use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;

type Grid = Vec<Vec<char>>;
fn neighbours(grid:&Grid, x: usize, y: usize) -> usize {
  let mut n = 0;
  let ix = x as isize;
  let iy = y as isize;
  let dirs = [(ix-1,iy), (ix+1,iy), (ix,iy+1), (ix,iy-1)];
  for &pos in dirs.iter() {
    let (xp, yp) = pos;
    if 0 <= xp && xp < (grid[0].len() as isize) && 0<= yp && yp < (grid.len() as isize) {
      if grid[yp as usize][xp as usize] == '#' {
        n += 1;
      }
    }
  }
  return n
}

fn step(grid: &Grid) -> Grid {
  let mut new:Grid = grid.clone();
  for (y, row) in grid.iter().enumerate() {
    for (x, &ch) in row.iter().enumerate() {
      if ch == '#' {
          let n = neighbours(&grid, x, y);
          if n != 1 {
            new[y][x] = '.';
          }
        }
        else {
          let n = neighbours(&grid,x,y);
          if n == 1 || n == 2 {
            new[y][x] = '#';
          }
        }
      }
    }
    return new;
}

fn parse(filename: &str) -> Grid {
  let reader = BufReader::new(File::open(filename).unwrap());
  let mut grid: Vec<Vec<char>> = vec![];
  for line in reader.lines() {
    grid.push(line.unwrap().chars().collect());
  }
  grid
}

fn bio_rating(grid: &Grid) -> usize {
  let mut num = 0;
  for (y, row) in grid.iter().enumerate() {
    for (x, _) in row.iter().enumerate() {
      if grid[y][x] == '#' {
        num += 2usize.pow((y*grid[0].len() + x) as u32)
      }
    }
  }
  num
}

fn main() {
  let mut grid = parse("input.txt");
  let mut set:HashSet<usize> = HashSet::new();
  loop {
    grid = step(&grid);
    let br = bio_rating(&grid);
    if set.contains(&br) {
      println!("bio rating: {}", br);
      return
    }
    set.insert(br);
  }
}
