from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cluster = Cluster()
session = cluster.connect()
session.execute("""CREATE KEYSPACE IF NOT EXISTS Test WITH REPLICATION = {'class' : 'SimpleStrategy' , 'replication_factor' : 1 };""")

session.set_keyspace('Test')
