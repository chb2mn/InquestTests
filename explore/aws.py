import boto.sdb
from pprint import pprint

def get_data():
    pass

if __name__ == '__main__':
    print "go"
    conn = boto.sdb.connect_to_region(
            'us-east-1',
            aws_access_key_id = 'AKIAJDFJ22X4S2UZK52A',
            aws_secret_access_key = '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',
        )
    domain = conn.get_domain('sandbox')
    query = 'select * from sandbox'
    data = domain.select(query)
    all_data = []
    i = 0
    j = 0
    for item in data:
        item_dict = {}
        for key, value in item.iteritems():
            item_dict[key] = value
            j+=1
        all_data.append(item_dict)
        i+= 1
    pprint(all_data)
    print "Total Groups:",i, "Total Items:", j