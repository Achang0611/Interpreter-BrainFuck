#include <iostream>
#include "BrainFuckParser.h"

using namespace std;

int main() {
    BrainFuckParser bf("++++++++++[>+++++++>++++++++++>+++>+<<<<-]\n"
                       ">++.>+.+++++++..+++.>++.<<+++++++++++++++.\n"
                       ">.+++.------.--------.>+.>.");
    bf.execute();
    BrainFuckParser bf2("+[+-]");
    bf2.execute();
    return 0;
}