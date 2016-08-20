import menu

class OrderMethod(object):
    def __init__(self, orders, prices):
        self.orders = orders
        self.prices = prices

    def __str__(self):
        ret = "prices: %d, buy methods is %s" % (self.prices, str(self.orders))
        return ret

def is_same_list(left, right):
    hashed = {}
    for i in left:
        if i in hashed:
            hashed[i] += 1
        else:
            hashed[i] = 1
    for i in right:
        if i not in hashed:
            return False
        else:
            hashed[i] -= 1
            if hashed[i] == 0:
                del hashed[i]
    return False if hashed else True

class _Calculator(object):

    def __init__(self, menu):
        self.menu = menu
        self.cached = {}

    def perform_calculate(self, remains, ordered, ordered_prices):
        if not remains:
            return OrderMethod(ordered, ordered_prices)

        if ordered_prices in self.cached:
            for r, m in self.cached[ordered_prices]:
                if is_same_list(remains, r):
                    return m

        min_method = None
        for k, item in self.menu.iteritems():
            all_in = True
            next_remains = remains[:]
            next_ordered = ordered[:]
            for i in item[menu.KEY_ITEM_ITEMS]:
                if i in next_remains:
                    next_remains.remove(i)
                else:
                    all_in = False
                    break
            next_ordered.append(item[menu.KEY_ITEM_ID])
            if all_in:
                next_prices = ordered_prices + int(item[menu.KEY_ITEM_PRICE])
                new_order_method = self.perform_calculate(next_remains, next_ordered, next_prices)
                if not new_order_method: continue
                if not min_method or new_order_method.prices < min_method.prices:
                    min_method = new_order_method

        if ordered_prices not in self.cached:
            self.cached[ordered_prices] = [(remains[:],min_method)]
        else:
            self.cached[ordered_prices].append((remains[:],min_method))
        return min_method


def calculate(menu_id, orders):
    full_menu = menu.get_menu(menu_id)
    # flatten orders first
    flatten_orders = []
    while orders:
        order = orders.pop(0)
        row = full_menu[order]
        items = row[menu.KEY_ITEM_ITEMS]
        if len(items) == 1 and items[0] == row[menu.KEY_ITEM_ID]:
            flatten_orders.append(items[0])
        else:
            orders.extend(items)
    calculator = _Calculator(full_menu)
    return calculator.perform_calculate(flatten_orders, [], 0)


def test():
    result = calculate(u'-1', [u'0',u'1'])
    assert result.orders == [u'2'], "The orders of calculate is wrong:" + str(result.orders)
    assert result.prices == 40, "The price is wrong"
    print "Buy succeed: ", result

    result = calculate(u'-1', [u'0',u'2'])
    assert result.orders == [u'0', u'2'], "The order of calculate is wrong: " + str(result.orders)
    assert result.prices == 70, "The price is wrong"
    print "Buy succeed: ", result

    result = calculate(u'-1', [u'0',u'1',u'12',u'7',u'5',u'5',u'8'])
    assert result.orders == [u'13'], "The order of calculate is wrong: " + str(result.orders)
    assert result.prices == 100, "The price is wrong"
    print "Buy succeed: ", result

    print "test pass"

    result = calculate(u'0', [u'11',u'11',u'11',u'11',u'13',u'30',u'30',u'30',u'30',u'76',u'76',u'76',u'76'])
    print result

if __name__ == "__main__":
    test()
