#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;
using namespace std::chrono;

void benchmark_cpp_sort(int id, int size, bool sorted = false, bool reverse = false) {
    vector<double> data(size);
    if (sorted) {
        for (int i = 0; i < size; ++i) data[i] = i;
    } else if (reverse) {
        for (int i = 0; i < size; ++i) data[i] = size - i;
    } else {
        for (int i = 0; i < size; ++i) data[i] = (double)rand() / RAND_MAX;
    }

    auto start = high_resolution_clock::now();
    sort(data.begin(), data.end()); // std::sort của C++
    auto stop = high_resolution_clock::now();   
    
    auto duration = duration_cast<milliseconds>(stop - start);
    cout << "Dữ liệu " << id << " - sort (C++): ";
    cout << setprecision(2) << fixed << duration.count() << "ms" << endl;
}

int main() {
    int size = 1000000;
    benchmark_cpp_sort(1, size, true, false);
    benchmark_cpp_sort(2, size, false, true); 
    for(int i=3; i<=10; ++i) benchmark_cpp_sort(i, size); 
    return 0;
}