import scala.io.Source

object d1 extends App {
    val masses = Source.fromFile("input.txt").getLines.map(_.toInt).toList

    def calcFuel(mass: Int) =
        mass / 3 - 2

    println(masses.map(calcFuel).sum)

    def calcAllFuel(mass: Int) = Iterator.iterate(calcFuel(mass))(calcFuel)

    println(masses.map(calcAllFuel(_).takeWhile(_ > 0).sum).sum)
}