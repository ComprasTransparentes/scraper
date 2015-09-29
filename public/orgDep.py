# -*- coding: utf-8-*-
import json
import sys

elbigjson = {
    "name": "Gobierno Central",
    "children": [{
        "name": "Presidencia de la Rep\u00fablica",
        "children": [{
            "name": "Presidencia de la Rep\u00fablica",
            "info": "El Poder Ejecutivo est\u00e1 encabezado por el Presidente de la Rep\u00fablica, quien desarrolla las funciones de Jefe de Estado, simbolizando y representando los intereses permanentes del pa\u00eds. A su vez, como Jefe de Gobierno, es quien dirige la pol\u00edtica gubernamental, respaldado por la mayor\u00eda pol\u00edtico-electoral.",
            "url": "http:\/\/www.presidencia.cl"
        }]
    }, {
        "name": "Ministerio del Interior y Seguridad P\u00fablica",
        "children": [{
            "name": "Subsecretar\u00eda del Interior",
            "info": "<p>Asistir en el ejercicio del gobierno y la administraci\u00f3n interior del Estado a quien ejerza la Presidencia de la Rep\u00fablica. Provee la plataforma pol\u00edtica, administrativa y de gesti\u00f3n para que quienes dirigen las intendencias y gobernaciones puedan ejercer a cabalidad dicha representaci\u00f3n en las jurisdicciones en que se divide el territorio nacional para efectos del ejercicio del gobierno y administraci\u00f3n superior y, adem\u00e1s, proporciona a la poblaci\u00f3n los bienes, prestaciones y servicios que establece la ley o las pol\u00edticas establecidas por el Ministerio del Interior.<\/p>",
            "url": "http:\/\/www.interior.gov.cl"
        }, {
            "name": "Subsecretar\u00eda de Desarrollo Regional",
            "info": "La misi\u00f3n de la Subdere es contribuir al desarrollo de los territorios, fortaleciendo su capacidad de buen gobierno, en coherencia con el proceso de descentralizaci\u00f3n.",
            "url": "http:\/\/www.subdere.gov.cl"
        }, {
            "name": "Agencia Nacional de Inteligencia",
            "info": "",
            "url": ""
        }, {
            "name": "Oficina Nacional de Emergencia",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Gobierno Interior",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio Electoral",
            "info": "Corresponde al Servicio Electoral velar por la mantenci\u00f3n del Archivo Electoral General; as\u00ed como la eficaz realizaci\u00f3n de los procesos electorales que peri\u00f3dicamente determina el ordenamiento jur\u00eddico nacional y la ejecuci\u00f3n de las acciones que le competen al Estado en el ordenamiento constitucional sobre partidos pol\u00edticos. Esta misi\u00f3n se lleva a cabo mediante la creaci\u00f3n de las condiciones para el ejercicio igualitario de los derechos electorales y mediante la ampliaci\u00f3n de la informaci\u00f3n hacia los Ciudadanos, Partidos Pol\u00edticos y Organismos Electorales con los que esta Instituci\u00f3n se relaciona.",
            "url": "http:\/\/www.servel.cl"
        }, {
            "name": "Intendencia Arica y Parinacota",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de Antofagasta",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de Atacama",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de Ays\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de Coquimbo",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de la Araucan\u00eda",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de Los Lagos",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de Los R\u00edos",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de Magallanes",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de O\u2019Higgins",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de Tarapac\u00e1",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia de Valpara\u00edso",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia del B\u00edo B\u00edo",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia del Maule",
            "info": "",
            "url": ""
        }, {
            "name": "Intendencia Metropolitana",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Arica",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Parinacota",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Iquique",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Tamarugal",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Antofagasta",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de El Loa",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Tocopilla",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Cha\u00f1aral",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Copiap\u00f3",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Huasco",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Elqui",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Limar\u00ed",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Choapa",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Petorca",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Valpara\u00edso",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de San Felipe",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Los Andes",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Quillota",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de San Antonio",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Isla de Pascua",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Cachapoal",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Colchagua",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Cardenal Caro",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Curic\u00f3",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Talca",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Linares",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Cauquenes",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de \u00d1uble",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de B\u00edo B\u00edo",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Concepci\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Arauco",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Malleco",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Caut\u00edn",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Valdivia",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Ranco",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Osorno",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Llanquihue",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Chilo\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Palena",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Coyhaique",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Puerto Ays\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de General Carrera",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Capit\u00e1n Prat",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de \u00daltima Esperanza",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Magallanes",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Tierra del Fuego",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de la Ant\u00e1rtica Chilena",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Chacabuco",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Cordillera",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Maipo",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Talagante",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Melipilla",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de Arica y Parinacota",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de Tarapac\u00e1",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de Antofagasta",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de Atacama",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de Coquimbo",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de Valpara\u00edso",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional Metropolitano de Santiago",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de O\u00b4Higgins",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional del Maule",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional del B\u00edo B\u00edo",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de La Araucan\u00eda",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de Los R\u00edos",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de Los Lagos",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de Ays\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Gobierno Regional de Magallanes y Ant\u00e1rtica Chilena ",
            "info": "",
            "url": ""
        }, {
            "name": "Gobernaci\u00f3n de Marga Marga",
            "info": "",
            "url": ""
        }, {
            "name": "Subsecretar\u00eda de Prevenci\u00f3n del Delito",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio Nacional de Prevenci\u00f3n y Rehabilitaci\u00f3n del Consumo de Drogas y Alcohol",
            "info": "",
            "url": ""
        }, {
            "name": "Departamento de Extranjer\u00eda y Migraci\u00f3n",
            "info": "<p>.<\/p>",
            "url": ""
        }, {
            "name": "Carabineros de Chile",
            "info": "Su misi\u00f3n es brindar seguridad a la comunidad en todo el territorio nacional mediante acciones prioritariamente preventivas, apoyadas por un permanente acercamiento a la comunidad. Privilegia la acci\u00f3n policial eficaz, eficiente, justa y transparente.",
            "url": "http:\/\/www.carabineros.cl"
        }, {
            "name": "Polic\u00eda de Investigaciones",
            "info": "Dar eficacia al derecho, garantizar el orden p\u00fablico y la seguridad p\u00fablica interior, a trav\u00e9s de la investigaci\u00f3n profesional y especializada de los delitos, de la inteligencia criminal, del control migratorio y de la cooperaci\u00f3n internacional, apoyando la generaci\u00f3n de condiciones b\u00e1sicas para la tranquilidad ciudadana que permitan el desarrollo econ\u00f3mico, pol\u00edtico, cultural y social de Chile.",
            "url": "http:\/\/www.investigaciones.cl\/"
        }, {
            "name": "Direcci\u00f3n de Previsi\u00f3n de Carabineros de Chile",
            "info": "<p>Entregar servicios de Previsi\u00f3n, Salud y Asistencias, mediante un modelo moderno y eficiente que asegure la calidad de tales prestaciones a nuestros beneficiarios de Carabineros, Polic\u00eda de Investigaciones, Gendarmer\u00eda de Chile, Mutualidad de Carabineros y DIPRECA.<\/p>",
            "url": "http:\/\/www.dipreca.cl"
        }]
    }, {
        "name": "Ministerio de Relaciones Exteriores",
        "children": [{
            "name": "Subsecretar\u00eda de Relaciones Exteriores",
            "info": "",
            "url": "http:\/\/www.minrel.gob.cl"
        }, {
            "name": "Direcci\u00f3n General de Relaciones Econ\u00f3micas Internacionales",
            "info": "",
            "url": ""
        }, {
            "name": "Direcci\u00f3n Nacional de Fronteras y L\u00edmites del Estado",
            "info": "Preservar y fortalecer la integridad territorial del Pa\u00eds, asesorando profesional y t\u00e9cnicamente al Supremo Gobierno y participando en la celebraci\u00f3n de Tratados, en la negociaci\u00f3n de Convenios, as\u00ed como en los Foros y en las materias relacionadas con los L\u00edmites Internacionales de Chile y las Pol\u00edticas de Integraci\u00f3n F\u00edsica, Vecinal y Regional, a trav\u00e9s del Ministerio de Relaciones Exteriores.",
            "url": "http:\/\/www.difrol.gov.cl"
        }, {
            "name": "Agencia de Cooperaci\u00f3n Internacional",
            "info": "Contribuir al logro de los objetivos de la pol\u00edtica exterior definidos por el Gobierno impulsando acciones de cooperaci\u00f3n Horizontal, Triangular para instituciones y pa\u00edses de la regi\u00f3n y de perfeccionamiento de recursos humanos para profesionales de Latinoam\u00e9rica, como asimismo, apoyar y complementar las pol\u00edticas, planes y programas nacionales prioritarios que promueva el Gobierno orientados al desarrollo del pa\u00eds, impulsando acciones de cooperaci\u00f3n bimultilateral.",
            "url": "http:\/\/www.agci.gob.cl"
        }, {
            "name": "Instituto Ant\u00e1rtico Chileno",
            "info": "Cumplir con la Pol\u00edtica Ant\u00e1rtica Nacional, incentivando el desarrollo de la investigaci\u00f3n cient\u00edfica, tecnol\u00f3gica y de innovaci\u00f3n en la Ant\u00e1rtica siguiendo c\u00e1nones internacionales, la participaci\u00f3n efectiva en el Sistema del Tratado Ant\u00e1rtico y Foros Internacionales relacionados, el fortalecimiento de Punta Arenas como puerta de entrada al Continente Blanco, la realizaci\u00f3n de acciones y actividades de divulgaci\u00f3n y valoraci\u00f3n del conocimiento ant\u00e1rtico en la comunidad nacional y asesorando al Ministerio de Relaciones Exteriores en materias ant\u00e1rticas.",
            "url": "http:\/\/www.inach.gob.cl"
        }]
    }, {
        "name": "Ministerio de Defensa Nacional",
        "children": [{
            "name": "Ej\u00e9rcito de Chile",
            "info": "",
            "url": ""
        }, {
            "name": "Armada de Chile",
            "info": "",
            "url": ""
        }, {
            "name": "Fuerza A\u00e9rea de Chile",
            "info": "",
            "url": ""
        }, {
            "name": "Direcci\u00f3n Administrativa",
            "info": "",
            "url": ""
        }, {
            "name": "Defensa Civil de Chile",
            "info": "Su misi\u00f3n general ser\u00e1 desarrollar en forma permanente acciones y actividades de prevenci\u00f3n y respuesta, ante la ocurrencia de emergencias, desastres o cat\u00e1strofes de origen natural y\/o antr\u00f3pico, como organizaci\u00f3n integrante del Sistema Nacional de Protecci\u00f3n Civil. En tal sentido, actuar\u00e1 en resguardo de las personas, de sus bienes y del medio ambiente ante situaciones de riesgo colectivo, tanto en tiempo normal como durante la vigencia de los Estados de Excepci\u00f3n.",
            "url": "http:\/\/www.defensacivil.cl\/"
        }, {
            "name": "Direcci\u00f3n General de Movilizaci\u00f3n Nacional",
            "info": "Tener a su cargo el reclutamiento del contingente para las instituciones de las F.AA., como asimismo, la preparaci\u00f3n de la movilizaci\u00f3n del potencial humano, material e industrial nacional para dar satisfacci\u00f3n a los requerimientos de los Campos de Acci\u00f3n B\u00e9lico, Econ\u00f3mico, Externo e Interno.Efectuar el control de las armas y otros elementos, su Reglamento Complementario.Efectuar el control de las artes marciales,el control de las sustancias qu\u00edmicas y otros elementos afines.",
            "url": "http:\/\/www.dgmn.cl\/"
        }, {
            "name": "Direcci\u00f3n General del Territorio Mar\u00edtimo y Marina Mercante",
            "info": "DIRECTEMAR es el organismo de la Armada, mediante el cual el Estado de Chile cautela el cumplimiento de las leyes y acuerdos internacionales vigentes, para proteger la vida humana en el mar, el medio ambiente, los recursos naturales y regular las actividades que se desarrollan en el \u00e1mbito acu\u00e1tico de su jurisdicci\u00f3n, con el prop\u00f3sito de contribuir el desarrollo mar\u00edtimo de la naci\u00f3n.",
            "url": "http:\/\/www.directemar.cl\/"
        }, {
            "name": "Caja de Previsi\u00f3n de la Defensa Nacional",
            "info": "Satisfacer a nuestros clientes(as) mediante la entrega oportuna y eficiente de las prestaciones del sistema de seguridad social de las Fuerzas Armadas, mejorando continuamente la gesti\u00f3n del pago de pensiones y sus servicios asociados, bonificaciones y prestaciones de salud, servicios sociales y financieros.",
            "url": "http:\/\/www.capredena.gov.cl\/"
        }, {
            "name": "Instituto Geogr\u00e1fico Militar",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio Aerofotogram\u00e9trico FACh",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio Hidrogr\u00e1fico y Oceanogr\u00e1fico de la Armada",
            "info": "El Servicio Hidrogr\u00e1fico y Oceanogr\u00e1fico de la Armada de Chile tiene por misi\u00f3n principal proporcionar los elementos t\u00e9cnicos y las informaciones y asistencias t\u00e9cnica destinada a dar seguridad a la navegaci\u00f3n en las v\u00edas fluviales y lacustres, aguas interiores, mar territorial y en alta mar contigua al litoral de Chile.",
            "url": "http:\/\/www.shoa.cl\/"
        }, {
            "name": "Direcci\u00f3n General de Aeron\u00e1utica Civil",
            "info": "Normar y fiscalizar las actividades a\u00e9reas que se realizan en el espacio a\u00e9reo controlado por Chile y las que ejecutan usuarios nacionales en el extranjero; prestar servicios de navegaci\u00f3n a\u00e9rea, meteorolog\u00eda, aeroportuarios y seguridad operacional, con el prop\u00f3sito de permitir una actividad a\u00e9rea segura, eficiente y sustentable, contribuyendo al desarrollo nacional.",
            "url": "http:\/\/www.dgac.gob.cl\/"
        }, {
            "name": "Subsecretar\u00eda de Defensa",
            "info": "",
            "url": ""
        }, {
            "name": "Subsecretar\u00eda para las Fuerzas Armadas",
            "info": "La Subsecretar\u00eda para las Fuerzas Armadas es el \u00f3rgano de colaboraci\u00f3n del Ministro Defensa Nacional en las materias que tienen relaci\u00f3n con la formulaci\u00f3n de pol\u00edticas y con la gesti\u00f3n de los asuntos y procesos administrativos financieros del Ministerio y las Fuerzas Armadas. Es la sucesora para todos los efectos legales, reglamentarios y contractuales de las Subsecretar\u00edas de Guerra, de Marina y de Aviaci\u00f3n y de la Direcci\u00f3n Administrativa del Ministerio de Defensa Nacional.",
            "url": "http:\/\/www.ssffaa.cl"
        }, {
            "name": "Estado Mayor Conjunto ",
            "info": "",
            "url": ""
        }]
    }, {
        "name": "Ministerio de Hacienda",
        "children": [{
            "name": "Subsecretar\u00eda de Hacienda ",
            "info": "Su misi\u00f3n es maximizar la tasa de crecimiento de la econom\u00eda, logrando el mejor uso y rendimiento de los recursos productivos con que cuenta el pa\u00eds, para as\u00ed alcanzar un crecimiento econ\u00f3mico alto y estable que se traduzca en una mejor calidad de vida para todos los chilenos y chilenas, especialmente los sectores m\u00e1s postergados y vulnerables.",
            "url": "http:\/\/www.hacienda.gov.cl\/"
        }, {
            "name": "Direcci\u00f3n de Presupuestos",
            "info": "Nuestra misi\u00f3n es velar por la eficiente asignaci\u00f3n y uso de los recursos p\u00fablicos en el marco de la pol\u00edtica fiscal, mediante la aplicaci\u00f3n de sistemas e instrumentos de gesti\u00f3n financiera, programaci\u00f3n y control de gesti\u00f3n.",
            "url": "http:\/\/www.dipres.gob.cl\/"
        }, {
            "name": "Tesorer\u00eda General de la Rep\u00fablica",
            "info": "Recaudar y cobrar las obligaciones tributarias y cr\u00e9ditos del sector p\u00fablico, administrando el Tesoro y distribuyendo los fondos de manera oportuna y transparente, contribuyendo as\u00ed al desarrollo del pa\u00eds y de sus ciudadanos.",
            "url": "http:\/\/www.tesoreria.cl\/"
        }, {
            "name": "Direcci\u00f3n Nacional del Servicio Civil",
            "info": "",
            "url": ""
        }, {
            "name": "Unidad de An\u00e1lisis Financiero",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Impuestos Internos",
            "info": "<p>La Misi&oacute;n del Servicio como Instituci&oacute;n del Estado es: \"Administrar con equidad y justicia el sistema de tributos internos de destino fiscal, facilitando el cumplimiento voluntario mediante la provisi&oacute;n de servicios de calidad, adecuados a cada tipo de contribuyente; velando por el correcto cumplimiento tributario con estricto apego a la legalidad vigente y focalizando el esfuerzo fiscalizador en los contribuyentes con comportamiento tributario riesgoso.<\/p>",
            "url": "http:\/\/www.sii.cl"
        }, {
            "name": "Servicio Nacional de Aduanas",
            "info": "Resguardar los intereses de la Naci\u00f3n y apoyar el Comercio Exterior del pa\u00eds, mediante el uso eficiente e integrado de la fiscalizaci\u00f3n y facilitaci\u00f3n de las operaciones de Comercio Internacional, bas\u00e1ndose en el principio de la buena fe, en un clima de confianza y actuando conforme a los principios de probidad y transparencia.",
            "url": "http:\/\/www.aduana.gob.cl"
        }, {
            "name": "Superintendencia de Bancos e Instituciones Financieras",
            "info": "El mandato que le impone la Ley General de Bancos a la Superintendencia de Bancos e Instituciones Financieras, es supervisar las empresas bancarias y otras instituciones financieras, en resguardo de los depositantes u otros acreedores y del inter\u00e9s p\u00fablico.",
            "url": "http:\/\/www.sbif.gob.cl"
        }, {
            "name": "Superintendencia de Valores y Seguros",
            "info": "Resguardar los derechos de los inversionistas y asegurados para propender al desarrollo de los mercados de valores y seguros a trav\u00e9s de una regulaci\u00f3n y una fiscalizaci\u00f3n que facilite el funcionamiento de \u00e9stos, de manera confiable y transparente.",
            "url": "http:\/\/www.svs.gob.cl"
        }, {
            "name": "Direcci\u00f3n de Compras y Contrataci\u00f3n P\u00fablica",
            "info": "<p class=\"MsoNormal\">Nuestra misi\u00f3n es crear valor en el Mercado P\u00fablico de Chile, poniendo a disposici\u00f3n de nuestros clientes el sistema de informaci\u00f3n de compras p\u00fablicas, para que los compradores realicen sus compras y contrataciones utilizando de manera eficiente y transparente los recursos del Estado; y para que los proveedores tengan mayor facilidad de acceso y puedan competir en \u00e9ste en igualdad de oportunidades.\u00a0Nuestro compromiso es desarrollar un mercado p\u00fablico transparente, confiable, sustentable y de amplio acceso, utilizando de manera intensiva las tecnolog\u00edas de informaci\u00f3n y poniendo en el centro de la gesti\u00f3n a nuestros clientes.<\/p>",
            "url": "http:\/\/www.chilecompra.cl\/"
        }, {
            "name": "Superintendencia de Casinos de Juego",
            "info": "",
            "url": ""
        }]
    }, {
        "name": "Ministerio Secretar\u00eda General de la Presidencia",
        "children": [{
            "name": "Subsecretar\u00eda General de la Presidencia",
            "info": "",
            "url": "http:\/\/www.minsegpres.gob.cl"
        }, {
            "name": "Servicio Nacional del Adulto Mayor",
            "info": "",
            "url": ""
        }, {
            "name": "Comisi\u00f3n Defensora Ciudadana",
            "info": "<p>La Comisi\u00f3n Asesora Presidencial para la Protecci\u00f3n de los Derechos de las Personas tiene como misi\u00f3n velar por la defensa y promoci\u00f3n de los derechos e intereses de las personas ante acciones u omisiones de los organismos p\u00fablicos, en lo relativo a la satisfacci\u00f3n de las necesidades de los ciudadanos frente a la prestaci\u00f3n de estos servicios.<\/p>",
            "url": "http:\/\/www.comisiondefensoraciudadana.cl\/"
        }]
    }, {
        "name": "Ministerio Secretar\u00eda General de Gobierno",
        "children": [{
            "name": "Subsecretar\u00eda General de Gobierno",
            "info": "",
            "url": ""
        }, {
            "name": "Instituto Nacional del Deporte",
            "info": "Desarrollar la cultura deportiva de la poblaci\u00f3n a trav\u00e9s de la ejecuci\u00f3n de planes y programas de fomento e infraestructura, y el financiamiento de proyectos, orientados a masificar la actividad f\u00edsica y la pr\u00e1ctica deportiva y a apoyar a los deportistas tomando como eje su crecimiento dentro del Sistema de Competencias Deportivas, con una perspectiva territorial, intersectorial y de g\u00e9nero.",
            "url": "http:\/\/www.ind.cl\/"
        }, {
            "name": "Consejo Nacional de Televisi\u00f3n",
            "info": "Su misi\u00f3n es velar por el correcto funcionamiento de los servicios de televisi\u00f3n.",
            "url": "http:\/\/www.cntv.cl\/"
        }]
    }, {
        "name": "Ministerio de Econom\u00eda, Fomento y Turismo",
        "children": [{
            "name": "Subsecretar\u00eda de Econom\u00eda y Empresa de Menor Tama\u00f1o",
            "info": "<p>Su misi\u00f3n es mejorar la calidad de vida de los ciudadanos a trav\u00e9s del crecimiento econ\u00f3mico, dise\u00f1ando y promoviendo pol\u00edticas regulatorias, y de fomento e innovaci\u00f3n para la competitividad.<\/p>",
            "url": "http:\/\/www.economia.gob.cl\/"
        }, {
            "name": "Subsecretar\u00eda de Pesca",
            "info": "Su misi\u00f3n es administrar, regular, controlar, desarrollar y difundir la actividad de la pesca industrial y artesanal, a trav\u00e9s de la investigaci\u00f3n b\u00e1sica y aplicada, innovaci\u00f3n tecnol\u00f3gica, formaci\u00f3n de recursos humanos altamente calificados, promoci\u00f3n de los productos en los mercados interno y externo para la conservaci\u00f3n y manejo sustentable de los recursos pesqueros en todo el territorio nacional.",
            "url": "http:\/\/www.subpesca.gob.cl"
        }, {
            "name": "Comit\u00e9 de Inversiones Extranjeras",
            "info": "Apoyar el posicionamiento de Chile como plaza de alto atractivo para la inversi\u00f3n extranjera y los negocios internacionales actuando en materias relacionadas con la administraci\u00f3n y difusi\u00f3n de la normativa legal pertinente, el desarrollo de actividades de promoci\u00f3n de diversa \u00edndole y la elaboraci\u00f3n de informaci\u00f3n relevante en materia de inversi\u00f3n extranjera, para inversionistas extranjeros y potenciales inversionistas.",
            "url": "http:\/\/www.inversionextranjera.gob.cl\/"
        }, {
            "name": "Corporaci\u00f3n de Fomento de la Producci\u00f3n",
            "info": "<p>Fomentar el emprendimiento y la innovaci&oacute;n para mejorar la productividad de Chile, y alcanzar posiciones de liderazgo mundial en materia de competitividad.<\/p>",
            "url": "http:\/\/www.corfo.gob.cl"
        }, {
            "name": "Fiscal\u00eda Nacional Econ\u00f3mica",
            "info": "Defender y promover la libre competencia actuando en representaci\u00f3n del inter\u00e9s p\u00fablico como organismo especializado, para evitar que agentes con poder de mercado atenten individual o conjuntamente contra la libertad econ\u00f3mica, procurando as\u00ed el mayor bienestar general de la sociedad.",
            "url": "http:\/\/www.fne.gob.cl\/"
        }, {
            "name": "Instituto Nacional de Estad\u00edsticas",
            "info": "Producir y difundir estad\u00edsticas oficiales de Chile, proporcionando informaci\u00f3n confiable y accesible a los usuarios para la toma de decisiones, logrando un mayor conocimiento de la realidad del pa\u00eds.  Articular el Sistema Estad\u00edstico Nacional, de manera que \u00e9ste provea al pa\u00eds informaci\u00f3n pertinente, relevante y comparable a nivel nacional e internacional.",
            "url": "http:\/\/www.ine.cl\/"
        }, {
            "name": "Servicio Nacional de Turismo",
            "info": "Ejecutar la Pol\u00edtica Nacional de Turismo mediante la implementaci\u00f3n de planes y programas que incentiven la competitividad y participaci\u00f3n del sector privado, el fomento de la oferta tur\u00edstica, la promoci\u00f3n y difusi\u00f3n de los destinos tur\u00edsticos resguardando el desarrollo sustentable de la actividad, que beneficien a los visitantes, nacionales y extranjeros, prestadores de servicios tur\u00edsticos, comunidades y al pa\u00eds en su conjunto.",
            "url": "http:\/\/www.sernatur.cl"
        }, {
            "name": "Servicio Nacional del Consumidor",
            "info": "<p>Construir una cultura de respeto a los derechos de los consumidores, mejorando continuamente su gesti\u00f3n e impulsando iniciativas que respondan a los problemas cotidianos de las personas.<\/p>",
            "url": "http:\/\/www.sernac.gob.cl\/"
        }, {
            "name": "Servicio Nacional de Pesca",
            "info": "Fiscalizar el cumplimiento de la normativa pesquera y de acuicultura, nacional e internacional, que contribuya con el desarrollo sustentable del sector pesquero nacional, a trav\u00e9s de estrategias de monitoreo, control y vigilancia sectorial.",
            "url": "http:\/\/www.sernapesca.gob.cl\/"
        }, {
            "name": "Subsecretar\u00eda de Turismo",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Cooperaci\u00f3n T\u00e9cnica ",
            "info": "Promover y apoyar iniciativas de mejoramiento de la competitividad de las micro y peque\u00f1as empresas y fortalecer el desarrollo de la capacidad de gesti\u00f3n de sus empresarios.",
            "url": "http:\/\/www.sercotec.gob.cl\/"
        }, {
            "name": "Comit\u00e9 Innova B\u00edo B\u00edo",
            "info": "Contribuir a la competitividad regional y a la creaci\u00f3n futura de fuentes sustentables de empleo, a trav\u00e9s del fortalecimiento de la innovaci\u00f3n y el desarrollo tecnol\u00f3gico.",
            "url": "http:\/\/www.innovabiobio.cl\/"
        }, {
            "name": "Instituto Nacional de Propiedad Industrial",
            "info": "Contribuir al desarrollo econ\u00f3mico nacional estimulando el emprendimiento, la innovaci\u00f3n y la creatividad mediante la protecci\u00f3n de la propiedad industrial y la gesti\u00f3n del conocimiento, sobre la base de procesos que aseguren eficacia, eficiencia, calidad, legalidad, as\u00ed como accesibilidad y certidumbre de la informaci\u00f3n.",
            "url": "http:\/\/www.inapi.cl\/"
        }]
    }, {
        "name": "Ministro de Desarrollo Social",
        "children": [{
            "name": "Subsecretar\u00eda de Planificaci\u00f3n",
            "info": "La misi\u00f3n del Ministerio de Planificaci\u00f3n es promover el desarrollo del pa\u00eds con integraci\u00f3n y protecci\u00f3n social de las personas, articulando acciones con las autoridades pol\u00edticas, \u00f3rganos del Estado y sociedad civil, a nivel nacional, regional y local, mediante el an\u00e1lisis, dise\u00f1o, coordinaci\u00f3n, ejecuci\u00f3n y evaluaci\u00f3n de pol\u00edticas sociales, planes y programas; la evaluaci\u00f3n de las iniciativas de inversi\u00f3n p\u00fablica; la provisi\u00f3n de informaci\u00f3n y an\u00e1lisis acerca de la realidad social y econ\u00f3mica; y la elaboraci\u00f3n de instrumentos y metodolog\u00edas para la gesti\u00f3n y toma de decisiones de pol\u00edticas p\u00fablicas.",
            "url": "http:\/\/www.mideplan.gob.cl"
        }, {
            "name": "Corporaci\u00f3n Nacional de Desarrollo Ind\u00edgena",
            "info": "Promover, coordinar y ejecutar la acci\u00f3n del Estado en favor del desarrollo integral de las personas y comunidades ind\u00edgenas, especialmente en lo econ\u00f3mico, social y cultural y de impulsar su participaci\u00f3n en la vida nacional, a trav\u00e9s de la coordinaci\u00f3n intersectorial, el financiamiento de iniciativas de inversi\u00f3n y la prestaci\u00f3n de servicios a usuarios.",
            "url": "http:\/\/www.conadi.gob.cl\/"
        }, {
            "name": "Servicio Nacional de la Discapacidad",
            "info": "La misi\u00f3n del Servicio Nacional de la Discapacidad es velar por la igualdad de oportunidades, la inclusi\u00f3n social, el respeto de los derechos, la participaci\u00f3n en el di\u00e1logo social y la accesibilidad de las personas con discapacidad y su entorno, a trav\u00e9s de la asesor\u00eda, coordinaci\u00f3n intersectorial y ejecuci\u00f3n de pol\u00edticas p\u00fablicas.",
            "url": "http:\/\/www.senadis.gob.cl\/"
        }, {
            "name": "Fondo de Solidaridad e Inversi\u00f3n Social",
            "info": "Trabajar con sentido de urgencia por erradicar la pobreza y disminuir la vulnerabilidad en Chile.",
            "url": "http:\/\/www.fosis.gob.cl"
        }, {
            "name": "Instituto Nacional de la Juventud",
            "info": "Colaborar en el dise\u00f1o, planificaci\u00f3n y coordinaci\u00f3n de pol\u00edticas p\u00fablicas en materia de juventud, a trav\u00e9s del estudio de la realidad juvenil, y la coordinaci\u00f3n con los agentes p\u00fablicos y privados relacionados con dicha tem\u00e1tica, con el objeto de dar soluci\u00f3n a las problem\u00e1ticas juveniles, principalmente enfocado a los grupos m\u00e1s vulnerable; crear un marco de igualdad de oportunidades e inclusi\u00f3n social\u00a0en dicho grupo et\u00e1reo; y a su vez, promover la participaci\u00f3n de este segmento en el desarrollo del pa\u00eds, mediante el\u00a0fortalecimiento del emprendimiento social, p\u00fablico, acad\u00e9mico, cultural y pol\u00edtico de la juventud chilena.",
            "url": "http:\/\/www.injuv.gob.cl\/"
        }, {
            "name": "Servicio Nacional del Adulto Mayor",
            "info": "Fomentar el envejecimiento activo y el desarrollo\u00a0 de servicios sociales para las personas mayores, cualquiera sea su condici\u00f3n, fortaleciendo su participaci\u00f3n y valoraci\u00f3n en la sociedad, promoviendo su autocuidado y autonom\u00eda, y favoreciendo el reconocimiento y ejercicio de sus derechos; por medio de la coordinaci\u00f3n intersectorial, el dise\u00f1o, implementaci\u00f3n y evaluaci\u00f3n de pol\u00edticas, planes y programas.",
            "url": "http:\/\/www.senama.gob.cl\/"
        }, {
            "name": "Subsecretar\u00eda de Evaluaci\u00f3n Social",
            "info": "",
            "url": ""
        }, {
            "name": "Subsecretar\u00eda de Servicios Sociales",
            "info": "",
            "url": ""
        }]
    }, {
        "name": "Ministerio de Educaci\u00f3n",
        "children": [{
            "name": "Subsecretar\u00eda de Educaci\u00f3n",
            "info": "La misi\u00f3n del Ministerio de Educaci\u00f3n es fomentar el desarrollo de la educaci\u00f3n en todos sus niveles y promover el progreso integral de todas las personas, a trav\u00e9s de un sistema educativo que asegure igualdad de oportunidades y aprendizaje de calidad para todos los ni\u00f1os\/as, j\u00f3venes y adultos durante su vida, con independencia de la edad y el sexo; otorg\u00e1ndoles una educaci\u00f3n humanista, democr\u00e1tica, de excelencia y abierta al mundo en todos los niveles de ense\u00f1anza, cautelando el buen uso de los recursos p\u00fablicos y contribuyendo activamente a la garant\u00efza del derecho a la educaci\u00f3n y a la libertad de ense\u00f1anza.",
            "url": "http:\/\/www.mineduc.gob.cl\/"
        }, {
            "name": "Consejo de Rectores de las Universidades Chilenas",
            "info": "",
            "url": ""
        }, {
            "name": "Consejo Nacional de Educaci\u00f3n",
            "info": "",
            "url": "http:\/\/www.cned.cl\/"
        }, {
            "name": "Comisi\u00f3n Administradora del Sistema de Cr\u00e9ditos para Estudios Superiores (Comisi\u00f3n Ingresa)",
            "info": "<p class=\"MsoNormal\">Es responsabilidad de Comisi\u00f3n Ingresa, dise\u00f1ar e implementar instrumentos de financiamiento para Educaci\u00f3n Superior que contemplen el uso de recursos tanto p\u00fablicos como privados, orientados a personas que cumplan con determinados est\u00e1ndares acad\u00e9micos y socioecon\u00f3micos. El prop\u00f3sito de esta misi\u00f3n es ampliar las oportunidades de acceso al sistema de Educaci\u00f3n Superior de Chile.\u00a0<\/p>",
            "url": ""
        }, {
            "name": "Direcci\u00f3n de Bibliotecas, Archivos y Museos",
            "info": "Promover el conocimiento, la creaci\u00f3n, la recreaci\u00f3n y la apropiaci\u00f3n permanente del patrimonio cultural y la memoria colectiva del pa\u00eds, contribuyendo a los procesos de construcci\u00f3n de identidades y al desarrollo de la comunidad nacional y de su inserci\u00f3n en la comunidad internacional. Lo anterior implica rescatar, conservar, investigar y difundir el patrimonio nacional, considerado en su m\u00e1s amplio sentido.",
            "url": "http:\/\/www.dibam.gob.cl\/"
        }, {
            "name": "Consejo de Calificaci\u00f3n Cinematogr\u00e1fica",
            "info": "El Consejo de Calificaci\u00f3n Cinematogr\u00e1fica es un \u00f3rgano centralizado, dependiente del Ministerio de Educaci\u00f3n, creado bajo la Ley N\u00ba19.846 de 2002. Es el \u00f3rgano encargado de calificar las producciones cinematogr\u00e1ficas destinadas a la comercializaci\u00f3n, distribuci\u00f3n y exhibici\u00f3n p\u00fablica. La calificaci\u00f3n se realizar\u00e1 por edades, considerando el contenido de las producciones cinematogr\u00e1ficas y propendiendo siempre a la protecci\u00f3n de la infancia y la adolescencia, y a su desarrollo psicol\u00f3gico y social.",
            "url": "http:\/\/www.consejodecalificacioncinematografica.cl\/"
        }, {
            "name": "Comisi\u00f3n Nacional de Investigaci\u00f3n Cient\u00edfica y Tecnol\u00f3gica",
            "info": "<p>Impulsar la formaci\u00f3n de capital humano avanzado y promover, desarrollar y difundir la investigaci\u00f3n cient\u00edfica y tecnol\u00f3gica, en coherencia con la Estrategia Nacional de Innovaci\u00f3n, con el fin de contribuir al desarrollo econ\u00f3mico, social y cultural del pa\u00eds, mediante el apoyo de iniciativas tanto a nivel p\u00fablico como privado.<\/p>",
            "url": "http:\/\/www.conicyt.gob.cl "
        }, {
            "name": "Junta Nacional de Auxilio Escolar y Becas",
            "info": "Facilitar la incorporaci\u00f3n, permanencia y \u00e9xito en el sistema educacional de ni\u00f1as, ni\u00f1os y j\u00f3venes en condici\u00f3n de desventaja social, econ\u00f3mica, psicol\u00f3gica o biol\u00f3gica, entregando para ello productos y servicios integrales de calidad, que conteribuyen a la igualdad de oportunidades frente al proceso  educacional.",
            "url": "http:\/\/www.junaeb.cl\/"
        }, {
            "name": "Junta Nacional de Jardines Infantiles",
            "info": "Nuestro compromiso es brindar Educaci\u00f3n Parvularia inclusiva y de calidad a ni\u00f1os y ni\u00f1as, preferentemente menores de cuatro a\u00f1os en situaci\u00f3n de vulnerabilidad, a trav\u00e9s de salas cunas y jardines infantiles de excelencia administrados en forma directa y por terceros, garantiz\u00e1ndoles un desarrollo en igualdad de oportunidades y constituy\u00e9ndose en un apoyo a sus familias.",
            "url": "http:\/\/www.junji.cl"
        }, {
            "name": "Superintendencia de Educaci\u00f3n",
            "info": "",
            "url": "http:\/\/www.supereduc.cl"
        }, {
            "name": "Agencia de calidad de la educaci\u00f3n",
            "info": "",
            "url": "http:\/\/www.agenciaeducacion.cl"
        }, {
            "name": "Consejo de Monumentos Nacionales",
            "info": "",
            "url": ""
        }, {
            "name": "Comisi\u00f3n Nacional de Acreditaci\u00f3n",
            "info": "",
            "url": ""
        }]
    }, {
        "name": "Ministerio de Justicia",
        "children": [{
            "name": "Subsecretar\u00eda de Justicia",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Registro Civil e Identificaci\u00f3n",
            "info": "<p>\u201cSomos el servicio p\u00fablico que hace posible a las personas demostrar su identidad, acreditar hechos y actos significativos en sus vidas, proporcionando un servicio confiable, oportuno y cercano a la gente\u201d.<\/p>",
            "url": "http:\/\/www.registrocivil.gob.cl\/"
        }, {
            "name": "Servicio M\u00e9dico Legal",
            "info": "El Servicio M\u00e9dico Legal de acuerdo a su misi\u00f3n se compromete a implementar y mantener un Sistema de Gesti\u00f3n de la Calidad para satisfacer a sus clientes y la mejora continua de sus procesos.",
            "url": "http:\/\/www.sml.cl\/"
        }, {
            "name": "Servicio Nacional de Menores",
            "info": "Contribuir al desarrollo del sistema de protecci\u00f3n social de la infancia y adolescencia a trav\u00e9s del ejercicio de derechos y la reinserci\u00f3n social y\/o familiar de ni\u00f1os, ni\u00f1as y adolescentes vulnerados en sus derechos e infractores de ley, mediante una red de programas ejecutados directamente o por organismos colaboradores del Servicio.",
            "url": "http:\/\/www.sename.gob.cl\/"
        }, {
            "name": "Defensor\u00eda Penal P\u00fablica",
            "info": "La misi\u00f3n de la Defensor\u00eda Penal P\u00fablica es proporcionar defensa penal de alta calidad profesional a las personas que carezcan de abogado por cualquier circunstancia, velando por la igualdad ante la ley, por el debido proceso y actuando con profundo respeto por la dignidad humana de los representados.",
            "url": "http:\/\/www.dpp.gob.cl\/"
        }, {
            "name": "Gendarmer\u00eda de Chile",
            "info": "Contribuir a una sociedad m\u00e1s segura, garantizando el cumplimiento eficaz de la detenci\u00f3n preventiva y de las penas privativas o restrictivas de libertad a quienes los tribunales determinen, proporcionando a los afectados un trato digno, acorde a su calidad de persona humana y desarrollando programas de reinserci\u00f3n social que tiendan a disminuir las probabilidades de reincidencia delictual.",
            "url": "http:\/\/www.gendarmeria.gob.cl\/"
        }, {
            "name": "Superintendencia de Quiebras",
            "info": "",
            "url": ""
        }, {
            "name": "Corporaci\u00f3n de Asistencia Judicial Regi\u00f3n Metropolitana",
            "info": "",
            "url": ""
        }, {
            "name": "Corporaci\u00f3n de Asistencia Judicial Regi\u00f3n Valpara\u00edso",
            "info": "",
            "url": ""
        }, {
            "name": "Corporaci\u00f3n de Asistencia Judicial Regiones Tarapac\u00e1 y Antofagasta",
            "info": "",
            "url": ""
        }, {
            "name": "Corporaci\u00f3n de Asistencia Judicial Regi\u00f3n B\u00edo B\u00edo",
            "info": "",
            "url": ""
        }]
    }, {
        "name": "Ministerio del Trabajo y Previsi\u00f3n Social",
        "children": [{
            "name": "Subsecretar\u00eda del Trabajo",
            "info": "",
            "url": ""
        }, {
            "name": "Subsecretar\u00eda de Previsi\u00f3n Social",
            "info": "",
            "url": ""
        }, {
            "name": "Direcci\u00f3n del Trabajo",
            "info": "Velar por el cumplimiento de la legislaci\u00f3n laboral, fiscalizando, interpretando, orientando la correcta aplicaci\u00f3n de la normativa y promoviendo la capacidad de autorregulaci\u00f3n de las partes, en la b\u00fasqueda del desarrollo de relaciones de equilibrio entre empleadores y trabajadores.",
            "url": "http:\/\/www.dt.gob.cl\/"
        }, {
            "name": "Direcci\u00f3n General de Cr\u00e9dito Prendario",
            "info": "La DICREP es una instituci\u00f3n del Estado, de car\u00e1cter social y econ\u00f3mico que tiene por finalidad otorgar cr\u00e9dito prendario en forma simple y oportuna, resguardando las especies entregadas en garant\u00eda. Asimismo, act\u00faa en apoyo del Estado en remates fiscales y como \u00f3rgano auxiliar de la Justicia en la implementaci\u00f3n de las acciones que le son demandadas. Todo lo anterior, en el marco de procesos de gesti\u00f3n modernos, eficientes, transparentes y de clara orientaci\u00f3n al usuario.",
            "url": "http:\/\/www.dicrep.gob.cl\/"
        }, {
            "name": "Instituto de Previsi\u00f3n Social",
            "info": "El Instituto de Previsi\u00f3n Social administra beneficios previsionales y sociales, formulando estrategias que permitan mejorar la calidad del servicio, para garantizar el acceso a los derechos de seguridad social de las personas.",
            "url": "http:\/\/www.ips.gob.cl"
        }, {
            "name": "Instituto de Seguridad Laboral",
            "info": "Otorgar Seguridad y Salud Laboral a nuestros afiliados, a trav\u00e9s de acciones de prevenci\u00f3n destinadas a mejorar la gesti\u00f3n de riesgos, y la entrega de servicios de recuperaci\u00f3n de la salud y mitigaci\u00f3n econ\u00f3mica de los da\u00f1os derivados de los accidentes y enfermedades del trabajo en el marco de la responsabilidad social.",
            "url": "http:\/\/www.isl.gob.cl\/"
        }, {
            "name": "Servicio Nacional de Capacitaci\u00f3n y Empleo",
            "info": "Contribuir a la generaci\u00f3n de empleo, dinamizar el mercado laboral y desarrollar capital humano mediante la aplicaci\u00f3n de pol\u00edticas p\u00fablicas de fomento e intermediaci\u00f3n laboral y de capacitaci\u00f3n orientada a la empleabilidad y la productividad.",
            "url": "http:\/\/www.sence.gob.cl\/"
        }, {
            "name": "Superintendencia de Pensiones",
            "info": "La misi\u00f3n es regularizar y fiscalizar el sistema de pensiones en su conjunto: Pensiones solidarias, sistema antiguo y sistema de AFP.",
            "url": "http:\/\/www.spensiones.gob.cl"
        }, {
            "name": "Superintendencia de Seguridad Social",
            "info": "Regular y fiscalizar el cumplimiento de la normativa de Seguridad Social y garantizar el respeto de los derechos de las personas, especialmente de los trabajadores, pensionados y sus familias, resolviendo con calidad y oportunidad sus consultas, reclamos, denuncias y apelaciones, proponiendo las medidas tendientes al perfeccionamiento del sistema chileno de seguridad social.",
            "url": "http:\/\/www.suseso.gob.cl\/"
        }, {
            "name": "Comisi\u00f3n del Sistema Nacional de Certificaci\u00f3n de Competencias Laborales",
            "info": "",
            "url": ""
        }]
    }, {
        "name": "Ministerio de Obras P\u00fablicas",
        "children": [{
            "name": "Subsecretar\u00eda de Obras P\u00fablicas",
            "info": "",
            "url": ""
        }, {
            "name": "Direcci\u00f3n General de Obras P\u00fablicas",
            "info": "Dirigir, coordinar y supervigilar la gesti\u00f3n de obras y servicios de infraestructura p\u00fablica, regulando el sistema de contrataci\u00f3n de obras y consultor\u00edas, a fin de asegurar la competencia, transparencia y eficiencia en el cumplimiento de las pol\u00edticas y objetivos del MOP.",
            "url": "http:\/\/www.dgop.gob.cl\/"
        }, {
            "name": "Direcci\u00f3n de Contabilidad y Finanzas",
            "info": "",
            "url": ""
        }, {
            "name": "Direcci\u00f3n de Aeropuertos",
            "info": "",
            "url": ""
        }, {
            "name": "Direcci\u00f3n de Arquitectura",
            "info": "Proveer y conservar la edificaci\u00f3n p\u00fablica requerida, para favorecer la competitividad y el mejoramiento de la calidad de vida sde los habitantes, a trav\u00e9s de acciones realizadas por el MOP o por mandato de otras instituciones del Estado.",
            "url": "http:\/\/www.arquitecturamop.cl\/"
        }, {
            "name": "Direcci\u00f3n General de Aguas",
            "info": "Organismo del Estado encargado de promover la gesti\u00f3n y administraci\u00f3n del recurso h\u00eddrico en un marco de sustentabilidad, inter\u00e9s publico y asignaci\u00f3n eficiente; y proporcionar y difundir la informaci\u00f3n generada por su red hidrom\u00e9trica y la contenida en el Catastro P\u00fablico de Aguas, con el objeto de contribuir a la competitividad del pa\u00eds y mejorar la calidad de vida de las personas.",
            "url": "http:\/\/www.dga.gob.cl\/"
        }, {
            "name": "Direcci\u00f3n de Obras Hidr\u00e1ulicas",
            "info": "Proveer de servicios de Infraestructura Hidr\u00e1ulica que permitan el \u00f3ptimo aprovechamiento del agua y la protecci\u00f3n del territorio y de las personas, mediante un equipo de trabajo competente, con eficiencia en el uso de los recursos y la participaci\u00f3n de la ciudadan\u00eda en las distintas etapas de los proyectos, para contribuir al desarrollo sustentable del Pa\u00eds.",
            "url": "http:\/\/www.doh.gob.cl"
        }, {
            "name": "Direcci\u00f3n de Obras Portuarias",
            "info": "La Direcci\u00f3n de Obras Portuarias tiene como misi\u00f3n proveer a la ciudadan\u00eda servicios de infraestructura portuaria y costera, mar\u00edtima, fluvial y lacustre necesarios para el mejoramiento de la calidad de vida, el desarrollo socioecon\u00f3mico del pa\u00eds y su integraci\u00f3n f\u00edsica nacional e internacional.",
            "url": "http:\/\/www.dop.cl"
        }, {
            "name": "Direcci\u00f3n de Planeamiento ",
            "info": "Proponer a la autoridad ministerial las pol\u00edticas, planes y programas de desarrollo y recuperaci\u00f3n de servicios de infraestructura; para la conectividad, la protecci\u00f3n del territorio y las personas, la edificaci\u00f3n p\u00fablica y el aprovechamiento \u00f3ptimo y de manejo de los recursos h\u00eddricos; que orienten y establezcan las decisiones de inversi\u00f3n, bas\u00e1ndose en un conocimiento e informaci\u00f3n territorial y sectorial integrada, considerando los lineamientos estrat\u00e9gicos de la autoridad, realizando la gesti\u00f3n presupuestaria y el seguimiento de la inversi\u00f3n y planes, buscando con ello responder a las necesidades del desarrollo sustentable del pa\u00eds.",
            "url": "http:\/\/www.dirplan.cl"
        }, {
            "name": "Direcci\u00f3n de Vialidad",
            "info": "Mejorar la conectividad interna del territorio chileno y con los pa\u00edses de la regi\u00f3n, mediante la provisi\u00f3n de servicios de infraestructura vial, potenciando el desarrollo del pa\u00eds y su gente, resguardando su calidad de vida, promoviendo la equidad social, \u00e9tnica, de g\u00e9nero, resguardando la seguridad vial, dando sustentabilidad medioambiental e incorporando sistem\u00e1ticamente tecnolog\u00edas innovadoras en el \u00e1mbito vial y de transporte.",
            "url": "http:\/\/www.vialidad.cl"
        }, {
            "name": "Superintendencia de Servicios Sanitarios",
            "info": "izar a los clientes de los servicios de agua potable y saneamiento de las zonas urbanas del pa\u00eds, que \u00e9stos corresponden (en cantidad y calidad) a los ofrecidos, que su precio es justo y sostenible en el largo plazo; y asegurar a la comunidad, que el agua una vez utilizada ser\u00e1 tratada para ser devuelta a la naturaleza de forma compatible con un desarrollo sustentable. esta responsabilidad ser\u00e1 cumplida buscando promover la transparencia en el mercado, el autocontrol por parte de las empresas y desarrollando una actuaci\u00f3n eficiente.",
            "url": "http:\/\/www.siss.gob.cl"
        }, {
            "name": "Instituto Nacional de Hidr\u00e1ulica",
            "info": "Desarrollar  y aumentar los servicios en materia de ingenier\u00eda hidr\u00e1ulica para los sectores p\u00fablico y privado,  mediante la realizaci\u00f3n de estudios, proyectos e investigaciones, modelaci\u00f3n f\u00edsica y matem\u00e1tica, calibraciones, certificaciones y apoyo acad\u00e9mico, contribuyendo de esta manera al conocimiento cient\u00edfico en el \u00e1rea y, adem\u00e1s, mejorar la eficiencia, la seguridad y mantenci\u00f3n de la infraestructura, en concordancia y respeto con el medio ambiente y la calidad de vida de los habitantes.",
            "url": "http:\/\/www.inh.cl\/"
        }, {
            "name": "Fiscal\u00eda Ministerio de Obras P\u00fablicas",
            "info": "",
            "url": ""
        }, {
            "name": "Coordinaci\u00f3n de Concesiones de Obras P\u00fablicas",
            "info": "",
            "url": "http:\/\/www.concesiones.cl"
        }]
    }, {
        "name": "Ministerio de Transportes y Telecomunicaciones",
        "children": [{
            "name": "Subsecretar\u00eda de Transportes",
            "info": "<p>Incentivar el desarrollo de sistemas de transporte eficientes, seguros y sustentables ambientalmente, para mejorar la calidad de vida de los usuarios de dichos sistemas y promover la integraci&oacute;n territorial y el desarrollo econ&oacute;mico del pa&iacute;s.<\/p>",
            "url": "http:\/\/www.subtrans.gob.cl"
        }, {
            "name": "Subsecretar\u00eda de Telecomunicaciones",
            "info": "Promover el acceso equitativo a las telecomunicaciones, reduciendo la brecha digital mediante el otorgamiento de subsidios, concesiones y permisos; profundizar la competencia en el mercado, actualizando el marco normativo del sector y reformulando la institucionalidad, para asegurar la debida protecci\u00f3n de los usuarios, fiscalizando el cumplimiento de las normas, en el contexto del rol subsidiario del Estado, permitiendo mayor igualdad de oportunidades y el incremento de la calidad de vida para todos los habitantes del pa\u00eds.",
            "url": "http:\/\/www.subtel.gob.cl"
        }, {
            "name": "Junta de Aeron\u00e1utica Civil",
            "info": "La misi\u00f3n institucional de la JAC consiste en ejercer la direcci\u00f3n superior de la aviaci\u00f3n civil en Chile. Esto implica fijar las grandes directrices del quehacer aeron\u00e1utico y administrar la pol\u00edtica a\u00e9rea, impulsando pol\u00edticas de apertura en el tr\u00e1fico a\u00e9reo entre Chile y otros pa\u00edses, y promoviendo el desarrollo del transporte a\u00e9reo comercial nacional e internacional a fin de propender a la mayor cantidad de servicios a\u00e9reos de la mejor calidad, eficiencia y al menor precio.",
            "url": "http:\/\/www.jac-chile.cl"
        }, {
            "name": "Centro de Control y Certificaci\u00f3n Vehicular",
            "info": "Su campo de acci\u00f3n se circunscribe al uso de gas en veh\u00edculos motorizados, homologaci\u00f3n de veh\u00edculos y motos, certificaci\u00f3n de veh\u00edculos pesados y la incorporaci\u00f3n de nuevas tecnolog\u00edas aplicadas al transporte.",
            "url": "http:\/\/www.subtrans.gob.cl"
        }, {
            "name": "Unidad Operativa de Control de Tr\u00e1nsito",
            "info": "Este sistema centralizado permite coordinar, supervisar y monitorear remotamente la operaci\u00f3n de casi la totalidad de los sem\u00e1foros existentes en la ciudad.",
            "url": "http:\/\/www.uoct.cl"
        }]
    }, {
        "name": "Ministerio de Salud",
        "children": [{
            "name": "Subsecretar\u00eda de Salud P\u00fablica",
            "info": "La misi\u00f3n institucional que el Ministerio de Salud se ha dado para este per\u00edodo, busca contribuir a elevar el nivel de salud de la poblaci\u00f3n; desarrollar arm\u00f3nicamente los sistemas de salud, centrados en las personas; fortalecer el control de los factores que puedan afectar la salud y reforzar la gesti\u00f3n de la red nacional de atenci\u00f3n. Todo ello para acoger oportunamente las necesidades de las personas, familias y comunidades, con la obligaci\u00f3n de rendir cuentas a la ciudadan\u00eda y promover la participaci\u00f3n de las mismas en el ejercicio de sus derechos y sus deberes.",
            "url": "http:\/\/www.minsal.cl"
        }, {
            "name": "Subsecretar\u00eda de Redes Asistenciales",
            "info": "",
            "url": ""
        }, {
            "name": "Central de Abastecimiento del Sistema Nacional de Servicios de Salud",
            "info": "",
            "url": ""
        }, {
            "name": "Fondo Nacional de Salud",
            "info": "<p>Ser un Seguro orientado a satisfacer necesidades de salud de sus asegurados, entregando cobertura financiera de las prestaciones de salud en el sector p\u00fablico y privado, y resguardando un eficiente manejo financiero del sector p\u00fablico de salud.<\/p>",
            "url": "http:\/\/www.fonasa.gob.cl\/"
        }, {
            "name": "Instituto de Salud P\u00fablica",
            "info": "Contribuir al mejoramiento de la salud de la poblaci\u00f3n, garantizando la calidad de bienes y servicios, a trav\u00e9s del fortalecimiento de la referencia, la fiscalizaci\u00f3n y la normalizaci\u00f3n.",
            "url": "http:\/\/www.ispch.cl\/"
        }, {
            "name": "Superintendencia de Salud",
            "info": "<p>La Misi\u00f3n de la Superintendencia de Salud es Regular y fiscalizar a los seguros y prestadores de salud del \u00e1mbito p\u00fablico y privado, resguardando los derechos de las personas, promoviendo la calidad y seguridad en las atenciones de salud.<\/p>",
            "url": "http:\/\/www.supersalud.gob.cl"
        }, {
            "name": "Servicio de Salud Metropolitano Central",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Metropolitano Norte",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Metropolitano Occidente",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Metropolitano Oriente",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Metropolitano Sur",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Metropolitano Sur Oriente",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Padre Hurtado",
            "info": "",
            "url": ""
        }, {
            "name": "Centro de Referencia de Salud de Pe\u00f1alol\u00e9n Cordillera Oriente",
            "info": "",
            "url": ""
        }, {
            "name": "Centro de Referencia de Salud de Maip\u00fa",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Arica",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Iquique",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Antofagasta",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Atacama",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Coquimbo",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Aconcagua",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Valpara\u00edso - San Antonio",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Vi\u00f1a Del Mar - Quillota",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud O\u00b4Higgins",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Maule",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud \u00d1uble",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Concepci\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Talcahuano",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud B\u00edo B\u00edo",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Arauco",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Araucan\u00eda Norte",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Araucan\u00eda Sur",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Valdivia",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Osorno",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud de Chilo\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Ays\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud del Reloncav\u00ed",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio de Salud Magallanes",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de Arica y Parinacota",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de Tarapac\u00e1",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de Antofagasta",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de Atacama",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de Coquimbo",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de Valpara\u00edso",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial Metropolitano de Santiago",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de O\u00b4Higgins",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial del Maule",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial del B\u00edo B\u00edo",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de La Araucan\u00eda",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de Los R\u00edos",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de Los Lagos",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de Ays\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Secretar\u00eda Regional Ministerial de Magallanes y Ant\u00e1rtica Chilena",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de San Camilo",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Leonardo Guzm\u00e1n de Antofagasta",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Victoria",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Mauricio heyermann de Angol",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Juan No\u00e9 de Arica",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Regional de Coyhaique",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital V\u00edctor R\u00edos Ruiz de Los Angeles",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Dr. Augusto Riffart de Castro",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital San Jose de Coronel",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Lota",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Guillermo Grant Benavente de Concepci\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Ovalle",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital La Serena",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital San Pablo de Coquimbo",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Ernesto Torres de Iquique",
            "info": "",
            "url": ""
        }, {
            "name": "HUAP Posta central",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital San Borja Arriar\u00e1n",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital San Jos\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Roberto del R\u00edo",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital F\u00e9lix Bulnes",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Melipilla",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital San Juan de Dios",
            "info": "",
            "url": ""
        }, {
            "name": "Instituto Pedro Aguirre Cerda",
            "info": "",
            "url": ""
        }, {
            "name": "Instituto de Neurocirug\u00eda",
            "info": "",
            "url": ""
        }, {
            "name": "Instituto Nacional de Geriatr\u00eda",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Del Salvador",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Barros Luco ",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital S\u00f3tero del R\u00edo",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Lautaro Navarro de Punta Arenas",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Curic\u00f3",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Linares",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Regional de Talca",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de San Carlos",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital San Juan de Dios de San Fernando",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Regional de Rancagua",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Osorno",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Puerto Montt",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Tom\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Las Higueras",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Base de Valdivia",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Claudio Vicu\u00f1a de San Antonio",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Carlos Van B\u00fcren",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Eduardo Pereira de Valpara\u00edso",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital de Quilpu\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Gustavo Fricke",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital San Mart\u00edn de Quillota",
            "info": "",
            "url": ""
        }, {
            "name": "Instituto Psiqui\u00e1trico",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital San Juan de Dios de Los Andes",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Exequiel Gonz\u00e1lez",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital El Pino",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Herminda Martin",
            "info": "",
            "url": ""
        }, {
            "name": "Instituto Nacional del T\u00f3rax",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Luis Tisn\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Instituto Traumatol\u00f3gico",
            "info": "",
            "url": ""
        }, {
            "name": "Instituto Nacional del C\u00e1ncer",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Luis Calvo Mackenna",
            "info": "",
            "url": ""
        }, {
            "name": "Hospital Dr. Hern\u00e1n Henr\u00edquez Aravena de Temuco",
            "info": "",
            "url": ""
        }, {
            "name": "Autoridad Sanitaria",
            "info": "La autoridad regional debe fiscalizar y sancionar disposiciones del C\u00f3digo Sanitario y otras normativas. Asimismo, la Seremi de Salud fiscaliza materias como higiene y seguridad del ambiente y de los lugares de trabajo; alimentos; laboratorios; farmacias; inhumaciones; exhumaciones y traslado de cad\u00e1veres.",
            "url": ""
        }, {
            "name": "Comisi\u00f3n de Medicina Preventiva e Invalidez",
            "info": "Velar, de acuerdo a la ley, por el cumplimiento de las normas m\u00e9dico legales en materias de seguridad social.\r\nActuar como garante de la fe p\u00fablica en la certificaci\u00f3n de estados de salud y en la gesti\u00f3n de procesos t\u00e9cnicos y administrativos.\r\nGarantizar en forma eficaz el acceso a los beneficios de la protecci\u00f3n social en salud.",
            "url": "http:\/\/www.infocompin.cl\/"
        }]
    }, {
        "name": "Ministerio de Vivienda y Urbanismo",
        "children": [{
            "name": "Subsecretar\u00eda de Vivienda y Urbanismo",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n de Tarapac\u00e1",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n de Antofagasta",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n de Atacama",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n de Coquimbo",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n de Valpara\u00edso",
            "info": "Materializar los planes y programas derivados de la Pol\u00edtica Urbano Habitacional del Ministerio de Vivienda y Urbanismo, desarrollando proyectos y construyendo viviendas de calidad, barrios, y ciudades integradas, seguras y sustentables, que permitan a las personas, principalmente las m\u00e1s vulnerables, mejorar su calidad de vida, la de sus familias y entorno.",
            "url": "http:\/\/www.serviuvalpo.cl\/"
        }, {
            "name": "SERVIU Regi\u00f3n Metropolitana de Santiago",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n del Libertador Bernardo O'Higgins",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n del Maule",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n del B\u00edo B\u00edo",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n de la Araucan\u00eda",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n de los Lagos",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n de Ays\u00e9n del General Carlos Ib\u00e1\u00f1ez del Campo",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n de Magallanes y la Ant\u00e1rtica Chilena",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Regi\u00f3n de Los R\u00edos",
            "info": "",
            "url": ""
        }, {
            "name": "SERVIU Arica y Parinacota",
            "info": "",
            "url": ""
        }, {
            "name": "Parque Metropolitano de Santiago",
            "info": "Mejorar la calidad de vida de las personas, proporcionando espacios urbanos de integraci\u00f3n social, promoviendo para y con la ciudadan\u00eda la educaci\u00f3n en la protecci\u00f3n del medio ambiente y el esparcimiento en contacto con la naturaleza dando cabida al arte, la cultura y el deporte.",
            "url": "http:\/\/www.parquemet.cl\/"
        }]
    }, {
        "name": "Ministerio de Bienes Nacionales",
        "children": [{
            "name": "Subsecretar\u00eda de Bienes Nacionales",
            "info": "",
            "url": ""
        }]
    }, {
        "name": "Ministerio de Agricultura",
        "children": [{
            "name": "Subsecretar\u00eda de Agricultura",
            "info": "",
            "url": ""
        }, {
            "name": "Comisi\u00f3n Nacional de Riego",
            "info": "Asegurar el incremento y mejoramiento de la superficie regada del pa\u00eds mediante la formulaci\u00f3n de la pol\u00edtica, estudios y programas y proyectos que aporten al mejoramiento de la competitividad de los agricultores\/as y las organizaciones de regantes.",
            "url": "http:\/\/www.chileriego.cl\/"
        }, {
            "name": "Instituto de Desarrollo Agropecuario",
            "info": "Generar capacidades y apoyar con acciones de fomento el desarrollo productivo sustentable de la peque\u00f1a agricultura.",
            "url": "http:\/\/www.indap.gob.cl"
        }, {
            "name": "Oficinas de Estudios y Pol\u00edticas Agrarias",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio Agr\u00edcola y Ganadero",
            "info": "Proteger y mejorar los recursos productivos silvoagropecuarios y los recursos naturales renovables del pa\u00eds, la inocuidad de insumos y alimentos agropecuarios, para apoyar el desarrollo sustentable y competitivo del sector silvoagropecuario.",
            "url": "http:\/\/www.sag.cl"
        }]
    }, {
        "name": "Ministerio de Miner\u00eda",
        "children": [{
            "name": "Subsecretar\u00eda de Miner\u00eda",
            "info": "",
            "url": ""
        }, {
            "name": "Comisi\u00f3n Chilena del Cobre",
            "info": "Asesorar al Gobierno en la elaboraci\u00f3n, implementaci\u00f3n y fiscalizaci\u00f3n de pol\u00edticas, estrategias y acciones que contribuyan al desarrollo sustentable del sector minero nacional y a fortalecer el aporte de \u00e9ste al resto de la econom\u00eda. Asimismo, resguardar los intereses del Estado en sus empresas mineras, fiscalizando y evaluando su gesti\u00f3n e inversiones.",
            "url": "http:\/\/www.cochilco.cl\/"
        }, {
            "name": "Servicio Nacional de Geolog\u00eda y Miner\u00eda",
            "info": "Nuestra misi\u00f3n es cumplir el mandato del Estado en materias de geolog\u00eda y miner\u00eda, con calidad, mediante un equipo humano profesional y altamente especializado, contribuyendo al desarrollo sustentable del pa\u00eds.",
            "url": "http:\/\/www.sernageomin.cl\/"
        }]
    }, {
        "name": "Servicio Nacional de la Mujer",
        "children": [{
            "name": "Servicio Nacional de la Mujer",
            "info": "Su misi\u00f3n es dise\u00f1ar, proponer y coordinar pol\u00edticas, planes, medidas y reformas legales conducentes a la igualdad de derechos y oportunidades entre hombres y mujeres; y a disminuir pr\u00e1cticas discriminatorias en el proceso de desarrollo pol\u00edtico, social, econ\u00f3mico y cultural del pa\u00eds.",
            "url": "http:\/\/www.sernam.cl\/"
        }]
    }, {
        "name": "Ministerio de Energ\u00eda",
        "children": [{
            "name": "Comisi\u00f3n Nacional de Energ\u00eda",
            "info": "",
            "url": ""
        }, {
            "name": "Subsecretar\u00eda de Energ\u00eda",
            "info": "",
            "url": ""
        }, {
            "name": "Comisi\u00f3n Chilena de Energ\u00eda Nuclear",
            "info": "<p>Contribuir al conocimiento en ciencia y tecnolog&iacute;a, al bienestar y seguridad de las personas y a la protecci&oacute;n del medio ambiente, para el sector p&uacute;blico y privado, en las &aacute;reas de salud, industria y educaci&oacute;n, a trav&eacute;s de la investigaci&oacute;n, desarrollo y aplicaciones pac&iacute;ficas de la energ&iacute;a nuclear, as&iacute; como su regulaci&oacute;n, control y fiscalizaci&oacute;n.<\/p>",
            "url": "http:\/\/www.cchen.cl"
        }, {
            "name": "Superintendencia de Electricidad y Combustibles",
            "info": "De acuerdo a lo que se refiere la Ley Org\u00e1nica Constitucional de la Superintendencia de Electricidad y Combustibles tiene por misi\u00f3n vigilar la adecuada operaci\u00f3n de los servicios de electricidad, gas y combustibles, en t\u00e9rminos de su seguridad, calidad y precio.\r\nConsecuentemente con su misi\u00f3n, y en torno a la \u00faltima modificaci\u00f3n realizada a la Ley N\u00ba 18.410 en Mayo de 2005, el objeto de la SEC ser\u00e1 fiscalizar y supervigilar el cumplimiento de las disposiciones legales y reglamentarias, y normas t\u00e9cnicas sobre generaci\u00f3n, producci\u00f3n, almacenamiento, transporte y distribuci\u00f3n de combustibles l\u00edquidos, gas y electricidad, para verificar que la calidad de los servicios que se presten a los usuarios sea la se\u00f1alada en dichas disposiciones y normas t\u00e9cnicas, y que las operaciones y el uso de los recursos energ\u00e9ticos no constituyan peligro para las personas o sus cosas.",
            "url": "http:\/\/www.sec.cl"
        }]
    }, {
        "name": "Consejo Nacional de la Cultura y las Artes",
        "children": [{
            "name": "Consejo Nacional de la Cultura y las Artes",
            "info": "<p>El Consejo Nacional de la Cultura y las Artes es el &oacute;rgano del Estado encargado de implementar las pol&iacute;ticas p&uacute;blicas para el desarrollo cultural. Nuestra misi&oacute;n es promover un desarrollo cultural arm&oacute;nico, pluralista y equitativo entre los habitantes del pa&iacute;s, a trav&eacute;s del fomento y difusi&oacute;n de la creaci&oacute;n art&iacute;stica nacional; as&iacute; como de la preservaci&oacute;n, promoci&oacute;n y difusi&oacute;n del patrimonio cultural chileno, adoptando iniciativas p&uacute;blicas que estimulen una participaci&oacute;n activa de la ciudadan&iacute;a en el logro de tales fines.<\/p>",
            "url": "http:\/\/www.cultura.gob.cl\/"
        }]
    }, {
        "name": "Ministerio del Medio Ambiente",
        "children": [{
            "name": "Comisi\u00f3n Nacional del Medio Ambiente",
            "info": "",
            "url": ""
        }, {
            "name": "Subsecretar\u00eda del Medio Ambiente",
            "info": "",
            "url": ""
        }, {
            "name": "Superintendencia del Medio Ambiente",
            "info": "",
            "url": ""
        }, {
            "name": "Servicio Evaluaci\u00f3n Ambiental",
            "info": "La misi\u00f3n del Servicio de Evaluaci\u00f3n Ambiental es resguardar el medio ambiente de manera responsable y eficiente, protegiendo siempre a la ciudadan\u00eda y los recursos naturales; adem\u00e1s de asegurar el uso sostenible, responsable, racional y \u00e9tico de los recursos naturales y contribuir al desarrollo integral, social, econ\u00f3mico y cultural de nuestro pa\u00eds.",
            "url": "http:\/\/www.sea.gob.cl\/"
        }]
    }, {
        "name": "Consejo de Defensa del Estado",
        "children": [{
            "name": "Consejo de Defensa del Estado",
            "info": "<p>Defender, representar y asesorar judicial y extrajudicialmente al Estado, en materias de car\u00e1cter patrimonial y no patrimonial, a trav\u00e9s del ejercicio de las acciones y defensas judiciales que correspondan, en beneficio de los intereses del Estado. Adem\u00e1s, otorgar el servicio de mediaci\u00f3n establecido en la Ley No. 19.966, a usuarios y prestadores del sistema p\u00fablico de salud, a trav\u00e9s de la designaci\u00f3n de mediadores.<\/p>",
            "url": "http:\/\/www.cde.cl"
        }]
    }, {
        "name": "Fundaciones",
        "children": [{
            "name": "Fundaci\u00f3n Integra",
            "info": "",
            "url": ""
        }, {
            "name": "Fundaci\u00f3n Tiempos Nuevos (MIM)",
            "info": "",
            "url": ""
        }, {
            "name": "Fundaci\u00f3n para la Promoci\u00f3n y Desarrollo de la Mujer (PROdeMU)",
            "info": "",
            "url": ""
        }, {
            "name": "Fundaci\u00f3n Artesan\u00edas de Chile",
            "info": "",
            "url": ""
        }, {
            "name": "Fundaci\u00f3n de la Familia",
            "info": "",
            "url": ""
        }]
    }, {
        "name": "Municipios",
        "children": [{
            "name": "Municipalidad de Algarrobo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Alhu\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Alto Biob\u00edo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Alto del Carmen",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Alto Hospicio",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Ancud",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Andacollo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Angol",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Antofagasta",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Antuco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Arauco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Arica",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Aysen",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Buin",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Bulnes",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cabildo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cabo de Hornos y Ant\u00e1rtica",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cabrero",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Calama",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Calbuco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Caldera",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Calera de Tango",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Calle Larga",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Camarones",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cami\u00f1a",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Canela",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Ca\u00f1ete",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Carahue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cartagena",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Casablanca",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Castro",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Catemu",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cauquenes",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cerrillos",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cerro Navia",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Chait\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Chanco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cha\u00f1aral",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Ch\u00e9pica",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Chiguayante",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Chile Chico",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Chill\u00e1n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Chill\u00e1n Viejo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Chimbarongo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cholchol",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Chonchi",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cisnes",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cobquecura",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cocham\u00f3",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cochrane",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Codegua",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Coelemu",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Coihueco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Coinco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Colb\u00fan",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Colchane",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Colina",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Collipulli",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Coltauco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Combarbal\u00e1",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Concepci\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Conchal\u00ed",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Conc\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Constituci\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Contulmo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Copiap\u00f3",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Coquimbo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Coronel",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Corral",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Coyhaique",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Cunco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Curacaut\u00edn",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Curacav\u00ed",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Curaco de V\u00e9lez",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Curanilahue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Curarrehue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Curepto",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Curic\u00f3",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Dalcahue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Diego de Almagro",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Do\u00f1ihue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de El Bosque",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de El Carmen",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de El Monte",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de El Quisco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de El Tabo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Empedrado",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Ercilla",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Estaci\u00f3n Central",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Florida",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Freire",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Freirina",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Fresia",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Frutillar",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Futaleuf\u00fa",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Futrono",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Galvarino",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de General Lagos",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Gorbea",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Graneros",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Guaitecas",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Hijuelas",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Hualaihu\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Huala\u00f1\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Hualp\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Hualqui",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Huara",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Huasco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Huechuraba",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Illapel",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Independencia",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Iquique",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Isla de Maipo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Isla de Pascua",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Juan Fern\u00e1ndez",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Calera",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Cisterna",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Cruz",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Estrella",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Florida",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Granja",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Higuera",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Ligua",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Pintana",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Reina",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Serena",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de La Uni\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lago Ranco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lago Verde",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Laguna Blanca",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Laja",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lampa",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lanco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Las Cabras",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Las Condes",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lautaro",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lebu",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Licant\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Limache",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Linares",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Litueche",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Llanquihue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Llay Llay",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lo Barnechea",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lo Espejo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lo Prado",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lolol",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Loncoche",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Longav\u00ed",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lonquimay",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Los Alamos",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Los Andes",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Los Angeles",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Los Lagos",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Los Muermos",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Los Sauces",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Los Vilos",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lota",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Lumaco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Machal\u00ed",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Macul",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de M\u00e1fil",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Maip\u00fa",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Malloa",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Marchihue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Mar\u00eda Elena",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Mar\u00eda Pinto",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Mariquina",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Maule",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Maull\u00edn",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Mejillones",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Melipeuco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Melipilla",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Molina",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Monte Patria",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Mostazal",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Mulch\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Nacimiento",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Nancagua",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Navidad",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Negrete",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Ninhue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Nogales",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Nueva Imperial",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de \u00d1iqu\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de \u00d1u\u00f1oa",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de O'higgins",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Olivar",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Ollag\u00fce",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Olmu\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Osorno",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Ovalle",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Padre Hurtado",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Padre Las Casas",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Paiguano",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Paillaco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Paine",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Palena",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Palmilla",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Panguipulli",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Panquehue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Papudo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Paredones",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Parral",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pedro Aguirre Cerda",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pelarco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pelluhue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pemuco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pencahue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Penco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pe\u00f1aflor",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pe\u00f1alol\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Peralillo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Perquenco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Petorca",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Peumo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pica",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pichidegua",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pichilemu",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pinto",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pirque",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pitrufqu\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Placilla",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Portezuelo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Porvenir",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pozo Almonte",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Primavera",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Providencia",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Puchuncav\u00ed",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Puc\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pudahuel",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Puente Alto",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Puerto Montt",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Puerto Natales",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Puerto Octay",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Puerto Varas",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pumanque",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Punitaqui",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Punta Arenas",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Puqueld\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Pur\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Purranque",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Putaendo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Putre",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Puyehue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Queil\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quell\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quemchi",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quilaco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quilicura",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quilleco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quill\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quillota",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quilpu\u00e9",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quinchao",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quinta de Tilcoco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quinta Normal",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quintero",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Quirihue",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Rancagua",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de R\u00e1nquil",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Rauco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Recoleta",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Renaico",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Renca",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Rengo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Requ\u00ednoa",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Retiro",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Rinconada",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Rio Bueno",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de R\u00edo Claro",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de R\u00edo Hurtado",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de R\u00edo Ib\u00e1\u00f1ez",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de R\u00edo Negro",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de R\u00edo Verde",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Romeral",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Saavedra",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Sagrada Familia",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Salamanca",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Antonio",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Bernardo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Carlos",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Clemente",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Esteban",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Fabi\u00e1n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Felipe",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Fernando",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Gregorio",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Ignacio",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Javier",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Joaqu\u00edn",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Jos\u00e9 de Maipo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Juan de la Costa",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Miguel",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Nicol\u00e1s",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Pablo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Pedro",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Pedro de Atacama",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Pedro De La Paz",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Rafael",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Ram\u00f3n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Rosendo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de San Vicente de Tagua Tagua",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Santa B\u00e1rbara",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Santa Cruz",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Santa Juana",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Santa Mar\u00eda",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Santiago",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Santo Domingo",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Sierra Gorda",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Talagante",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Talca",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Talcahuano",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Taltal",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Temuco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Teno",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Teodoro Schmidt",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Tierra Amarilla",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Tiltil",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Timaukel",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Tir\u00faa",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Tocopilla",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Tolt\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Tome",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Torres del Paine",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Tortel",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Traigu\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Treguaco",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Tucapel",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Valdivia",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Vallenar",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Valpara\u00edso",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Vichuqu\u00e9n",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Victoria",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Vicu\u00f1a",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Vilc\u00fan",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Villa Alegre",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Villa Alemana",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Villarrica",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Vi\u00f1a del Mar",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Vitacura",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Yerbas Buenas",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Yumbel",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Yungay",
            "info": "",
            "url": ""
        }, {
            "name": "Municipalidad de Zapallar",
            "info": "",
            "url": ""
        }]
    }]
};
#print elbigjson
elements = elbigjson["children"]
for key in elements:
    newJs = key["children"]
    #print "a"
    elgran =  key["name"]
    #print "aa"
    for asd in newJs:
        print elgran +"@"+ asd["name"].decode('utf-8')

