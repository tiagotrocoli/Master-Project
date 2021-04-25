# 1. Introduction

In this work, we present a comparative study of RSS-based localization techniques implemented in commodity hardware. 
We compare nine localization methods in a real-world office environment with strong radio signal interference and in rooms of 
a house with weak interference. In addition to accuracy, we present energy consumption and response time for each method. 
Results show that Fingerprinting methods had overall better results than multilateration ones. But the accuracy of the second 
can be increased using a more complex model with the cost of more energy consumption, but not necessarily increasing the response time. 
The study also shows that well-placed anchor nodes can improve the methods' accuracy without the need for any additional modification. 
Besides, the selection of subsets of anchor nodes could provide substantially better accuracy than using all of them. 
And a good subset could be made up of best-placed anchor nodes with average ones.

<p align="center">
<img src="/images/objective.PNG" height="80%" width="80%">  
</p>

# 2. Problem

Indoor localization consists of estimating a position of people and devices in indoor environments, such as tunnels, airports, 
shopping malls, warehouses and smart factories. Indoor localization for mobile devices and people is a difficult problem that GPS and other 
global localization technologies are highly inaccuracy. A workaround consists of deploying anchor nodes 
that emit signals to mobile devices. Mobile devices can use received signal strengths (RSS) from such nodes along with numerical 
methods to estimate their position.

<p align="center">
<img src="/images/problem.PNG" height="100%" width="100%">  
</p>

# 3. What is RSS?
It is the received signal strength emitted from an anchor node to a mobile node. With RSS data, it is possible to estimate the distance between
an anchor and mobile node. This project used Wi-Fi signals.

<p align="center">
<img src="/images/signals.PNG" height="60%" width="60%">  
</p>

# 4. Anchor node calibration

It is a process in which it is possible to estimate the distance of any position of the indoor enviorement from a especific anchor node.
The process envolves finding a distance estimator (function) based on data of known position and distance. The known data pair (position, distance)
is called training points. We can use any regression function, but in this project we used two: polynomial and lognormal function. The image below shows
two estimation models.

<p align="center">
<img src="/images/twoModels.PNG" height="70%" width="70%">  
</p>

Given the model below:

<p align="center">
<img src="/images/model.png" height="20%" width="20%">  
</p>

in which g(<b>a</b><sub>i</sub>, rss<sub>ij</sub>) is a model of <i>k</i> parameters, rss<sub>ij</sub> and d&#770<sub>ij</sub> are the RSS and the 
estimated distance of anchor node <i>i</i> to the training point <i>j</i>, respectively. Calibration of anchor node <i>i</i> estimates the best parameters <b>a</b><sub>i</sub> 
given all RSS (rss<sub>i1</sub>, rss<sub>i2</sub>, ..., rss<sub>im</sub>) of training points to minimize differences between the actual and estimated distances from anchor node <i>i</i> 
to all these points. To do that, least squares was applied:  

<p align="center">
<img src="/images/LeastSquare.PNG" height="40%" width="40%">  
</p>

in which d<sub>ij</sub> is the real distance from anchor node <i>i</i> to training point <i>j</i>. Since there were 6 anchor nodes, 6 calibrations were done 
using polynomial and 6 for lognormal shadowing path-loss model. Also, rss<sub>ij</sub> is the mean value of N samples of RSS from anchor node <i>i</i> to 
training point <i>j</i>, that is:

<p align="center">
<img src="/images/mean.PNG" height="30%" width="30%">  
</p>

# 5. Indoor Enviorements

The first experiment was in a lab of University of Campinas (Unicamp) with anchor nodes that emitted Wi-Fi signals. Empty crossed circles represent training points, 
filled ones are test points, rounded squares are tables and writing desks with office chairs. The image does not show computers and other furniture.

<p align="center">
<img src="/images/MapOfExperiment.png" height="60%" width="60%">  
</p>

The second experiment took place two fully furnished rooms where. The crossed circles with a number are test points, the others are training points. 
The image does not show furniture.

<p align="center">
<img src="/images/experiment_2.png" height="60%" width="60%">  
</p>

# 6. Multilateration

Multilateration estimates a mobile node position based on distances from it to anchor nodes. To estimate the distance, the method needs the position of anchor nodes 
and distance estimator for each anchor node which is described in the section "Anchor node calibration". The method that deploys exactly three anchor nodes is called 
lateration.  Multilateration is a generalization of it which uses more than three of them. The image below depicts the method.

<p align="center">
<img src="/images/lateration.PNG" height="60%" width="60%">  
</p>

The method has 6 variations depending on how it estimates the position and the calibration of anchor nodes. It can use linear least squares (LLS), non-linear least squares (NLS) or weighted 
non-linear least squares (weighted NLS). The 3 algorithms below relate to these variations.

<p align="center">
<img src="/images/LLS.PNG" height="60%" width="60%">  
</p>


<p align="center">
<img src="/images/NLS.PNG" height="60%" width="60%">  
</p>


<p align="center">
<img src="/images/weighted.PNG" height="60%" width="60%">  
</p>

# 7. Fingerprinting
