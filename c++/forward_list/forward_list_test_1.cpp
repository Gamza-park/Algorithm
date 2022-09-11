#include <string>
#include <iostream>
#include <forward_list>

struct citizen {
    std::string name;
    int age;
};

std::ostream &operator<<(std::ostream &os, const citizen &c){
    return (os << "[" << c.name << ", " << c.age << "]");
}

int main(){
    std::forward_list<citizen> citizens = {
        {"kim", 22}, {"lee", 25}, {"Park", 18}, {"Jin", 16}
    };

    auto citizens_copy = citizens;// 깊은복사

    std::cout << "전체 시민들: ";
    for (const auto &c : citizens)
        std:: cout << c << " ";
    std::cout << std::endl;

    citizens.remove_if([](const citizen &c){
        return (c.age < 19);

    });

    std ::cout << "투표권이 있는 시민들 : ";
    for(const auto &c : citizens)
        std::cout << c << " ";
    std::cout << std:: endl;

    std::forward_list<citizen> citizens1 = {
        {"kim", 22}, {"lee", 25}, {"Park", 18}, {"Jin", 16}
    };

    citizens1.remove_if([](const citizen &c){
        return (c.age != 18);

    });
    


    std::cout << "내년에 투표권이 생기는 시민들 : ";
    for(const auto &c : citizens1)
        std::cout << c << " ";
    std::cout << std:: endl;

    return 0;

}