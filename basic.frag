#version 330

uniform vec2 resolution;
uniform vec2 circle;
uniform vec2 r_offset;
out vec4 FragColor;
void main()
{
    float pos_x=gl_FragCoord.x / resolution.x;
    float pos_y=gl_FragCoord.y / resolution.y;
    float z_real = 1*(pos_x * 3.5 - 2.5+.75)-.75;
    float z_imag = 1*(pos_y * 2.0 - 1.0);
    float real = r_offset.x;
    float imaginary = r_offset.y;
    bool fractal=true;
    float brightness=-0.2;
    float temp_real=0.0;
    for(float i=0;i<100;i++){
        temp_real=z_real;
        z_real=z_real*z_real-z_imag*z_imag+real;
        z_imag=2*temp_real*z_imag+imaginary;
            if (abs(z_imag*z_imag)+abs(z_real*z_real)>16){
            brightness+=0.04;
            fractal=false;
        }
    }
    float red=0.01;
    float green=0;
    float blue=0;
    if (fractal){
        brightness=0.0;
        float rel_x=pos_x-circle.x;
        float rel_y=pos_y-circle.y;
        float dist=rel_x*rel_x+rel_y*rel_y;
        brightness=brightness+.1/dist;
        red=brightness+.1*r_offset.y/dist;
        green=brightness+.05*r_offset.x/dist;
        blue=brightness;


    }

    FragColor = vec4(brightness+red,brightness+green,brightness+blue,1.0);
}