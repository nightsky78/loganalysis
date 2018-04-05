import psycopg2
import configparser

class Db_handler:
    def __init__(self):

        # Parse the config file
        dbconfig = configparser.ConfigParser()
        configfilepath = r'./DB.config'
        dbconfig.read(configfilepath)

        self.dbname = dbconfig.get('dbconfig','db_name')
        self.user = dbconfig.get('dbconfig', 'user')
        self.password = dbconfig.get('dbconfig', 'password')
        self.host = dbconfig.get('dbconfig', 'db_url')
        self.port = dbconfig.get('dbconfig','db_port')

        # create DB connection
        self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host,
                               port=self.port)

    # Method reads the most popular articles
    def retrieve_popular_articles(self, top):
        self.top = top

        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        cur.execute("SELECT title, count(title) FROM v_list GROUP BY title ORDER BY count DESC LIMIT {0};".format(self.top))
        return cur.fetchall()

    # Method reads the most popular authors
    def retrieve_popular_authors(self, top):
        self.top = top

        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        cur.execute("select name, count(name) FROM v_list GROUP BY name ORDER BY count DESC LIMIT {0};".format(self.top))
        return cur.fetchall()

    # Method to evaluate the access stats of the website
    def retrieve_failure_days(self, margin):
        self.margin = margin

        con = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
        cur = con.cursor()

        cur.execute("select CAST(date as timestamp), CAST(count1 as float) / CAST (count as float) as error_frac FROM v_status_count \
                            where CAST(count1 as float) / CAST (count as float) >= {0} ".format(self.margin))
        return cur.fetchall()