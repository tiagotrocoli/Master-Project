# 1. Introduction

Indoor localization is an important and wide-ranging IoT application. In low-cost devices, methods relying on the Received Signal Strength (RSS) to estimate distances and positions of nodes are widely used since they require no additional hardware and provide reasonable accuracy. While many methods for RSS-based indoor localization have been developed, comparative studies for such methods have typically focused primarily on the accuracy, ignoring important metrics such as response time and energy consumption. In energy-restricted devices, in particular, localization accuracy cannot come at the expense of reducing battery lifetime, and so maximizing accuracy in isolation may not be desirable. 

In this work, we present a comparative study of RSS-based localization techniques implemented in commodity hardware. We compare nine localization methods in a real-world office environment with strong radio signal interference and in rooms of a house with weak interference. In addition to accuracy, we present energy consumption and response time for each method. Results show that Fingerprinting methods had overall better results than multilateration ones. But the accuracy of the second can be increased using a more complex model with the cost of more energy consumption, but not necessarily increasing the response time. The study also shows that well-placed anchor nodes can improve the methods' accuracy without the need for any additional modification. Besides, the selection of subsets of anchor nodes could provide substantially better accuracy than using all of them. And a good subset could be made up of best-placed anchor nodes with average ones.

<p align="center">
<img src="/images/objective.PNG" height="80%" width="80%">  
</p>


# 2. Multilateration
