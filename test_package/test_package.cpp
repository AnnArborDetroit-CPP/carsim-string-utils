#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include "joiner.h"

int main() {
    std::string joined = joiner::join(std::vector<int>({ 1, 2, 3, 4, 5 }), ",");
    std::cout << joined << std::endl;
}
