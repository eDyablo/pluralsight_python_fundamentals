#include <fstream>

#include "colorpoints.hpp"

using std::ios;
using std::ofstream;
using std::size;

int main() {
  vertex_t vertices[] = {{.position = {3323.176, 6562.231, 9351.231},
                          .color = {3040, 34423, 54321}},
                         {.position = {7623.982, 2542.231, 9823.121},
                          .color = {32736, 5342, 2321}},
                         {.position = {6729.862, 2347.212, 3421.322},
                          .color = {45263, 36291, 36701}},
                         {.position = {6352.121, 3432.111, 9763.232},
                          .color = {56222, 36612, 11214}}};

  ofstream file("/data/colorpoints.bin", ios::out | ios::binary);
  file.write(reinterpret_cast<char *>(&vertices[0]),
             size(vertices) * sizeof(vertex_t));
  return 0;
}
