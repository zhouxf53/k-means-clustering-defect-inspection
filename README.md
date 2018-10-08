# k-means-clustering-defect-inspection

## Original paper: 
(1) https://www.sciencedirect.com/science/article/pii/S0963869515000961 
(2) https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9861/98610S/Thermography-and-k-means-clustering-methods-for-anti-reflective-coating/10.1117/12.2222313.full?SSO=1
## Introduction
### Objective
This work applies thermography (Thermal infrared imaging) on different kinds of materials to identify defects inside of them. The objective is to segment the defect area from the non-defect area automatically without human intervention—a machine vision approach.
### Theoretical background
The algorithm assumes that the defect area would have different thermophysical properties (heat capacity and thermal conductivity) than the non-defect area, thus their surface temperature response became different under thermal excitation. The algorithm identified such difference and segmented areas with a distinctive thermal contrast. 
## Algorithm description
Algorithm is designed as follows:
![Fig 1-1 Algorithm flow](https://github.com/zhouxf53/k-means-clustering-defect-inspection/blob/master/1.png)
(1) A de-trend filter was applied to remove background noise due to uneven heating and camera itself. 
(2) Edge detection algorithm was applied to highlight the boundary with sharp gradient.
(3) Clustering method was applied to segment the defect cluster from the remaining noise
And an example of the algorithm flow can be illustrated as:
![Fig 1-2 Algorithm visualization](https://github.com/zhouxf53/k-means-clustering-defect-inspection/blob/master/2.png)
