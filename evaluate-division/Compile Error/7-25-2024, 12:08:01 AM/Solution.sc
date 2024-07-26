// https://leetcode.com/problems/evaluate-division

    def calcEquation(eq: List[List[String]], vals: Array[Double], q: List[List[String]]): Array[Double] = 

       val m = Map.empty[String,Map[String,Double]]

       val fn = (a:String, b:String,r:Double) => 
          m.getOrElseUpdate(a,Map())(b) = r
          m.getOrElseUpdate(b,Map())(a) = 1.0/r

       eq.zipWithIndex.foreach: 
         case (List(a,b), i) => fn(a,b,vals(i))
         case _ =>

       m.foreach: (a,ratios) => 
        ratios.foreach: (b, ab) => 
            m(b).foreach: (c, bc) =>
              fn(a, c, ab * bc)

       val ans = Array.fill(q.size)(-1.0)
       q.zipWithIndex.foreach: 
        case (List(a,b), i) => 
          m.contains(a) && m.contains(b) match 
           case true => (m(b).contains(a)) match
               case true => 
                ans(i) = 1 / m(b)(a)
               case false => 
                m(b).keys.find(m(a).contains) match
                  case Some(x) =>
                    ans(i) = m(a)(x) / m(b)(x)
                    fn(a,b,ans(i))
                  case None => 
           case _ =>
        case _ =>

       ans
}