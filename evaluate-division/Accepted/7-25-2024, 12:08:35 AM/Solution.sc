// https://leetcode.com/problems/evaluate-division

object Solution:
  import collection.mutable

  def calcEquation(equations: List[List[String]], values: Array[Double], queries: List[List[String]]): Array[Double] =
    val graph = mutable.Map[String, mutable.Map[String, Double]]()

    // build the graph from input
    for (i <- equations.indices)
      val equation = equations(i)
      val dividend = equation(0)
      val divisor = equation(1)
      val quotient = values(i)

      if (!graph.contains(dividend))
        graph.addOne(dividend, mutable.Map())
      if (!graph.contains(divisor))
        graph.addOne(divisor, mutable.Map())

      graph(dividend).addOne(divisor, quotient)
      graph(divisor).addOne(dividend, 1 / quotient)
    def dfs(curr: String, target: String, accProduct: Double, visited: Set[String]): Double =
      if (curr == target) accProduct
      else if (visited.contains(curr)) -1.0
      else
        graph(curr)
          .map((next, weight) => dfs(next, target, accProduct * weight, visited + curr))
          .find(_ != -1.0)
          .getOrElse(-1.0)

    val result =
      for (List(dividend, divisor) <- queries) yield
        if (!graph.contains(dividend) || !graph.contains(divisor)) -1.0
        else dfs(dividend, divisor, 1.0, Set.empty)

    result.toArray