import java.io.File;
import java.util.*;

public class Route
{
  public static void main(String[] args) throws Exception
  {
    // pass the path to the file as a parameter
    File file =
      new File("./data");
    Scanner sc = new Scanner(file);

    String[] one = sc.nextLine().split(",");
    String[] two = sc.nextLine().split(",");

    task(one, two);
    
    one = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",");
    two = "U62,R66,U55,R34,D71,R55,D58,R83".split(",");

    task(one, two);


    one = "R8,U5,L5,D3".split(",");
    two = "U7,R6,D4,L4".split(",");

    task(one, two);
  }

  private static void task(String[] one, String[] two)
  {

    Coord first = new Coord(0,0);
    Coord second = new Coord(0,0);

    List<Coord> pathOne = new ArrayList<Coord>();
    List<Coord> pathTwo = new ArrayList<Coord>();
    List<Coord> crosses = new ArrayList<Coord>();
    List<Integer> distances = new ArrayList<Integer>();


    for(int i = 0; i < one.length; i++)
    {
      char direction = one[i].charAt(0);
      int distance = Integer.parseInt(one[i].substring(1));

      Coord next = null;

      switch(direction) {
        case 'D':
          next = first.down(distance); 
          break;
        case 'U':
          next = first.up(distance); 
          break;
        case 'L':
          next = first.left(distance); 
          break;
        case 'R':
          next = first.right(distance); 
          break;
      }
      pathOne.add(next);
      first = next;

    }

    
    for(int i = 0; i < two.length; i++)
    {
      char direction = two[i].charAt(0);
      int distance = Integer.parseInt(two[i].substring(1));

      Coord next = null;

      switch(direction) {
        case 'D':
          next = second.down(distance); 
          break;
        case 'U':
          next = second.up(distance); 
          break;
        case 'L':
          next = second.left(distance); 
          break;
        case 'R':
          next = second.right(distance); 
          break;
      }
      pathTwo.add(next);
      second = next;
      
    }


    int iDist = 0;
    for(int i = 0; i < pathOne.size() - 1; i++)
    {
      iDist += Integer.parseInt(one[i].substring(1));
      int jDist = 0;
      for(int j = 0; j < pathTwo.size() - 1; j++)
      {
        jDist += Integer.parseInt(two[j].substring(1));

        Coord intersect = intersects(pathOne.get(i), pathOne.get(i+1), pathTwo.get(j), pathTwo.get(j+1));

        if(intersect != null)
        {
          crosses.add(intersect);
          distances.add(iDist + jDist +pathOne.get(i).distanceTo(intersect) + pathTwo.get(j).distanceTo(intersect));
        }
      }
    }

    /*
    *
    //System.out.println(pathOne);
    int least = 10000000;

    for(Coord cross: crosses)
    {
      int dist = cross.manhattanDistance();
      least = Math.min(dist, least);
    }

    System.out.println(least);

    */

    int least = 10000000;

    for(int dist: distances)
      least = Math.min(least,dist);
 
    //System.out.println(distances);
    System.out.println(least);
  }


  private static Coord intersects(Coord p11, Coord p12, Coord p21, Coord p22)
  {
    if(p11.x == p12.x) // p1 is vertical
    {
      if(p21.x == p22.x)
        return null;
      else
      {
        if(Math.max(p11.y, p12.y) >= p21.y && Math.min(p11.y, p12.y) <= p21.y &&
           Math.max(p21.x, p22.x) >= p11.x && Math.min(p21.x, p22.x) <= p11.x)
          return new Coord(p11.x, p21.y);
        else
          return null;
      }
    }
    else // p1 is horizontal
    {
      if(p21.y == p22.y)
        return null;
      else
      {
        if(Math.max(p11.x, p12.x) >= p21.x && Math.min(p11.x, p12.x) <= p21.x &&
           Math.max(p21.y, p22.y) >= p11.y && Math.min(p21.y, p22.y) <= p11.y)
          return new Coord(p21.x, p11.y);
        else
          return null;
      }
    }
  }

} // route
