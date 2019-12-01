const fs = require('fs')

const masses = fs.readFileSync('./input.txt').toString().split("\n").map(Number)

const calcFuel = n => Math.floor(n / 3) - 2;

const calcTotalFuel = n => {
  const fuel = calcFuel(n);
  return fuel <= 0 ? 0 : fuel + calcTotalFuel(fuel);
};

const sum = (a, b) => a + b;

// p1
console.log(masses.map(calcFuel).reduce(sum))

// p2
console.log(masses.map(calcTotalFuel).reduce(sum))
