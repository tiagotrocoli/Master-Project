#include "hyperbolicalgorithm.h"


void HyperbolicAlgorithm::estimate(std::vector<double> &x, std::vector<double> &y, std::vector<double> &d){

    int size = d.size();

    Matrix A = Matrix(size - 1, 2);
    Matrix B = Matrix(size - 1, 1);
    Matrix AA = Matrix(size - 1, size - 1);

    double x0 = x[0];
    double y0 = y[0];
    double r0 = d[0];
    double xi, yi, ri;

    for (int i=1; i<size ;i++) {
        xi = x[i];
        yi = y[i];
        ri = d[i];

        //set value of Matrix A
        A.setCell(i-1, 0, 2 * (xi - x0));
        A.setCell(i-1, 1, 2 * (yi - y0));

        //set value of Matrix B
        B.setCell(i-1, 0, (r0 * r0 - ri * ri) - (x0 * x0 - xi * xi) - (y0 * y0 - yi * yi));
    }

    AA = A.transpose() * A;
    if (AA.getDet() != 0){
        Matrix tarPosMat(2, 1);
        tarPosMat = AA.inverse() * A.transpose() * B;
        std::cout << tarPosMat.getCell(0, 0) << std::endl;
        std::cout << tarPosMat.getCell(1, 0) << std::endl;
    } else {
        std::cout << "NULL" << std::endl;
    }
}
