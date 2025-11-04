#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib>
#include <ctime>

int main() {
    std::srand(std::time(nullptr));
    std::cout << "=== Embedded Diagnostics System Boot ===" << std::endl;

    while (true) {
        int temp = std::rand() % 100;   
        int voltage = 3000 + std::rand() % 500; 
        bool fault = (std::rand() % 20 == 0);

        std::cout << "[DATA] TEMP=" << temp 
                  << "C | VOLT=" << voltage 
                  << "mV | STATUS=" << (fault ? "FAULT" : "OK")
                  << std::endl;

        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    return 0;
}
