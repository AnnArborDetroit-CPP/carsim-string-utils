#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <initializer_list>
#include "joiner.h"

namespace joiner
{
  std::string join(std::initializer_list<std::string> v, const std::string& delim)
  {
    return join<std::initializer_list<std::string>>(v, delim);
  }
}