# Setup

```shell
$ pip install flask
$ pip install flask-cli
```

# Run

```shell
$ cd path/to/project/root
$ FLASK_APP=./main.py flask run
```

Run in debug mode
```shell
$ cd path/to/project/root
$ FLASK_APP=./main.py FLASK_DEBUG=1 flask run
```

# APIs

* get all menus: `$HOST/menus`
* get all item in specify menu: `$HOST/menus/<menu_name>`  # e.g. `$HOST/menus/mcdonalds`
* get best prices: `$HOST/getPrices` with argument:
    * menu_id: the id of menu, e.g. mcdonalds is 1.
    * orders: a id list of ordered items.

## Simple test
Run server first, then try below APIs:
* `$HOST/menus`
* `$HOST/menus/mcdonalds`
* `$HOST/getPrices?menu_id=-1&orders=[0,0,1]`

