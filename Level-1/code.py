'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  ///
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import Decimal
import math

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = Decimal.from_float(0)

    for item in order.items:

        if item.type == 'payment':
            net += Decimal.from_float(item.amount)
            #print("SOMA NET: " + str(net))
        elif item.type == 'product':
            net -= Decimal.from_float(item.amount) * Decimal.from_float(item.quantity)
            #print("SUBTRAI NET: " + str(net) + "e " + str(item.amount))
        else:
            return("Invalid item type: %s" % item.type)

    #if net != 0:
    #print("NET: FIM " + str(net))
    if math.isclose(net,0, abs_tol=1e-9)==False:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
