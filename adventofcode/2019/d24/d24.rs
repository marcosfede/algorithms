use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};

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
        num += 2usize.pow((y * grid[0].len() + x) as u32)
      }
    }
  }
  num
}

type Grid = Vec<Vec<char>>;

fn neighbours(grid: &Grid, x: usize, y: usize) -> usize {
  let mut n = 0;
  let ix = x as isize;
  let iy = y as isize;
  let dirs = [(ix - 1, iy), (ix + 1, iy), (ix, iy + 1), (ix, iy - 1)];
  for &pos in dirs.iter() {
    let (xp, yp) = pos;
    if 0 <= xp && xp < (grid[0].len() as isize) && 0 <= yp && yp < (grid.len() as isize) {
      if grid[yp as usize][xp as usize] == '#' {
        n += 1;
      }
    }
  }
  return n;
}

fn step(grid: &Grid) -> Grid {
  let mut new: Grid = grid.clone();
  for (y, row) in grid.iter().enumerate() {
    for (x, &ch) in row.iter().enumerate() {
      if ch == '#' {
        let n = neighbours(&grid, x, y);
        if n != 1 {
          new[y][x] = '.';
        }
      } else {
        let n = neighbours(&grid, x, y);
        if n == 1 || n == 2 {
          new[y][x] = '#';
        }
      }
    }
  }
  return new;
}

#[derive(PartialEq, Eq, Hash, Copy, Clone, Debug)]
struct Cell {
  x: usize,
  y: usize,
  d: isize,
}

fn get_recursive_neighbours(c: &Cell) -> Vec<Cell> {
  let mut neigh: Vec<Cell> = vec![];
  let ix = c.x as isize;
  let iy = c.y as isize;
  let dirs = [(ix - 1, iy), (ix + 1, iy), (ix, iy + 1), (ix, iy - 1)];
  for &pos in dirs.iter() {
    match pos {
      (-1, _) => neigh.push(Cell {
        x: 1,
        y: 2,
        d: c.d - 1,
      }),
      (5, _) => neigh.push(Cell {
        x: 3,
        y: 2,
        d: c.d - 1,
      }),
      (_, -1) => neigh.push(Cell {
        x: 2,
        y: 1,
        d: c.d - 1,
      }),
      (_, 5) => neigh.push(Cell {
        x: 2,
        y: 3,
        d: c.d - 1,
      }),
      (2, 2) => match (c.x, c.y) {
        (1, 2) => neigh.extend((0..5).map(|y| Cell {
          x: 0,
          y: y,
          d: c.d + 1,
        })),
        (3, 2) => neigh.extend((0..5).map(|y| Cell {
          x: 4,
          y: y,
          d: c.d + 1,
        })),
        (2, 1) => neigh.extend((0..5).map(|x| Cell {
          x: x,
          y: 0,
          d: c.d + 1,
        })),
        (2, 3) => neigh.extend((0..5).map(|x| Cell {
          x: x,
          y: 4,
          d: c.d + 1,
        })),
        _ => {}
      },
      (xp, yp) => neigh.push(Cell {
        x: xp as usize,
        y: yp as usize,
        d: c.d,
      }),
    }
  }

  return neigh;
}

fn bugs_near(bugs: &HashSet<Cell>, c: &Cell) -> usize {
  return get_recursive_neighbours(c)
    .iter()
    .map(|n| if bugs.contains(n) { 1 } else { 0 })
    .sum();
}

fn part1() {
  let mut grid = parse("input.txt");
  let mut set: HashSet<usize> = HashSet::new();
  loop {
    grid = step(&grid);
    let br = bio_rating(&grid);
    if set.contains(&br) {
      println!("part1: {}", br);
      return;
    }
    set.insert(br);
  }
}

fn part2() {
  let grid = parse("input.txt");
  let mut bugs: HashSet<Cell> = HashSet::new();

  for (y, row) in grid.iter().enumerate() {
    for (x, &ch) in row.iter().enumerate() {
      if ch == '#' {
        bugs.insert(Cell { x, y, d: 0 });
      }
    }
  }

  for _ in 0..200 {
    let mut new_bugs: HashSet<Cell> = HashSet::new();
    let mut empty_spaces_nearby: HashSet<Cell> = HashSet::new();

    for bug in bugs.iter() {
      for neighbour in get_recursive_neighbours(bug).iter() {
        if !bugs.contains(neighbour) {
          empty_spaces_nearby.insert(*neighbour);
        }
      }
    }

    for bug in bugs.iter() {
      if bugs_near(&bugs, bug) == 1 {
        new_bugs.insert(*bug);
      }
    }

    for empty in empty_spaces_nearby.iter() {
      let bn = bugs_near(&bugs, empty);
      if bn == 1 || bn == 2 {
        new_bugs.insert(*empty);
      }
    }

    bugs = new_bugs;
  }

  println!("part2: {}", bugs.len());
}

fn main() {
  part1();
  part2();
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn test_recursive_neighbours() {
    assert_eq!(
      get_recursive_neighbours(&Cell { x: 0, y: 0, d: 0 })
        .drain(..)
        .collect::<HashSet<Cell>>(),
      vec!(
        Cell { x: 1, y: 2, d: -1 },
        Cell { x: 2, y: 1, d: -1 },
        Cell { x: 1, y: 0, d: 0 },
        Cell { x: 0, y: 1, d: 0 }
      )
      .drain(..)
      .collect::<HashSet<Cell>>()
    );

    assert_eq!(
      get_recursive_neighbours(&Cell { x: 2, y: 0, d: 0 })
        .drain(..)
        .collect::<HashSet<Cell>>(),
      vec!(
        Cell { x: 1, y: 0, d: 0 },
        Cell { x: 3, y: 0, d: 0 },
        Cell { x: 2, y: 1, d: 0 },
        Cell { x: 2, y: 1, d: -1 }
      )
      .drain(..)
      .collect::<HashSet<Cell>>()
    );

    assert_eq!(
      get_recursive_neighbours(&Cell { x: 1, y: 2, d: 0 })
        .drain(..)
        .collect::<HashSet<Cell>>(),
      vec!(
        Cell { x: 0, y: 2, d: 0 },
        Cell { x: 1, y: 1, d: 0 },
        Cell { x: 1, y: 3, d: 0 },
        Cell { x: 0, y: 0, d: 1 },
        Cell { x: 0, y: 1, d: 1 },
        Cell { x: 0, y: 2, d: 1 },
        Cell { x: 0, y: 3, d: 1 },
        Cell { x: 0, y: 4, d: 1 },
      )
      .drain(..)
      .collect::<HashSet<Cell>>()
    );

    assert_eq!(
      get_recursive_neighbours(&Cell { x: 2, y: 3, d: 0 })
        .drain(..)
        .collect::<HashSet<Cell>>(),
      vec!(
        Cell { x: 1, y: 3, d: 0 },
        Cell { x: 3, y: 3, d: 0 },
        Cell { x: 2, y: 4, d: 0 },
        Cell { x: 0, y: 4, d: 1 },
        Cell { x: 1, y: 4, d: 1 },
        Cell { x: 2, y: 4, d: 1 },
        Cell { x: 3, y: 4, d: 1 },
        Cell { x: 4, y: 4, d: 1 },
      )
      .drain(..)
      .collect::<HashSet<Cell>>()
    );

    assert_eq!(
      get_recursive_neighbours(&Cell { x: 4, y: 2, d: 0 })
        .drain(..)
        .collect::<HashSet<Cell>>(),
      vec!(
        Cell { x: 3, y: 2, d: 0 },
        Cell { x: 4, y: 1, d: 0 },
        Cell { x: 4, y: 3, d: 0 },
        Cell { x: 3, y: 2, d: -1 },
      )
      .drain(..)
      .collect::<HashSet<Cell>>()
    );
  }
}
