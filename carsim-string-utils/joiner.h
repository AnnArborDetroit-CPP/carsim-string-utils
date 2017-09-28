#pragma once
#include <string>
#include <sstream>
#include <initializer_list>

namespace joiner
{
  template <typename T>
  std::string join(const T& v, const std::string& delim) {
    std::ostringstream s;
    for (const auto& i : v) {
      if (&i != &*v.begin()) {
        s << delim;
      }
      s << i;
    }
    return s.str();
  }

  std::string join(std::initializer_list<std::string> v, const std::string& delim);
}
