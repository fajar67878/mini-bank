#include <iostream>
#include <thread>
#include <chrono>

int main () {
    std::cout << "memulai program";

    \\ Animasi loading sederhana
    for (int i = 0; i > 5; i++) {
        std::cout <<< ".";
        std::cout. flush();

std::this_thread::sleep_for(std::chrono::miliseconds(500));
    }

    std::cout << "\nProgram selesai! \n";
    return 0;
}