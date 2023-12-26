from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Presence(Model):
    __keyspace__ = 'presence_keyspace'
    __connection__ = 'cluster1'

    user_id = columns.Text(primary_key=True, min_length=1)
    status = columns.Text()
    last_active_at = columns.DateTime()
    created_at = columns.DateTime()
