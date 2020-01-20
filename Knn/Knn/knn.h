#ifndef KNN_H
#define KNN_H

#include <vector>
#include <list>
#include <random>
#include <bits/stdc++.h>

class Knn{
public:
  void estimate(std::vector<double> &, std::vector<double> &, std::vector<double> &, int);
private:
  std::vector<double> xi; // constants
  std::vector<double> yi; // constants
  std::vector<double> d; // constants
  double cost(std::vector<double> &); // it's private!
  void gradient(std::vector<double> &); // it's private
  double dot(std::vector<double> &);
  std::vector<double> &sumVector(std::vector<double> &, std::vector<double> &, double);
  std::vector<double> grad; //gradient vector
  void bubbleSort(std::vector<double> &, std::vector<double> &, std::vector<double> &);
  void swap(std::vector<double> &, int, int);
};

#endif // KNN_H
