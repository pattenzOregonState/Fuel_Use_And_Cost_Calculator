#######################################################################
# Program Filename: Fuel_Use+Cost_Calculator
# Author: Zachary Patten
# Date: 4/7/2022
# Description: This is the ENGR 103 assignment from studio 2
# Input: Gas Price, Cars' Fuel Efficiency, Average Distance Oregonians Drive/Year, Electricity Cost
# Output: The gas or gas equivalent used each year by each car
#######################################################################
def gas_use_price_calc(mpg, model, electric):
    gas_used = 14032 / mpg
    expense_1 = round(gas_used*(4.72*(not electric) + 33.7*0.1116*electric), 2)
    expense_2 = round(gas_used*(5.92*(not electric) + 33.7*0.3*electric), 2)
    if electric:
        print(
            str(model) + " uses the equivalent of " + str(round(gas_used, 2)) + " gallons of gas, and it costs $" +
            str(expense_1) + " if charged at home and $" + str(expense_2) + " if charged at a charging station."
        )
    else:
        print(
            str(model) + " use(s) " + str(round(gas_used, 2)) + " gallons of gas, and it costs $" +
            str(expense_1) + " in Oregon and $" + str(expense_2) + " in California."
        )


gas_use_price_calc(30, "Gas Sedan and SUV Hybrid", False)
gas_use_price_calc(45, "Hybrid Sedan", False)
gas_use_price_calc(20, "Gas SUV", False)
gas_use_price_calc(126, "Tesla Model 3", True)
gas_use_price_calc(108, "Chevy Bolt", True)
