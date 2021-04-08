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
<img src="/images/problem.PNG" height="80%" width="80%">  
</p>

# 3. What is RSS?
It is the received signal strength emitted from an anchor node to a mobile node. With RSS data, it is possible to estimate the distance between
an anchor and mobile node. This project used Wi-Fi signals.

<p align="center">
<img src="/images/signals.PNG" height="60%" width="60%">  
</p>

# 4. Anchor node calibration

It is a process in which it is possible to estimate the distance of a especific anchor node reguarding any position of the indoor enviorement.
The process envolves finding a distance estimator (function) based on data of known position and distance. The known data pair (position, distance)
is called training points. We can use any regression function, but in this project we used two: polynomial and lognormal function. 

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

<p align="center">
<img src="/images/multilateration.PNG" height="60%" width="60%">  
</p>

# 7. Fingerprinting
