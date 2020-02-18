#include "CircularAlgorithm.h"

int main(void){
	// don't forget,process time also!!!!
    CircularAlgorithm C;

    std::vector<double> xi = {0.36,1.57,11.26, 7.12};
    std::vector<double> yi = {5.6,3.31,1.03,4.09};
    std::vector<double> d  = {8,7,9,4};

    C.estimate(xi, yi, d);
}
