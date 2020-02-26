#include "../portfolio/Portfolio.h"
#include "OrderBook.h"

#ifndef BACKTESTER_H
#define BACKTESTER_H

class Backtester {
    private:
        const Portfolio *PORTFOLIO;
        const OrderBook *BOOK;
        int START_TIME;
        int END_TIME;
    public:
        Backtester(const int start_time, const int end_time = -1);
};

#endif
