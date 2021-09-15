//
// Created by vmtay on 2021/9/15.
//

#ifndef UNTITLED1_BRAINFUCKPARSER_H
#define UNTITLED1_BRAINFUCKPARSER_H

#include <string>

#define addySz 30000

class BrainFuckParser {
public:
    explicit BrainFuckParser(std::string);

    virtual ~BrainFuckParser();

    bool execute();

private:
    int p = 0;
    std::string codes;
    uint8_t addy[addySz]{};

    int bracketCheck();
};

#endif //UNTITLED1_BRAINFUCKPARSER_H
