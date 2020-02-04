#include "hyperbolicalgorithm.h"
#include <string>
#include <string.h>

void print(std::vector<double> &vec){
    for(int i=0;i<vec.size();i++){
        std::cout <<vec[i] << std::endl;
    }
    std::cout <<std::endl;
}

int main(int argc, char *argv[]){

    HyperbolicAlgorithm H;

    std::vector<double> xi = {4.4, 2.2, 0, 6.6, 0, 6.6};
    std::vector<double> yi = {2.6,13.0,6.5, 10.4, 3.9, 7.8};
    std::vector<double> d  = std::vector<double>(6);

    if(strcmp(argv[1],"1") == 0){
        std::vector<double>::iterator it1 = xi.begin();
        std::vector<double>::iterator it2 = yi.begin();
        int j = 0;
        for(int i=0;i<6;i++){
            if(strcmp(argv[i+2],"0") != 0){
                d[j] = std::stof(argv[i+2]);
                it1++;
                it2++;
                j++;
            }
            else{
                xi.erase(it1);
                yi.erase(it2);
            }
        }
        d.resize(j);
    }
    H.estimate(xi, yi, d);
}
