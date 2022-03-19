import boto3
import code.keys
from code.keys import ctx as ctx_keys

items_to_write = []
filename = code.keys.__file__.removeprefix('/Users/austin/Code/talon/')
for (category, mappings) in ctx_keys.lists.items():
    category = category.removeprefix('self.')
    context = ctx_keys.matches if hasattr(ctx_keys, 'matches') else 'default'
    for (invocation, target) in mappings.items():
        mapping = {'target': target,
                   'invocation': invocation,
                   'category': category,
                   'file': filename,
                   'context': context}
        items_to_write.append(mapping)


def load_mappings(mappings, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('mappings')
    for mapping in mappings:
        target = mapping['target']
        context = mapping['context']
        print("Adding mapping:", target, context)
        table.put_item(Item=mapping)

if __name__ == '__main__':
    load_mappings(items_to_write)