#include <iostream>
#include <queue>

class Job {
    int id;
    std::string user;
    int pages;

    static int count;

public:
    Job(const std::string& u, int p) : user(u), pages(p), id(++count) {}

    friend std::ostream& operator<<(std::ostream& os, const Job& j){
        os << "id: " << j.id << ", User: " << j.user << ", Pages: " << j.pages << " ";
        return os;
    }

};

 int Job::count = 0;

template <size_t N>
class Printer{
    std::queue<Job> jobs;

public:
    bool addNewJob(const Job& job){
        if(jobs.size() == N){
            std::cout << "Failed: " << job << std::endl;
            return false;
        }
        std::cout << "Printing Added: " << job << std::endl;
        jobs.push(job);
        return true;
    }

    void startPrinting(){
        while (not jobs.empty()){
			std::cout << "Printing: " << jobs.front() << std::endl;
			jobs.pop();
		}
    }

};

int main(){

    Printer<5> printer;

    Job j1("Park", 10);
    Job j2("Kim", 7);
    Job j3("Lee", 2);
    Job j4("Sim", 1);
    Job j5("Choi", 4);
    Job j6("Heo", 9);

    printer.addNewJob(j1);
    printer.addNewJob(j2);
    printer.addNewJob(j3);
    printer.addNewJob(j4);
    printer.addNewJob(j5);
    printer.addNewJob(j6);

    printer.startPrinting();
    printer.addNewJob(j6);

}