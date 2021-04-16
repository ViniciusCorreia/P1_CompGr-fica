
void draw(){
  background(500);
  int margin = 20;
  float x = 0;
  float y = 0;
  
  
  float n = round(map(mouseX, 0, width, 3, 10));
  float a = TWO_PI/n;
  float h = a/2;
  
  
  float r = (width/2) - margin;
  float r2 = r * map(mouseY, 0, width, 0.3, 0.5);
  
  
  beginShape();
  translate(width/2, height/2);
  for(float i=0; i< TWO_PI;i+=a){
    float sx = x + r2 * cos(i);
    float sy = y + r2 * sin(i);
    vertex(sx,sy);
    sx = x + cos(i+h) * r;
    sy = y+ sin(i+h) * r;
    vertex(sx,sy);
  }
  endShape();
}
void setup(){
 size(800,800); 
}
