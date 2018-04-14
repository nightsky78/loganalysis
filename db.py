"""Module to handle database transactions."""
import psycopg2
import configparser


class DbHandler:
    """
    The class DB_handler connects to the DB and retrieves dedicated data.

    The connection parameters to connect to the database are read from
    ./DB.config .

    Args:
        No args in the class

    Returns:
        no returns

    Raises:
        no execptions

    Functions:
        retrieve_popular_articles - argument: number of result lines
        to be returned
        retrieve_popular_authors - argument: number of result lines
        to be returned
        retrieve_failure_days - no arguments returns: query result
    """

    def __init__(self):
        """Connect to DB via conn params from conf file."""
        # Parse the config file
        dbconfig = configparser.ConfigParser()
        configfilepath = r'./DB.config'
        dbconfig.read(configfilepath)

        self.dbname = dbconfig.get('dbconfig', 'db_name')
        self.user = dbconfig.get('dbconfig', 'user')
        self.password = dbconfig.get('dbconfig', 'password')
        self.host = dbconfig.get('dbconfig', 'db_url')
        self.port = dbconfig.get('dbconfig', 'db_port')

        # create DB connection
        self.conn = psycopg2.connect(dbname=self.dbname,
                                     user=self.user,
                                     password=self.password,
                                     host=self.host,
                                     port=self.port)

    # Method reads the most popular articles
    def retrieve_popular_articles(self, top):
        """
        Retrieve popular article.

        :param top: Number of lines to be returned.
        :return: Lines with query result.
        """
        self.top = top

        con = psycopg2.connect(dbname=self.dbname,
                               user=self.user,
                               password=self.password,
                               host=self.host,
                               port=self.port)
        cur = con.cursor()

        cur.execute("SELECT title, count(title) FROM v_list GROUP BY "
                    "title ORDER BY count DESC LIMIT {0};".format(self.top))
        return cur.fetchall()

    # Method reads the most popular authors
    def retrieve_popular_authors(self, top):
        """
        Retrieve popular authors.

        :param top: Number of lines to be returned.
        :return: Lines with query result.
        """
        self.top = top

        con = psycopg2.connect(dbname=self.dbname,
                               user=self.user,
                               password=self.password,
                               host=self.host,
                               port=self.port)
        cur = con.cursor()

        cur.execute("select name, count(name) FROM v_list GROUP BY "
                    "name ORDER BY count DESC LIMIT {0};".format(self.top))
        return cur.fetchall()

    # Method to evaluate the access stats of the website
    def retrieve_failure_days(self, margin):
        """
        Retrieve failure days with margin.

        :param margin: Error margin used in the query.
        :return: Query result.
        """
        self.margin = margin

        con = psycopg2.connect(dbname=self.dbname,
                               user=self.user,
                               password=self.password,
                               host=self.host,
                               port=self.port)
        cur = con.cursor()

        cur.execute("select CAST(date as timestamp), "
                    "CAST(count as float) / CAST (count1 as float) "
                    "as error_frac FROM v_status_count \
                            where CAST(count as float) / CAST "
                    "(count1 as float) >= {0} ".format(self.margin))
        return cur.fetchall()
