#include <iostream>
#include <thread>
#include <chrono>

int main(){
    std::cout << "Memulai Program";
    
    //Animasi loading sederhana
    for (int i = 0; i < 5; i++) {
        std::cout << ".";
        std::cout.flush();

std::this_thread::sleep_for(std::chrono::milisecond(500));
    }

        std::cout << "\program selesai!\n"
    return 0;
}