#include <iostream>
#include <forward_list>

using namespace std;

int main(){

    forward_list<int> fwd_list = {5,4,6,7,8,2,1,3};

    fwd_list.push_front(0);

    auto it = fwd_list.begin(); 

    fwd_list.insert_after(it, 5); // 맨처음 원소 뒤에 추가.

    fwd_list.insert_after(it, 6);

    fwd_list.pop_front(); // 맨 앞 원소 삭제.

    fwd_list.erase_after(it); // 맨 앞의 다음 원소를 삭제. 

    fwd_list.erase_after(it, fwd_list.end()); // 맨 앞 원소 다음부터 맨 마지막 원소까지 삭제.

    fwd_list.sort(); // 1,2,3,4,5,6,7,8

    fwd_list.sort(std::greater<int>()); //8,7,6,5,4,3,2,1

    fwd_list = {5,4,6,7,8,2,1,3};

    fwd_list.reverse(); // 대칭이동 3 1 2 8 7 6 4 5

    fwd_list.unique(); // 중복제거

    return 0;

}