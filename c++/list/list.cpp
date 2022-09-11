#include <iostream>
#include <list>
#include <vector>

void printList(std::list<int> list){
    for(auto v : list){
        std::cout << v << " ";
    }

    std::cout << std::endl;
}
void printVec(std::vector<int> list){
    for(auto v : list){
        std::cout << v << " ";
    }

    std::cout << std::endl;
}

int main(){
    // std::list<int> list1 = {1, 2, 3, 4, 5};
    // printList(list1);
    // list1.push_back(6);
    // std::cout << "Push_back" << std::endl;
    // printList(list1);
    // list1.insert(next(list1.begin()), 0);
    // std::cout << "insert1" << std::endl;
    // printList(list1);
    // list1.insert(list1.end(), 7);
    // std::cout << "insert2" << std::endl;
    // printList(list1);

    // list1.pop_back();
    // std::cout << "Pop_back" << std::endl;
    // printList(list1);

    std::vector<int> vec = {1, 2, 3, 4, 5};
    auto v_it4 = vec.begin()+4;
    vec.insert(vec.begin() + 2 , 0);
    printVec(vec);

    std::list<int> lst = {1, 2, 3, 4, 5};
    auto l_it4 = next(lst.begin(), 4);
    lst.insert(next(lst.begin(),2), 0);
    printList(lst);
}