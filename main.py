# -*- encoding: utf-8 -*-
from modules.milanuncios import Milanuncios


ret = Milanuncios().query(
                            zona='madrid',
                            desde=150,
                            hasta=400,
                            query='portatil',
                            max_pag=99999, # no limitamos por pagina
                            max_minutes=60*24*2.5, # limitamos por antiguedad: dos dias y medio
                            max_ads=1000, # no limitamos por numero de anuncios
                            filtros=[
                                {
                                    'con'   :   [
                                                    ['(?:12|16)\s*(?:gb|giga)', 'i[78]'], # con mucha ram
                                                    ['(?:12|16)\s*(?:gb|giga)', 'msi', 'ddr5'],
                                                    ['i[678][\-\s][678][0-9]{3}'], # buen procesador
                                                    ['1[0-9]{3}\s*gtx'], # nvidia
                                                    ['9[0-9]{2}\s*gtx'],
                                                    ['1[0-9]{3}\s*(?:gt|rx)'], # radeon
                                                    ['9[0-9]{2}\s*(?:gt|rx)'], 
                                                    ['msi'], # buena marca
                                                    ['urge'] # cosas rebajadas

                                                ],
                                    'sin'   :   [
                                                    #'intel graphics',
                                                    '4\s*(?:gb|giga)',
                                                    'rot[oa]',
                                                    'torre'
                                                ]
                                }

                            ]
                         )
