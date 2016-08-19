#version 110

uniform vec2 WindowSize;

void main() {
  // Assuming screen width 512, need to fix this:
  // See: https://www.opengl.org/registry/doc/GLSLangSpec.Full.1.20.8.pdf

  float fx = gl_FragCoord[0] / WindowSize[0];
  float fy = gl_FragCoord[1] / WindowSize[1];
  float fz = gl_FragCoord[2];
  float fiw = gl_FragCoord[3];

  gl_FragColor = vec4(fx, fy, fz, 1.0);

}