#include <iostream>
#include "Adder/adder.h"
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>

using namespace cv; 


int main(){

    std::cout << "Sup World" << std::endl;
    std::cout << add(10, 3.5f) << std::endl;
    std::cout << add(18, 0.56f) << std::endl;
    std::cout << (double)minus(10, 5) << std::endl; 

    cv::Mat matrix(100, 100, CV_16UC1); 
    
    for (size_t i = 0; i < 100; ++i){
        for (size_t j = 0; j < 100; ++j){
            matrix.at<unsigned char>(i, j) = 128; 
        }
    }

    cv::namedWindow("Local Window"); 
    cv::imshow("Local Window", matrix); 
    cv::waitKey(0); 
    

    

}
