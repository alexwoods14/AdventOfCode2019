public class Coord
{
  public int x;
  public int y;

  public Coord(int x, int y)
  {
    this.x = x;
    this.y = y;
  } 


  @Override
  public boolean equals(Object o)
  {

    if(o == null)
      return false;

    if(this == o)
      return true;

    if((o instanceof Coord) && ((Coord)o).x == this.x && ((Coord)o).y == this.y)
      return true;
    else
      return false;

  }

  public Coord up(int i) {
    return new Coord(x, y + i);
  }
  public Coord down(int i) {
    return new Coord(x, y - i);
  }
  public Coord left(int i) {
    return new Coord(x - i, y);
  }
  public Coord right(int i) {
    return new Coord(x + i, y);
  }

  public int manhattanDistance() {
    return Math.abs(x) + Math.abs(y);
  }

  public int distanceTo(Coord other) {
    return Math.abs(this.x - other.x) + Math.abs(this.y - other.y);
  }

  @Override
  public int hashCode()
  {
    return (int)(Math.pow(2.0,x) * Math.pow(3.0,y));
  }

  @Override
  public String toString()
  {
    return String.format("(%4d, %4d)", x, y);
  }

} // Coord
