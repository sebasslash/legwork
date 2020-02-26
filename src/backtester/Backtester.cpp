#include "../../include/backtester/Backtester.h"



Backtester::Backtester(const int start_time, const int end_time=-1) {
    this->BOOK = new OrderBook();
    this->PORTFOLIO = new Portfolio();
    this->START_TIME = start_time;
    this->END_TIME = end_time;
}