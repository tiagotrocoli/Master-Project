#ifndef CIRCULARALGORITHM_H
#define CIRCULARALGORITHM_H

#include <vector>
#include <list>
#include <random>
#include <bits/stdc++.h>

class CircularAlgorithm{
public:
  void estimate(std::vector<double> &X, std::vector<double> &Y, std::vector<double> &D);
private:
  std::vector<double> xi; // constants
  std::vector<double> yi; // constants
  std::vector<double> d; // constants
  void estimate(std::vector<double> &, std::vector<double> &);
  double cost(std::vector<double> &); // it's private!
  void gradient(std::vector<double> &); // it's private
  double dot(std::vector<double> &);
  std::vector<double> &sumVector(std::vector<double> &, std::vector<double> &, double);
  std::vector<double> grad; //gradient vector
};

#endif // CIRCULARALGORITHM_H
