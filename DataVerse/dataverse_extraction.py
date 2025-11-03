import pyodbc
import pandas as pd
import time
from sqlalchemy import create_engine
import urllib
import openpyxl

server = 'azwe-des-dev-01-sql.database.windows.net'
database = 'dynamics-reports-dev-01-db'
username = 'tudor.muntean@endava.com'
driver = '{ODBC Driver 17 for SQL Server}' # check your correct driver.
authentication = 'ActiveDirectoryInteractive' # works on windows not on linux/macos


conn_str = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'Authentication={authentication};'
)
connection_url = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(conn_str)}"
engine = create_engine(connection_url, pool_pre_ping=True)

def getActivePersons(sql_engine,country_id='106DAFC0-F283-E611-80CE-005056A82C24'):
    """
    retrieves active persons from SQL Server DB and stores them in a data frame
    """
    query = f"""
    SELECT
        P.endv_fullname AS full_name,
        BU.[name] AS current_bu,
        G.endv_name AS grade,
        D.endv_name AS discipline,
        S.endv_name AS core_skill
    FROM [dbo].[endv_person] AS P
    INNER JOIN [dbo].[businessunit] AS BU ON BU.Id = P.endv_currentbu
    INNER JOIN [staging].[endv_grade] AS G ON G.endv_gradeid = P.endv_grade
    INNER JOIN [staging].[endv_discipline] AS D ON D.endv_disciplineid = P.endv_discipline
    INNER JOIN [staging].[endv_skill] AS S ON S.endv_skillid = P.endv_coreskill
    WHERE P.endv_country = '{country_id}';
    """
    print("Executing query to retrieve active persons...")
    return pd.read_sql(query, sql_engine)
    
# log time taken to execute the function in miliseconds
start_time = time.time()
df = getActivePersons(engine)
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"Time taken to execute the function: {execution_time} ms")
df.to_excel("endava_people_romania.xlsx", index=False)



