#version 110
#extension GL_EXT_gpu_shader4 : require

uniform vec2 WindowSize;
uniform vec2 XY;
uniform int data[256];

void main() {
  // See: https://www.opengl.org/registry/doc/GLSLangSpec.Full.1.20.8.pdf

  float fx = gl_FragCoord[0] / WindowSize[0];
  float fy = gl_FragCoord[1] / WindowSize[1];
  float fz = float(data[int(gl_FragCoord[0]) % 256]) / 256.0;

  if (distance(gl_FragCoord.xy, XY) < 5.0)
  {
    gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
  }
  else
  {
    gl_FragColor = vec4(fx, fy, fz, 1.0);
  }

}