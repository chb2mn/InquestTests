import boto.sdb
from pprint import pprint
import ConfigParser

if __name__ == '__main__':
    config = ConfigParser.RawConfigParser()
    config.read('aws.cfg')
    print "connecting, please wait"
    conn = boto.sdb.connect_to_region(
            config.get('aws_configs', 'region'),
            aws_access_key_id = config.get('aws_configs', 'aws_access_key_id'),
            aws_secret_access_key = config.get('aws_configs', 'aws_secret_access_key'),
        )
    domain = conn.get_domain('sandbox')
    #NOTE: For big data running select * is stupid, but we don't have a lot so this is ok
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
    #Print all of the data out

    pprint(all_data)
    print "Total Groups:",i, "Total Items:", j
