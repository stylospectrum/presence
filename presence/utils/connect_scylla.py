import os
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table, create_keyspace_simple
from cassandra.cluster import Cluster

from presence.models.presence import Presence


def connect_scylla():
    print('Connecting to Scylla DB ...')

    try:
        if os.getenv('CQLENG_ALLOW_SCHEMA_MANAGEMENT') is None:
            os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'

        conns = ['cluster1']

        cluster = Cluster(contact_points=['localhost'])
        session = cluster.connect()

        for conn in conns:
            connection.register_connection(conn, session=session)

        create_keyspace_simple('presence_keyspace',
                               connections=conns, replication_factor=1)

        sync_table(Presence, connections=conns)
        print('Successfully connected to Scylla DB')
    except Exception as e:
        print('Fail connect to Scylla DB')
        print(e)
