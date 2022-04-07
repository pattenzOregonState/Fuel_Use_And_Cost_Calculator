#######################################################################
# Program Filename: Fuel_Use+Cost_Calculator
# Author: Zachary Patten
# Date: 4/7/2022
# Description: This is the ENGR 103 assignment from studio 2
# Input: Gas Price, Cars' Fuel Efficiency, Average Distance Oregonians Drive/Year, Electricity Cost
# Output: The gas or gas equivalent used each year by each car
#######################################################################
def gas_use_price_calc(mpg, model):
    gas_used = 14032 / mpg
    print(
        str(model) + " use(s) " + str(round(gas_used, 2)) + " gallons of gas, and it costs " +
        str(round(gas_used * 4.72, 2)) + "$ in Oregon and " + str(round(gas_used * 5.92, 2)) + "$ in California."
    )


def electric_use_price_calc(mpg, model):
    gas_used = 14032 / mpg
    print(
        str(model) + " uses the equivalent of " + str(round(gas_used, 2)) + " gallons of gas, and it costs " +
        str(round(gas_used*33.7*0.1116, 2)) + "$ if charged at home and " + str(round(gas_used*0.3*33.7, 2)) +
        "$ if charged at a charging station."
    )


gas_use_price_calc(30, "Gas Sedan and SUV Hybrid")
gas_use_price_calc(45, "Hybrid Sedan")
gas_use_price_calc(20, "Gas SUV")
electric_use_price_calc(126, "Tesla Model 3")
electric_use_price_calc(108, "Chevy Bolt")
