from pprint import pprint
import json
import sys
import code.keys
from code.keys import ctx as ctx_keys


# class Mapping:
#     def __init__(self, target, invocation, category, file):
#         self.target = target
#         self.invocation = invocation
#         self.category = category
#         self.file = file

items_to_write = []
filename = code.keys.__file__.removeprefix('/Users/austin/Code/talon/')
for (category, mappings) in ctx_keys.lists.items():
    category = category.removeprefix('self.')
    context = ctx_keys.matches if hasattr(ctx_keys, 'matches') else 'default'
    for (invocation, target) in mappings.items():
        items_to_write.append({'target': target, 'invocation': invocation, 'category': category, 'file': filename})

pprint(items_to_write)