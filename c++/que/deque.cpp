#include <iostream>
#include <deque>

void printDeque(std::deque<int> deq){
    std::cout << std::endl;
    for(auto v : deq){
        std::cout << v << " ";
    }
    std::cout << std::endl;
}

int main(){
    std::deque<int> deq = {1, 2, 3, 4, 5};
    printDeque(deq);

    deq.push_front(0);
    printDeque(deq);

    deq.push_back(6);
    printDeque(deq);

    deq.insert(deq.begin()+2, 10);
    printDeque(deq);

    deq.pop_back();
    printDeque(deq);

    deq.pop_front();
    printDeque(deq);

    deq.erase(deq.begin()+1);
    printDeque(deq);

    deq.erase(deq.begin() + 3, deq.end());
    printDeque(deq);
}