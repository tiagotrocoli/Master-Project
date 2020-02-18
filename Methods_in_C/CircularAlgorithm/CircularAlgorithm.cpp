#include "CircularAlgorithm.h"
#include <iostream>

// tested!!!
double CircularAlgorithm::cost(std::vector<double> &var){
    size_t size = d.size();
    double result = 0;
    for(size_t i=0;i<size;i+=1){
      double res = (var[0] - xi[i])*(var[0] - xi[i]) + (var[1] - yi[i])*(var[1] - yi[i]) - d[i]*d[i];
      result = result + res*res;
    }
    return result;
}

// tested!!!
// -grad of x
void CircularAlgorithm::gradient(std::vector<double> &var){
    double res1 = 0, res2 = 0;
    int size = d.size();

    for(int i=0;i<size;i++){
      res1 += 4*(var[0] - xi[i])*((var[0] - xi[i])*(var[0] - xi[i]) + (var[1] - yi[i])*(var[1] - yi[i]) - d[i]*d[i]);
      res2 += 4*(var[1] - yi[i])*((var[0] - xi[i])*(var[0] - xi[i]) + (var[1] - yi[i])*(var[1] - yi[i]) - d[i]*d[i]);
    }

    grad[0] = res1;
    grad[1] = res2;
}

// tested
double CircularAlgorithm::dot(std::vector<double> &v){

  double result = 0;
  size_t size = v.size();

  for(size_t i=0;i<size;i++){
    result+= v[i]*v[i];
  }
  return result;
}

//tested
std::vector<double> &CircularAlgorithm::sumVector(std::vector<double> &var, std::vector<double> &p, double a){

  static std::vector<double> *v = new std::vector<double>(); // create a vector for this function to avoid creating every time it is called
  size_t size = var.size();
  v->clear();
  for(size_t i=0;i<size;i++){
    v->push_back(var[i] + a*p[i]);
  }
  return *v;
}

void CircularAlgorithm::estimate(std::vector<double> &X, std::vector<double> &Y, std::vector<double> &D){
    double c = 0.5;
    double p = 0.5;
    double tol = 0.000001;

    xi = X;
    yi = Y;
    d  = D;

    grad.push_back(0);
    grad.push_back(0);

    std::vector<double> x(2);
    srand((unsigned)time(NULL));
    x[0] = 100*((double)rand()/(double)RAND_MAX);
    x[1] = 100*((double)rand()/(double)RAND_MAX);

    // grad of x
    gradient(x);

    while(dot(grad) > tol){
        // armijo condition
        double a = 1.0;
        while(cost(sumVector(x,grad,-a)) > cost(x) - c*a*dot(grad)){
            a = p*a;
        }
        x = sumVector(x,grad,-a);
        gradient(x);
    }
    std::cout << x[0] << " " << x[1] <<std::endl;
}
