#include "knn.h"
#include <vector>

int main(void){

    Knn k;

    std::vector<double> xi = {0.36,1.57,11.26, 7.12};
    std::vector<double> yi = {5.6,3.31,1.03,4.09};
    std::vector<double> d  = {8,7,9,4};

    k.estimate(xi, yi, d, 4);

    return 0;
}
