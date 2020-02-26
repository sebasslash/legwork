#include "../include/backtester/Backtester.h"
#include "../include/portfolio/Portfolio.h"
#include<iostream>
#include<string>

int main(char *argv[], int argc){
    // Initiate the Backtester
    const Backtester *bt = new Backtester(0);
    // Load the algorithm with Boost Python
    // Run the Backtester
    // Present Results Back as a JSON object
    return 0;
}