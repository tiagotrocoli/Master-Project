#include "hyperbolicalgorithm.h"

int main(){

    HyperbolicAlgorithm H;

    std::vector<double> xi = {0.36,1.57,11.26, 7.12};
    std::vector<double> yi = {5.6,3.31,1.03,4.09};
    std::vector<double> d  = {8,7,9,4};

    H.estimate(xi, yi, d);
}
