#include <iostream>
#include <stack>
#include <deque>
#include <queue>

int main(){
    std::deque<int> stk1;
    stk1.push_back(1); // 1
    stk1.push_back(2); // 1, 2
    stk1.pop_back(); // 1
    stk1.push_front(0); // 0, 1

    std::stack<int> stk2;
    stk2.push(1); // 1
    stk2.push(2); // 1, 2
    stk2.pop(); // 1
    stk2.push_front(0); //  Error!

    std::queue<int> q;

    q.push(1);
    q.push(2);
    q.push(3);
    q.pop();
    q.push(4);
}