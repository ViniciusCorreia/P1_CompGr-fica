float Xpl = 100;
float Ypl = 600;
float Xp4 = 700;
float Yp4 = 200;

boolean Clickp2 = false;
boolean Clickp3 = false;

void setup()
{
  size(1000,800);
}

float p2_x = 300;
float p2_y = 200;
float p3_x = 500;
float p3_y = 600;
void draw() {
  background(500);
  
  if(Clickp2)
  {
    p2_x = mouseX;
    p2_y = mouseY;
  }
  else if(Clickp3)
  {
    p3_x = mouseX;
    p3_y = mouseY;
  }
  noFill();
  beginShape();
  for(float i = 0; i <= 1; i += 0.01) {
    float ax = Xpl + i*(p2_x-Xpl);
    float ay = Ypl + i*(p2_y-Ypl);
    float bx = p2_x + i*(p3_x-p2_x);
    float by = p2_y + i*(p3_y-p2_y);
    float cx = p3_x + i*(Xp4-p3_x);
    float cy = p3_y + i*(Yp4-p3_y);
    float dx = ax + i*(bx-ax);
    float dy = ay + i*(by-ay);
    float ex = bx + i*(cx-bx);
    float ey = by + i*(cy-by);
    float fx = dx + i*(ex-dx);
    float fy = dy + i*(ey-dy);
    vertex(fx, fy);
  }
  endShape();
  fill(0, 0, 0);
  circle(Xpl, Ypl, 5);
  circle(p2_x, p2_y, 5);
  circle(p3_x, p3_y, 5);
  circle(Xp4, Yp4, 5);
}
void mouseReleased()
{
  Clickp2 = false;
  Clickp3 = false;
}
void mousePressed()
{
    if(dist(p2_x, p2_y, mouseX, mouseY) < 10)
    {
      Clickp2 = true;
    }
    if(dist(p3_x, p3_y, mouseX, mouseY) < 10)
    {
      Clickp3 = true;
    }
  
}
