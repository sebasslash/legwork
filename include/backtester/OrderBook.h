#include <string>
#include <vector>
#include "../portfolio/Portfolio.h"

#ifndef ORDERBOOK_H
#define ORDERBOOK_H

class OrderBook {
    public:
        class Order {
            private:
                std::string ticker;
                size_t share_count;
                double share_price;
                std::string order_type;
                Portfolio *p;
            public:
                Order(std::string ticker_in, double share_price_in, 
                      std::string order_type_in, size_t share_count_in=100)
                    : ticker(ticker_in), share_price(share_price_in), 
                      share_count(share_count_in), order_type(order_type) {}
                std::string get_ticker() { return this->ticker; } 
                std::string get_order_type() { return this->order_type; } 
                size_t get_share_count() { return this->share_count; }
                double get_share_price() { return this->share_price; }
        };
};

#endif