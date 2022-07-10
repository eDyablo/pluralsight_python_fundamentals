#pragma once

#include <cstdint>

struct vector_t {
  float x;
  float y;
  float z;
};

struct color_t {
  uint16_t red;
  uint16_t green;
  uint16_t blue;
};

struct vertex_t {
  vector_t position;
  color_t color;
};