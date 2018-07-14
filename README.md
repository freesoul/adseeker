# adseeker

This software aims to web-scrap several websites (currently only www.milanuncios.es) to find interesting and recent advertisements, and collects the contact information.

The intention is that we automatically send a Whatsap saying that we are interested, so we can catch the most recent opportunities.


## Example

### Code

```
from modules.milanuncios import Milanuncios


ret = Milanuncios().query(
                            zone='madrid',
                            price_min=150,
                            price_max=400,
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
```

### Output

```
Pagina 1
Detected 30 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('rot[oa]' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
Found 0 interesting ads on current page
Pagina 2
Detected 30 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Found 0 interesting ads on current page
Pagina 3
Detected 27 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['(?:12|16)\\s*(?:gb|giga)', 'i[78]']
{'name': 'ORDENADOR PORTATIL HP ENVY 15 NOTEBOOK', 'link': 'https://www.milanuncios.com/portatiles-de-segunda-mano/ordenador-portatil-hp-envy-15-notebook-272345689.htm', 'time': 180, 'id': 'r272345689', 'precio': 300, 'coin': '€', 'abstract': ' Intel(R) Core(TM) i7-4702MQ CPU 2. 20GHz\nMemoria Local:  1TB\nRAM:  16GB\nSistema operativo de 64 bits\nPerfectas condiciones\n2014'}
Skipping item ('rot[oa]' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Found 1 interesting ads on current page
Pagina 4
Detected 28 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('rot[oa]' found)
Skipping item ('rot[oa]' found)
Found 0 interesting ads on current page
Pagina 5
Detected 26 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
{'name': 'PORTÁTIL I5,  16 GB. RAM, DVD-RW. A PRUEBA', 'link': 'https://www.milanuncios.com/portatiles-de-segunda-mano/portatil-i5-16-gb-ram-dvd-rw-a-prueba-274110751.htm', 'time': 840, 'id': 'r274110751', 'precio': 289, 'coin': '€', 'abstract': ' Doy por escrito 3 meses de garantía. \n\ntengo más ordenadores y otras cosas,  pídeme el listado por whatsapp. \n\ncontactar solo por tlf.  o whatsapp.  al 675415873. \n\ntened en cuenta que algunos ordenadores tienen averías ocultas que quizá en el momento de la compra,  en frío,  no salga pero,  después de unas horas o días de uso,  la avería sale,  en estos 3 meses comprobarás que el mío no tiene ningún problema.  \n\nacepto como parte de pago,  tu ordenador. \n\npodéis venir a probarlo en madrido,  envío urgente,  pagándolo contra-reembolso a toda españa,  por 15 euros. \n\ntiene instalado windows 10 de 64 bits,  os puedo instalar otro windows sin coste,  paquete de office y los programas necesarios para trabajar y navegar por internet.  es ideal para hacer trabajos de ofimática,  imprimir fotos y documentos,  jugar,  etc. \n\nordenador portátil fujitsu lifebook,  modelo s752.  con bluetooth y displayport,  puerto similar a hdmi.  \n\nes un ordenador muy rápido,  podéis venir a comprobarlo. \nla batería dura unas 4 horas.  \npantalla led de 14 pulgadas panorámica. \nprocesador intel i5 de 4 núcleos a 2600 mhz. \n500 gb.  de disco duro de alta velocidad,  va a 7200 r. p. m. \n16 gb.  de memoria ram,  \n3 puertos usb,  uno es de alta velocidad. \npuerto esata de alta velocidad. \nconector vga para monitor externo. \ndisplayport para monitor o tv.  en alta definición. \ntarjetas wifi y red a 1000 mbps.  soporta fibra óptica. \nlector grabador de cds.  y dvds. \nlector de tarjetas de memoria. \nlector de tarjetas inteligentes. \nadaptador de corriente. \n\ncuesta 289 euros.  ... Leer más', 'nombre': '\nAlfredo (Particular)\n', 'telefonos': ['913032129']}
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
Found 1 interesting ads on current page
Pagina 6
Detected 25 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Found 0 interesting ads on current page
Pagina 7
Detected 30 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Found 0 interesting ads on current page
Pagina 8
Detected 23 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['(?:12|16)\\s*(?:gb|giga)', 'i[78]']
{'name': 'LENOVO W530', 'link': 'https://www.milanuncios.com/ordenadores-de-segunda-mano/lenovo-w530-271625837.htm', 'time': 1320, 'id': 'r271625837', 'precio': 360, 'coin': '€', 'abstract': ' Ordenador portatil Lenovo W530,  pantalla:  15. 6 pulgadas,  procesador:  Intel core i7-3610QM CPU@ 2. 30GHz,  16Gb RAM,  500GB HDD,  dvd-rw,  windows 10 original,  tarjeta grafica NVIDIA Quadro K1000M,   estado:  usado,  funciona perfectamente memòria ampliable a 32GB.  Cualquier duda o pregunta por telefono o whatsapp no atendemos Emails. ', 'nombre': '\nJose (Particular)\n', 'telefonos': ['663578888']}
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Found 1 interesting ads on current page
Pagina 9
Detected 29 ads (in total at current page)
Item OK, list: ['(?:12|16)\\s*(?:gb|giga)', 'i[78]']
{'name': 'PORTATIL LENOVO W530 I7 3, 1 16R SSD 15P', 'link': 'https://www.milanuncios.com/portatiles-de-segunda-mano/portatil-lenovo-w530-i7-3-1-16r-ssd-15p-270729354.htm', 'time': 1440, 'id': 'r270729354', 'precio': 360, 'coin': '€', 'abstract': ' Workstation portatil lenovo thinkpad w530.  Totalmente impecable,  muy cuidado,  poco uso,  estado 9/10. Procesador i7 3612QM 4 nucleos alta gama(mas rapido que muchos 6a gen. ), 16gb en 2 modulos ampliables directamente a 32gb,  SSD 128Gb Ultrarapido + Hd 500gb Hitachi ambos Sata 6. 0 7200rpm. grafica nvidia quadro k1000m 2gb. pantalla 15, 6p fullhd 1920x1080. bateria nueva y cargador original,  dura mas de 2h. Unidad nacional teclado español  con ñ. Ideal para profesional,diseño, usuario avanzado o gaming(Mueve Fortnite en alta) . Webcam,  lector de huella, Msata (para un tercer disco), caddy con segundo HDD montado en hueco del DVD, 2x usb 3. 0, mini display port, vga, express card. windows 10 ultima edicion recien instalado. no cambio ni negocio. no marear. A recoger en zone oporto. no me desplazo. Puedo enviar(consulta  condiciones) contactar directamente al 722565313 por whatsapp preferentemente. gracias. mas portatiles en mi perfil.  ... Leer más', 'nombre': '\nWorkstation Portatil (Particular)\n', 'telefonos': ['722565313']}
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
{'name': 'PORTÁTIL I5,  16 GB. RAM, DVD-RW. A PRUEBA', 'link': 'https://www.milanuncios.com/portatiles-de-segunda-mano/portatil-i5-16-gb-ram-dvd-rw-a-prueba-274117830.htm', 'time': 1440, 'id': 'r274117830', 'precio': 289, 'coin': '€', 'abstract': ' Doy por escrito 3 meses de garantía. \n\ntengo más ordenadores y otras cosas,  pídeme el listado por whatsapp. \n\ncontactar solo por tlf.  o whatsapp.  al 675415873. \n\ntened en cuenta que algunos ordenadores tienen averías ocultas que quizá en el momento de la compra,  en frío,  no salga pero,  después de unas horas o días de uso,  la avería sale,  en estos 3 meses comprobarás que el mío no tiene ningún problema.  \n\nacepto como parte de pago,  tu ordenador. \n\npodéis venir a probarlo en madrido,  envío urgente,  pagándolo contra-reembolso a toda españa,  por 15 euros. \n\ntiene instalado windows 10 de 64 bits,  os puedo instalar otro windows sin coste,  paquete de office y los programas necesarios para trabajar y navegar por internet.  es ideal para hacer trabajos de ofimática,  imprimir fotos y documentos,  jugar,  etc. \n\nordenador portátil fujitsu lifebook,  modelo s752.  con bluetooth y displayport,  puerto similar a hdmi.  \n\nes un ordenador muy rápido,  podéis venir a comprobarlo. \nla batería dura unas 4 horas.  \npantalla led de 14 pulgadas panorámica. \nprocesador intel i5 de 4 núcleos a 2600 mhz. \n500 gb.  de disco duro de alta velocidad,  va a 7200 r. p. m. \n16 gb.  de memoria ram,  \n3 puertos usb,  uno es de alta velocidad. \npuerto esata de alta velocidad. \nconector vga para monitor externo. \ndisplayport para monitor o tv.  en alta definición. \ntarjetas wifi y red a 1000 mbps.  soporta fibra óptica. \nlector grabador de cds.  y dvds. \nlector de tarjetas de memoria. \nlector de tarjetas inteligentes. \nadaptador de corriente. \n\ncuesta 289 euros.  ... Leer más', 'nombre': '\nAlfredo (Particular)\n', 'telefonos': ['675415873']}
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Found 2 interesting ads on current page
Pagina 10
Detected 30 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['msi']
{'name': 'LOTE ORDENADORES DE SOBREMESA', 'link': 'https://www.milanuncios.com/portatiles-de-segunda-mano/lote-ordenadores-de-sobremesa-196789436.htm', 'time': 1440, 'id': 'r196789436', 'precio': 250, 'coin': '€', 'abstract': ' !!!oferton!!! 10 torres en perfecto estado, cpu amd athlon 2800+ 1. 8ghz/512mb ram ddr/disco duro ide 40gb/placas base gigabyte con dos controladoras sata/grafica msi mx400/dvd_rom, floppy/fuente 400w/windows xp profesional con licencia/ ragalo teclados ps2/  ideal para locutorios,  asociaciones,  autoescuelas,  oficinas. .  ect.  si los lleva antes del 30 d este mes se le quedan en 200,  no wasapp, incluida opcion de entrega a domicilio solo en Madrid incluido en precio,  envio a toda españa gastosaparte.  Abel17 ... Leer más', 'nombre': '\nParticular (Particular)\n', 'telefonos': ['677823542']}
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
{'name': 'PORTÁTIL I5,  8 GB. RAM, WEBCAM. A PRUEBA', 'link': 'https://www.milanuncios.com/portatiles-de-segunda-mano/portatil-i5-8-gb-ram-webcam-a-prueba-269454142.htm', 'time': 1440, 'id': 'r269454142', 'precio': 199, 'coin': '€', 'abstract': ' Doy por escrito 3 meses de garantía. \n\nla zone redonda que hay a la derecha del ratón,  es así,  viene de fábrica. \n\ntengo más ordenadores y otras cosas,  pídeme el listado por whatsapp. \n\ncontactar solo por tlf.  o whatsapp.  al 675415873. \n\ntened en cuenta que algunos ordenadores tienen averías ocultas que quizá en el momento de la compra,  en frío,  no salga pero,  después de unas horas o días de uso,  la avería sale,  en estos 3 meses comprobarás que el mío no tiene ningún problema.acepto como parte de pago,  tu ordenador. \n\npodéis venir a probarlo en madrid o,  envío urgente,  pagándolo contra-reembolso a toda españa,  por 15 euros. \n\ntiene instalado windows 7 de 64 bits,  os puedo instalar otro windows sin coste,  paquete de office y los programas necesarios para trabajar y navegar por internet.  es ideal para hacer trabajos de ofimática,  imprimir fotos y documentos,  jugar,  etc. \n\nordenador portátil fujitsu lifebook,  modelo s762.  con webcam,  bluetooth y displayport,  puerto similar a hdmi.  \n\nes un ordenador muy rápido,  podéis venir a comprobarlo. \nla batería dura 4 horas.  \npantalla led de 13, 3 pulgadas panorámica. \nprocesador intel i5 de 4 núcleos a 2600 mhz. \n320 gb.  de disco duro. \n8 gb.  de memoria ram,  admite price_max 16 gb.  de ram. \n2 puertos usb,  uno es de alta velocidad. \npuerto esata de alta velocidad. \nconector vga para monitor externo. \ndisplayport para monitor o tv.  en alta definición. \ntarjetas wifi y red a 1000 mbps.  soporta fibra óptica. \nlector grabador de cds.  y dvds. \nlector de tarjetas de memoria. \nlector de tarjetas inteligentes. \nadaptador de corriente. \n\ncuesta 199 euros.  ... Leer más', 'nombre': '\nAlfredo (Particular)\n', 'telefonos': ['913032129']}
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Found 2 interesting ads on current page
Pagina 11
Detected 26 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['urge']
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['(?:12|16)\\s*(?:gb|giga)', 'i[78]']
{'name': 'PLACA BASE DELL INSPIRON 15 5567', 'link': 'https://www.milanuncios.com/portatiles-de-segunda-mano/placa-base-dell-inspiron-15-5567-271217358.htm', 'time': 1440, 'id': 'r271217358', 'precio': 190, 'coin': '€', 'abstract': ' vendo placa base Dell inspiron 5567 con procesador y grafica integrados. \n\nmonta un i7 7500U de procesador\ngráfica Raedon M445. \n \n\n16 GB de RAM su batería y su DVD writer. \n\nenvío a toda España \n\n\npago vía PayPal\n\nprecio negociable\n\npreguntas por email: \nnataliama1988@gmail. com', 'nombre': '\n (Particular)\n', 'telefonos': ['639405032']}
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Item OK, list: ['(?:12|16)\\s*(?:gb|giga)', 'i[78]']
{'name': 'LENOVO THINKCENTRE M92Z I7 3770S 8GB SSD', 'link': 'https://www.milanuncios.com/ordenadores-de-segunda-mano/lenovo-thinkcentre-m92z-i7-3770s-8gb-ssd-259596344.htm', 'time': 1440, 'id': 'r259596344', 'precio': 380, 'coin': '€', 'abstract': ' OFERTóN !!TLenovo thinkcentre m92z i7 3770s 8gb ssd w10 pro 64bits\n\nAll in One tipo Imac. \n\ncolor\nbusiness black\n\nprocesador\t\n3° generación intel® core™ i7 3770s\n    \ncantidad de núcleos 4\ncantidad de subprocesos 8\nfrecuencia básica del procesador 3, 10 ghz\nfrecuencia turbo máxima 3, 90 ghz\ncaché 8 mb smartcache\ntdp 65 w\n\nlga1155 socket\n\npantalla\t\npantalla led de 23  (16: 9) \n1600x900 hd+\nse puede ajustar altura , girarlo o montarlo en la pared. \n\ngráficos\t\nintel® hd 4000(integrado)\nsalida y entrada de video displayport\nsoporta 2 monitores conectados a la vez. \n\n\nmemoria\t\n8 gb ddr3 1600 mhz\nadmite 16 gb max. \n\ncámara web integrada\t\n\naudio\t\n2 altavoces estereo 3w internos (con amplificador)\nmicrófono digital (estándar)\n\naudio salida\ndolby advanced audio v2,  high definition audio\n\n\nalmacenamiento\t\nssd:  2. 5  128gb sata 6gb samsung\nse puede añadir otro hdd o ssd . \n  \n\nunidad óptica\t\ngrabadora de dvd slim\ndvd supermulti\ndvd±rw (±r dl) / dvd-ram\n\n\npuertos i/o (entrada/salida)\t\nlateral:  2 puertos usb 3. 0,  2 de audio (uno de entrada y otro de salida)\ntrasero:  4 puertos usb 2. 0,  2 display port (uno de entrada y otro de salida)\n\nconexiones\nbluetooth 4. 0,  ethernet,  fast ethernet,  gigabit ethernet,  ieee 802. 11b,  ieee 802. 11g,  ieee 802. 11n\ncompliant standards\nbluetooth 4. 0,  ieee 802. 11b,  ieee 802. 11g,  ieee 802. 11n\nethernet controller(s)\nintel 82579lm\nwireless lan supported\nyes\nwireless nic\nintel centrino wireless-n 2230\n\nsistema operativo\t\nwindows® 7 pro x64\nactualizado a windows 10 x64 bits original\n\noffice 2016\nsepueden añadir otros programas si se desea. \nfl studio,  autodesk 3ds max. . . \n\njuegos incluidos\nthis war of mine\nunravel \n\n\nteclado y raton microsoft confort curve. \ncable de alimentacion. \n\nperfectado estado. \nse puede probar. \nsuper silencioso y rapido. \n\n\t\n\nignorar\n\nhp,  dell,  lenovo,  htc,  iphone,  ssd,  hdd,  hdmi,  i3,  i5,  i7 ganga ordenador,  torre,  pc,  portátil,  \npiezas,  raspberry pi zero 1 2 3 + iphone 5 5s 6 6s 7 mini,  sff,  usff windows 7 8 10,  cpu,  \nprocesador,  asrock,  msi,  acer, 775,  1151,  1150.  disco duro.  2, 5 3, 5 sobremesa. \n playstation xbox 360 ipad pulgadas,  samsung,  toshiba,  sony,  huawei.  ... Leer más'}
Found 2 interesting ads on current page
Pagina 12
Detected 24 ads (in total at current page)
Item OK, list: ['(?:12|16)\\s*(?:gb|giga)', 'i[78]']
{'name': 'LENOVO THINKCENTRE M92Z I7 3770S 8GB SSD', 'link': 'https://www.milanuncios.com/ordenadores-de-segunda-mano/lenovo-thinkcentre-m92z-i7-3770s-8gb-ssd-259596344.htm', 'time': 1440, 'id': 'r259596344', 'precio': 380, 'coin': '€', 'abstract': ' OFERTóN !!TLenovo thinkcentre m92z i7 3770s 8gb ssd w10 pro 64bits\n\nAll in One tipo Imac. \n\ncolor\nbusiness black\n\nprocesador\t\n3° generación intel® core™ i7 3770s\n    \ncantidad de núcleos 4\ncantidad de subprocesos 8\nfrecuencia básica del procesador 3, 10 ghz\nfrecuencia turbo máxima 3, 90 ghz\ncaché 8 mb smartcache\ntdp 65 w\n\nlga1155 socket\n\npantalla\t\npantalla led de 23  (16: 9) \n1600x900 hd+\nse puede ajustar altura , girarlo o montarlo en la pared. \n\ngráficos\t\nintel® hd 4000(integrado)\nsalida y entrada de video displayport\nsoporta 2 monitores conectados a la vez. \n\n\nmemoria\t\n8 gb ddr3 1600 mhz\nadmite 16 gb max. \n\ncámara web integrada\t\n\naudio\t\n2 altavoces estereo 3w internos (con amplificador)\nmicrófono digital (estándar)\n\naudio salida\ndolby advanced audio v2,  high definition audio\n\n\nalmacenamiento\t\nssd:  2. 5  128gb sata 6gb samsung\nse puede añadir otro hdd o ssd . \n  \n\nunidad óptica\t\ngrabadora de dvd slim\ndvd supermulti\ndvd±rw (±r dl) / dvd-ram\n\n\npuertos i/o (entrada/salida)\t\nlateral:  2 puertos usb 3. 0,  2 de audio (uno de entrada y otro de salida)\ntrasero:  4 puertos usb 2. 0,  2 display port (uno de entrada y otro de salida)\n\nconexiones\nbluetooth 4. 0,  ethernet,  fast ethernet,  gigabit ethernet,  ieee 802. 11b,  ieee 802. 11g,  ieee 802. 11n\ncompliant standards\nbluetooth 4. 0,  ieee 802. 11b,  ieee 802. 11g,  ieee 802. 11n\nethernet controller(s)\nintel 82579lm\nwireless lan supported\nyes\nwireless nic\nintel centrino wireless-n 2230\n\nsistema operativo\t\nwindows® 7 pro x64\nactualizado a windows 10 x64 bits original\n\noffice 2016\nsepueden añadir otros programas si se desea. \nfl studio,  autodesk 3ds max. . . \n\njuegos incluidos\nthis war of mine\nunravel \n\n\nteclado y raton microsoft confort curve. \ncable de alimentacion. \n\nperfectado estado. \nse puede probar. \nsuper silencioso y rapido. \n\n\t\n\nignorar\n\nhp,  dell,  lenovo,  htc,  iphone,  ssd,  hdd,  hdmi,  i3,  i5,  i7 ganga ordenador,  torre,  pc,  portátil,  \npiezas,  raspberry pi zero 1 2 3 + iphone 5 5s 6 6s 7 mini,  sff,  usff windows 7 8 10,  cpu,  \nprocesador,  asrock,  msi,  acer, 775,  1151,  1150.  disco duro.  2, 5 3, 5 sobremesa. \n playstation xbox 360 ipad pulgadas,  samsung,  toshiba,  sony,  huawei.  ... Leer más'}
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Found 1 interesting ads on current page
Pagina 13
Detected 21 ads (in total at current page)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Skipping item ('4\s*(?:gb|giga)' found)
Finished (max minutes or ads)

```


## Requisites

### Making Chrome & ChromeDriver undetectable to Distil technology (only headed version for now)

1. You need a stable version of google-chrome-stable installed WHICH HAS NOT 'NavigatorAutomationInformation' implemented. 
After almost becoming crazy trying to find how to remove the 'navigator.webdriver' tag, it was really simple.
That property is set at runtime by a method webdriver() which always return true, as long as 'webdriver' is visible in the Navigator interface scope.
I did not notice how did worked until I found a google group where they put a link to the commit that incorporated all changes to accomplish with
W3C rules for webdrivers, that means, incorporating 'NavigatorAutomationInformation' to the prototype.

That means you have two options here:

	1.A. Recompile the last version of chromium (probably "no, thanks")
		1.A.1. Download the source (https://chromium.googlesource.com/chromium/src/+/master/docs/linux_build_instructions.md#System-requirements)
		1.A.2. Modify 'third_party/WebKit/Source/core/frame/Navigator.idl' by commenting the line 'Navigator implements NavigatorAutomationInformation';
		1.A.3. Start compiling it in your super-computer and go on holidays. When you are back maybe it will be built.

	1.B. Use a version which hasn't commited that change yet. That means, anything uploaded *before Oct 2017* (ej. v61).
		1.B.1. Find deb package mirros using 'inurl:/deb/pool/main/g/google-chrome-stable/' at Google.



2. You need to install an also patched version of ChromeDriver at '/usr/bin/local'.

Well, they look for $cdc_... document variable names, and they catch you if there's one. ChromeDriver put one of these, so we have to change it.

	2.A. Download ChromeDriver sourcecode (available in the Chromium source code too, downloadable with depot_tools). (I'd go for 2.B).
		2.A.1. Find the file 'call_function.js' and replace the line 'var key = '$cdc_asdjflasutopfhvcZLmcfl_';' with 'var key = 'sex_and_whisky_';
		2.A.2. Compile it and move it to the folder we said.
	

	2.B. Download ChromeDriver binary for a version which fits the chrome binary. (eg. for chrome v61, we download v2.34, see 
	http://chromedriver.chromium.org/downloads, https://chromedriver.storage.googleapis.com/index.html?path=2.34/)
		2.B.1. Open it with an hex editor and do the step 2.A.1.


### Libraries

Python dependencies:

1. python3 -m pip install beautifulsoup4



## To do

- Read configs from json
- Add whatsap messaging
- Add other modules
