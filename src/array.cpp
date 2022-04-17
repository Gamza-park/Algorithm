#include <iostream>
#include <Array>

using namespace std;

template <size_t N>

void print(array<int, N>& arr){
    for(auto ele : arr)
        cout << ele << ", ";
}

int main(){

    // array<int, 10> arr1; // 크기가 10인 int타입 배열
    // arr1[0] = 1;

    // cout << arr1[0] << endl;

    // array<int, 4> arr2 = {1,2,3,4};
    // cout << " arr2 의 원소" ;
    // for(int i=0; i<arr2.size(); i++){
    //     cout << arr2[i] << " ";
    // }
    // cout << endl;


    // array<int, 4> arr3 = {1,2,3,4};

    // try {
    //     cout << arr3.at(3) << endl;
    //     cout << arr3.at(4) << endl;
    // } catch(const out_of_range& ex){
    //     cerr << ex.what() << endl;
    // }

    

    array<int, 9> arr = {1,2,3,4,5,6,7,8,9};
    print(arr);

    /*
    범위기반 반복문은
    for (auto it = arr.begin(); it != arr.end(); it++){
        auto element = (+it)
        cout << element << " ";
    }
    */

    return 0;
}

