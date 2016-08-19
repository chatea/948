# -*- coding: utf-8 -*-
import json
import csv

import logging

_TEST_MENU_ID = u'-1'
_KEY_MENU_ID = u'menu_id'
_KEY_MENU_NAME = u'name'
_KEY_MENU_TITLE = u'title'
_KEY_MENU_PATH = u'path_to_file'

KEY_ITEM_ID = u'id'
KEY_ITEM_ITEMS = u'items'
KEY_ITEM_NAME = u'name'
KEY_ITEM_PRICE = u'price'
KEY_ITEM_CATEGORY = u'category'

def load_csv(filename):
    """ load a CSV file, output is a dictionary
    Args:
        filename: the full file path for read
    Return:
        A dictionary
    """
    with file(filename, 'rb') as csvfile:
        ret = {}
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        headers = reader.next()
        headers[0] = headers[0][1:].strip()
        headers = [unicode(w, 'utf-8') for w in headers]
        for row in reader:
            item_id = unicode(row[0], 'utf-8')
            items = {}
            for i in xrange(0, len(row)):
                if headers[i] == KEY_ITEM_ITEMS:
                    dumped_items = json.loads(row[i])
                    print dumped_items
                    items[headers[i]] = [str(i).decode('utf-8') for i in dumped_items]
                else:
                    items[headers[i]] = unicode(row[i], 'utf-8')
            ret[item_id] = items
        return ret

print "import menu list"
menu_map = load_csv('menulist.csv')
print "import menu list complete:"


def get_menu_list():
    global menu_map
    return menu_map


def get_menu(menu_id):
    """ get menu by menu id
    Return:
        return menu if exist, else None
    """
    global menu_map
    global _KEY_MENU_PATH
    menu_id = str(menu_id).encode('utf-8')
    if menu_id not in menu_map:
        return None

    menu_item = menu_map[menu_id]
    file_path = menu_item[_KEY_MENU_PATH]
    return load_csv(file_path)


def test():
    menu_list = get_menu_list()
    assert menu_list is not None, "Cannot find menu list!"
    print menu_list

    test_menu = get_menu(_TEST_MENU_ID)
    assert test_menu is not None, "Cannot find test menu"
    assert test_menu[u'0'][KEY_ITEM_ID] == u'0', "id is not correct for item id 0"
    assert test_menu[u'0'][KEY_ITEM_ITEMS][0] == u'0', "items are not correct for item id 0"
    assert test_menu[u'0'][KEY_ITEM_NAME] == u'海帶', "name is not correct for item id 0"
    assert test_menu[u'0'][KEY_ITEM_PRICE] == u'30', "price is not correct for item id 0"
    assert test_menu[u'0'][KEY_ITEM_CATEGORY] == u'海鮮', "cateogry is not correct for item id 0"

    assert test_menu[u'1'][KEY_ITEM_ID] == u'1', "id is not correct for item id 1"
    assert test_menu[u'1'][KEY_ITEM_ITEMS][0] == u'1', "items are not correct for item id 1"
    assert test_menu[u'1'][KEY_ITEM_NAME] == u'王子麵', "name is not correct for item id 1"
    assert test_menu[u'1'][KEY_ITEM_PRICE] == u'20', "price is not correct for item id 1"
    assert test_menu[u'1'][KEY_ITEM_CATEGORY] == u'', "cateogry is not correct for item id 1"

    print "Test pass"

if __name__ == "__main__":
    test()
