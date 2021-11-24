'''
    pip install pandas
    pip install regex
'''

try:
    import os
    import pandas as pd
    import numpy as np
    import sys
    import arv.data.transformer as DB
    import arv.core.settings as APP

except ModuleNotFoundError as m_error:
    print(str(m_error))
    print('please install the required module and try again...')
    exit()


settings = APP.Settings(sys.path[0])

#comprobar que funciona correctamente el rename_dataframe_cols y el delete_dataframe_cols
#DB.transform_all(settings=settings, delete_scrap_files=False)

db = pd.read_csv(settings.products_database_filepath)

DB.dataframe_info(db, "TITULAR")


#ATENCION: no elimina el SCRAP
#HAY QUE CAMBIAR ILUMINATED BATHROOM MIRROR PARA TODOS Y DIFERENCIAR BIEN LAS CATEGORIAS




'''
#print(settings.scrapes_filepath_list)


last_date = DB.get_lastdate(database=db, date_format=settings.date_format)
last_snapshot =db[db['scrap__spider_date']==last_date.strftime(settings.date_format)]

'''