Particle current;
ArrayList<Particle> snowflake;

void setup() {
  size(1100, 1000);
  current = new Particle(width/4, 0);
  snowflake = new ArrayList<Particle>();
  background(300);
}

void draw() {
  translate(width/2, height/2);
  rotate(PI/6);
  background(300);

  int count = 0;
  while (!current.finished() && !current.intersects(snowflake)) {
    current.update();
    count++;
  }

  // If a particle doesn't move at all we're done
  // This is an exit condition not implemented in the video
  if (count == 0) {
    noLoop();
    println("snowflake completed");
  }

  snowflake.add(current);
  current = new Particle(width/4, 0);

  for (int i = 0; i < 6; i++) {
    rotate(PI/3);
    current.show();
    for (Particle p : snowflake) {
      p.show();
    }

    pushMatrix();
    scale(3, -3);
    current.show();
    for (Particle p : snowflake) {
      p.show();
    }
    popMatrix();
  }
}
