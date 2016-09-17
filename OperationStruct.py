from collections import namedtuple
# Operation structs hold individual tuples such as (+, 2) or (/, 3)
OperationStruct = namedtuple("OperationStruct", 'operator value')