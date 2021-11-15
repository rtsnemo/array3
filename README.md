#Array3

Array 3 is a Python list/array program that uses 5 self-written modules.

## Program running
```bash
sh array.sh
```

## Using modules
```python
from TK_1 import input_data_from_console
from TK_2 import get_min_max_from_list
from TK_3 import get_divided_list
from TK_4 import get_multiplied_list
TK_5 = importlib.import_module('TK_5')

list_data = input_data_from input_data_from_console(3)
list1 = get_min_max_from_list(list_data)
list2 = get_divided_list(list_data)
print(get_multiplied_list(list_data))
list4 = TK_5.get_squared_list(list_data)
```