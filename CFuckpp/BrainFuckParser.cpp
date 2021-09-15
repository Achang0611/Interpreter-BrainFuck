//
// Created by vmtay on 2021/9/13.
//

#include "BrainFuckParser.h"

#include <iostream>
#include <stack>

BrainFuckParser::BrainFuckParser(std::string codes) : codes(std::move(codes)) {}


BrainFuckParser::~BrainFuckParser() = default;

int BrainFuckParser::bracketCheck() {
    std::stack<int> stack;

    for (int i = 0; i < codes.length(); ++i) {
        switch (codes[i]) {
            case '[':
                stack.push(i);
                break;
            case ']':
                if (stack.empty())
                    return i;
                stack.pop();
                break;
        }
    }

    return stack.empty() ? -1 : stack.top();
}

bool BrainFuckParser::execute() {
    int wrongIndex = bracketCheck();
    if (wrongIndex != -1) {
        std::cerr << "Unbalanced brackets at " << wrongIndex << std::endl;
        return false;
    }

    int offset = 0;
    std::stack<int> label;
    bool skip = false;

    while (offset < codes.length()) {
        char command = codes[offset];
        if (skip) {
            if (command == ']') {
                skip = false;
            }

            offset++;
            continue;
        }

        switch (command) {
            case '>':
                ++p %= addySz;
                break;
            case '<':
                --p %= addySz;
                break;
            case '+':
                addy[p]++;
                break;
            case '-':
                addy[p]--;
                break;
            case '.':
                std::cout << addy[p];
                break;
            case ',':
                std::cin >> std::noskipws >> addy[p];
                fflush(stdin);
                break;
            case '[':
                if (addy[p] == 0)
                    skip = true;
                else
                    label.push(offset - 1);
                break;
            case ']':
                if (addy[p] > 0)
                    offset = label.top();
                label.pop();
                break;
            default:
                break;
        }

        offset++;
    }

    return true;
}
