from modules.milanuncios import Milanuncios


ret = Milanuncios().query(
                            zona='madrid',
                            desde=150,
                            hasta=400,
                            query='portátil',
                            max_pag=3,
                            filtros=[
                                {
                                    'con'   :   [
                                                    ['8\s?gb', 'i7'],
                                                    ['8\s?gb', 'msi', 'ddr5'],
                                                    ['1050','gtx'], # nvidia
                                                    ['1070','gtx'],
                                                    ['1080','gtx'],
                                                    ['560','rx'], # radeon
                                                    ['550','rx'],
                                                    ['470','rx'],
                                                    ['1030','gt'],
                                                    ['730','gt'],
                                                    ['msi'],
                                                    ['urge', 'desperfecto']

                                                ],
                                    'sin'   :   [
                                                    'intel graphics',
                                                    '4\s?gb',
                                                    'roto',
                                                    'pantalla rota'
                                                ]
                                }

                            ]
                         )
