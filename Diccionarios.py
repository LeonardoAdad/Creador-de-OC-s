import random
import time 

# ── Diccionarios ──
escenarios = {
    "Fantasía": [
        "Salon del trono", "montaña misteriosa", "Bosque Mágico", "Aldea", "Templo antiguo",
        "Taberna", "Caverna de dragones", "Isla Perdida", "Establo de caballos", "Escuela mágica"
    ],
    "Cyberpunk": [
        "Bar clandestino", "Base espacial", "Ciudad futurista",
        "Barrios Bajos", "Nave espacial", "Edificio corporativo",
        "Bar lujoso", "Ciberespacio", "Ciudad subterránea", "Batalla de por territorio"
    ],
    "Actualidad": [
        "El rancho", "Puestos callejeros", "Centro de la ciudad", "Cafetería",
        "Oficina", "Barrio", "Calle Transitada", "Transporte público",
        "Bar", "Parque"
    ]
}

profesiones = {
    "Fantasía": [
        "Mago", "Caballero", "Nigromante", "Arquero", "Asesino",
        "Realeza", "Plebeyo", "Bardo", "Arquero", "Bufon"
    ],
    "Cyberpunk": [
        "Hacker/Netrunner", "Pandillero", "Nomada", "Fixer", "Corporativo",
        "Policía", "Político", "Rockerboy", "Ingeniero", "Sicario"
    ],
    "Actualidad": [
        "Doctor", "Estudiante", "Chofer", "Bartender", "Oficinista",
        "Chef", "Artista", "Cholo", "Programador", "Abogado", "Profesor"
    ]
}

Razas = {
    "Humano", "Elfo", "Enano", "Orco", "Goblin", "Tifling", "Celestial", "Draconido", "Mediano", "Semielfo"
}

tematica = {
    "Fantasía", "Cyberpunk", "Actualidad"
}

genero = {
    "Femenino", "Masculino", "No binario"
}

caracteristicas_fisicas = {
    "Complexión": [
        "Robusta", "Esbelta", "Media", "Definida"
    ],
    "Cabello": [
        "Largo", "Medio", "Corto", "Pelón"
    ],
    "Color de piel": [
        "Afro", "Moreno", "Blanco", "Olivo", "Albino", "Almendrado", "Rojo", "Verde", "Morado", "Azul", "Amarillo", "Rosa"
    ]
}

colores_principales = {
    "Fríos", "Calidos", "Pasteles"
}

# Acciones por profesión y escenario para las descripciones finales
Acciones_por_profesion_y_escenario = {
    "mago": {
        "salon del trono": "Lanzando un hechizo que rodea toda la sala del trono.",
        "montaña misteriosa": "Entre los árboles camina con calma mientras que con su cetro mágico ilumina su camino en un camino oscuro.",
        "aldea": "En una calle medianamente transitada, atiende un puesto de pociones.",
        "templo antiguo": "Caminando en el centro del templo hacia el altar, con su magia rodeándolo.",
        "taberna": "Tranquilo, sentado en la barra mientras bebe una cerveza desde un tarro de cristal.",
        "caverna de dragones": "Entrando a una gran cueva iluminando la oscuridad densa con su cetro mágico.",
        "isla perdida": "Usa sus poderes para crear un portal que lo lleve a casa.",
        "establo de caballos": "Alimenta a los caballos.",
        "escuela mágica": "Siendo el maestro dando clases a aspirantes a magos en una gran aula de clases."
    },
    "caballero": {
        "salon del trono": "Parado custodiando una gran puerta de madera.",
        "montaña misteriosa": "Explorando el bosque, vigilante de sus alrededores, lleva su espada en mano.",
        "aldea": "Haciendo patrulla en una calle transitada, observando a los aldeanos.",
        "templo antiguo": "De rodillas en el altar con su espada entre sus manos.",
        "taberna": "Intentando relajarse, sentado en una mesa apartada con solo una cerveza frente a él y sin su casco puesto.",
        "caverna de dragones": "Explorando la caverna con su espada en mano y viéndose alerta mientras un dragón lo acecha en las sombras.",
        "isla perdida": "Confundido, mirando su entorno mientras busca su espada y su casco.",
        "establo de caballos": "Montando un caballo con armadura, preparándose para salir.",
        "escuela mágica": "Custodiando la oficina del director de la escuela."
    },
    "nigromante": {
        "salon del trono": "Leyendo su libro de hechizos frente a los reyes, con una bruma oscura inundando el salón.",
        "montaña misteriosa": "En un claro entre los árboles, está parado en el centro de un círculo con runas y velas mientras mira al cielo.",
        "aldea": "Parado en un callejón, observa a las personas pasar mientras se mantiene en las sombras.",
        "templo antiguo": "Realizando un ritual con runas en el altar del templo, con niebla a su alrededor.",
        "taberna": "En una mesa apartada, hablando con sus posibles clientes hace una demostración de sus poderes.",
        "caverna de dragones": "Camina hacia la oscuridad de la caverna con destellos de magia a su alrededor, carga un libro grueso y antiguo.",
        "isla perdida": "Dibuja runas en la arena hasta el cansancio.",
        "establo de caballos": "Cepilla un caballo de pelaje negro.",
        "escuela mágica": "Dando clases de nigromancia en un gran aula de clases sumergida en oscuridad."
    },
    "asesino": {
        "salon del trono": "Acechando desde las sombras.",
        "montaña misteriosa": "Se oculta en un refugio entre los árboles.",
        "aldea": "Camina misterioso entre todas las personas, mirando a su objetivo fijamente.",
        "templo antiguo": "Sentado en una banca mientras afila su cuchillo.",
        "taberna": "Sentado con despreocupación en la barra con un tarro en su mano mientras habla con el cantinero.",
        "caverna de dragones": "Escabulléndose en la caverna, atento a sus alrededores como si buscara esconderse ahí dentro.",
        "isla perdida": "Cortando lianas para construir un barco.",
        "establo de caballos": "Observando el establo desde lejos, pareciendo que busca a alguien mientras sostiene su cuchillo.",
        "escuela mágica": "Colándose en la oficina del director de la escuela."
    },
    "realeza": {
        "salon del trono": "Dictando órdenes sentado en el trono en soledad.",
        "montaña misteriosa": "Observando desde la punta de la montaña empoderar a sus alrededores.",
        "aldea": "Recorriendo el lugar con escolta mientras los demás se inclinan ante él.",
        "templo antiguo": "Ora con reverencia en busca de sabiduría.",
        "taberna": "Sentado lejos de los demás bebiendo un tarro de cerveza.",
        "caverna de dragones": "Dando órdenes de atacar a sus soldados.",
        "isla perdida": "Reclama la nueva isla como suya usando su ropa como bandera.",
        "establo de caballos": "Admirando a todos sus caballos.",
        "escuela mágica": "Leyendo libros mientras mezcla en un caldero."
    },
    "plebeyo": {
        "salon del trono": "Espera a la llegada del rey junto a más plebeyos.",
        "montaña misteriosa": "Escalando con fuerza con miedo a soltarse.",
        "aldea": "Trabajando con la ganadería.",
        "templo antiguo": "Rezando por que pase un milagro.",
        "taberna": "Bebiendo acompañado de compañeros.",
        "caverna de dragones": "Escondido detrás de una piedra grande rezando por no ser comido.",
        "isla perdida": "Buscando recoger recursos para sobrevivir.",
        "establo de caballos": "Bañando y alimentando a los caballos.",
        "escuela mágica": "Observa asombrado alrededor."
    },
    "bardo": {
        "salon del trono": "Cantando alabanzas para entretener al rey.",
        "montaña misteriosa": "Componiendo música en la punta de la montaña.",
        "aldea": "Animando a los plebeyos con su música.",
        "templo antiguo": "Entonando música más tranquila.",
        "taberna": "Tocando melodías para ganar monedas entre los borrachos.",
        "caverna de dragones": "Tocando música haciendo que los dragones se duerman.",
        "isla perdida": "Creando canciones para entretenerse en la orilla de la isla.",
        "establo de caballos": "Improvisando versos para los caballos.",
        "escuela mágica": "Canta versos haciendo hechizos mágicos."
    },
    "arquero": {
        "salon del trono": "Vigilando en las afueras de la entrada del castillo.",
        "montaña misteriosa": "Rastreando huellas en busca de monstruos.",
        "aldea": "Protegiendo a la aldea y los habitantes.",
        "templo antiguo": "Explorando ruinas con cautela.",
        "taberna": "Se queda alerta de posibles amenazas.",
        "caverna de dragones": "Apunta dentro de la caverna listo para disparar.",
        "isla perdida": "Cazando animales para sobrevivir.",
        "establo de caballos": "Practicando su puntería en área libre.",
        "escuela mágica": "Aprendiendo a hacer encantamientos puestos en sus flechas."
    },
    "bufon": {
        "salon del trono": "Haciendo reír al rey con sus bromas.",
        "montaña misteriosa": "Paseando por la montaña dando saltos felices.",
        "aldea": "Merodeando en la aldea haciendo reír a los niños.",
        "templo antiguo": "Rompiendo la seriedad con sus bromas.",
        "taberna": "Riendo y contando chistes con los borrachos de la taberna.",
        "caverna de dragones": "Intentando distraer al monstruo estando ligeramente nervioso.",
        "isla perdida": "Crea juegos absurdos para entretenerse.",
        "establo de caballos": "Imita a los caballos haciendo relinchos.",
        "escuela mágica": "Copia a los maestros en sus clases con humor."
    },
    "hacker/netrunner": {
        "bar clandestino": "Sentado en una mesa apartada, en esquina oscura mientras usa su laptop.",
        "base espacial": "Robando información clasificada de la base desde una gran computadora.",
        "ciudad futurista": "Escondido en un callejón para hackear las cámaras de seguridad del edificio de una gran corporación.",
        "barrios bajos": "Camina agotado devuelta a casa por una calle descuidada y pobremente iluminada.",
        "nave espacial": "Intenta hackear el sistema de la nave para tomar el control de su rumbo.",
        "edificio corporativo": "Infiltrado, roba la información clasificada de la computadora del CEO.",
        "bar lujoso": "Se reúne en una mesa discreta y alejada con un cliente importante.",
        "ciberespacio": "Usa la plataforma para buscar información de empresarios y políticos importantes.",
        "ciudad subterránea": "Camina por las calles con seguridad mientras busca un lugar para comer.",
        "batalla de por territorio": "Sabotea las bases de datos del bando contrario."
    },
    "pandillero": {
        "bar clandestino": "Sentado en la barra, bebiendo y charlando con un grupo grande de amigos.",
        "base espacial": "Pelea con los guardias de seguridad.",
        "ciudad futurista": "Pasa el rato con sus amigos, conduciendo por las calles.",
        "barrios bajos": "Descansando en un callejón.",
        "nave espacial": "Se infiltra para robar partes de la nave.",
        "edificio corporativo": "En una revuelta dura del edificio, rompiendo vidrios y grafiteando las paredes.",
        "bar lujoso": "Afuera del bar, peleando con un empresario.",
        "ciberespacio": "Vandalizando un callejón.",
        "ciudad subterránea": "Pasando el tiempo con su grupo, ríen mientras caminan entre la gente.",
        "batalla de por territorio": "Peleando a puño limpio entre las personas."
    },
    "nomada": {
        "bar clandestino": "Cierra un trato con un cliente.",
        "base espacial": "Se infiltra a la base y se escabulle para no ser detectado por las cámaras.",
        "ciudad futurista": "Camina por las calles iluminadas por el neón de las pantallas y anuncios.",
        "barrios bajos": "Intenta reparar su brazo biónico por su cuenta en un callejón descuidado.",
        "nave espacial": "Se sienta frente al panel de control, intentando averiguar cómo funciona la nave para robarla.",
        "edificio corporativo": "Después de infiltrarse, desactiva las cámaras del edificio.",
        "bar lujoso": "Intenta ocultar su identidad mientras escucha la conversación de un grupo de empresarios.",
        "ciberespacio": "Usa su gran computadora para hackear los servidores.",
        "ciudad subterránea": "Sentado en un taller clandestino tras haberse instalado un brazo biónico.",
        "batalla de por territorio": "Líder de un grupo de rebeldes, dando órdenes y peleando con sus compañeros."
    },
    "fixer": {
        "bar clandestino": "Negocia con un mercenario, ambos sentados en una mesa apartada y oculta.",
        "base espacial": "Observa una pantalla holográfica, pasando toda la información importante a una usb futurista.",
        "ciudad futurista": "Observa el paisaje futurista desde un techo mientras usa un pequeño intercomunicador en su oído para coordinar una operación secreta.",
        "barrios bajos": "Entrega un puño de credenciales falsas a un cliente.",
        "nave espacial": "Organiza a su grupo desde la distancia, observando mientras secuestran la nave por dentro.",
        "edificio corporativo": "En la oficina de un corporativo, cierra un trato importante de contrabando.",
        "bar lujoso": "En una mesa privada y elegante negocia con un grupo de ejecutivos.",
        "ciberespacio": "Con una identidad falsa, conoce clientes nuevos y recluta hackers.",
        "ciudad subterránea": "Observa todo desde cámaras ocultas.",
        "batalla de por territorio": "Crea alianzas y arma a sus aliados."
    },
    "corporativo": {
        "bar clandestino": "Sentado en una mesa pequeña, degusta una bebida mientras dos guardaespaldas se mantienen a su lado.",
        "base espacial": "Dirige una operación importante, dando órdenes a sus subordinados a través de una pantalla holográfica.",
        "ciudad futurista": "Observa la ciudad desde su auto lujoso.",
        "barrios bajos": "Junto a sus guardaespaldas, visita los barrios, observando todo con mala cara.",
        "nave espacial": "Habla con el piloto de la nave que está financiando antes de que éste aborde.",
        "edificio corporativo": "Durante una reunión en una gran y elegante oficina, observa la ciudad a través de los grandes ventanales.",
        "bar lujoso": "Bebe junto a un grupo de socios mientras discuten sobre los papeles que tienen esparcidos sobre la mesa.",
        "ciberespacio": "Da órdenes para eliminar aun Hacker que intenta difamarlo en los anuncios dentro del ciberespacio.",
        "ciudad subterránea": "Infiltrado, entra a una oficina secreta para hablar personalmente con un socio traficante.",
        "batalla de por territorio": "Desde la seguridad de un búnker, habla con sus hombres para liderar una operación de ataque a lugares estratégicas."
    },
    "policía": {
        "bar clandestino": "Investigando discretamente y buscando pruebas.",
        "base espacial": "Patrullando pasillos y manteniendo el orden.",
        "ciudad futurista": "Regulando el tráfico.",
        "barrios bajos": "Persiguiendo un ladrón por la calle.",
        "nave espacial": "Vigilando los alrededores de la nave.",
        "edificio corporativo": "En la entrada del edificio.",
        "bar lujoso": "Cuidando el área VIP.",
        "ciberespacio": "Patrullando en un carro espacial.",
        "ciudad subterránea": "Merodeando alrededor buscando hackers.",
        "batalla de por territorio": "Tratando de mantener orden entre más policías."
    },
    "político": {
        "bar clandestino": "Negociando acuerdos ilegales en secreto.",
        "base espacial": "Dando órdenes.",
        "ciudad futurista": "Dando discurso de promesas que nunca va a cumplir.",
        "barrios bajos": "Prometiendo mayores mejoras y reformas.",
        "nave espacial": "Liderando con debates.",
        "edificio corporativo": "Firmando contratos y alianzas.",
        "bar lujoso": "Bebiendo a más no poder con sus guardaespaldas a sus lados.",
        "ciberespacio": "Difundiendo propaganda digital.",
        "ciudad subterránea": "Buscando apoyos y líderes ilegales.",
        "batalla de por territorio": "Manipula narrativas para tener más seguidores."
    },
    "rockerboy": {
        "bar clandestino": "Presumiendo sus hazañas espaciales.",
        "base espacial": "Explorando emocionado.",
        "ciudad futurista": "Vuela entre rascacielos.",
        "barrios bajos": "Inspirando esperanza con mucha energía.",
        "nave espacial": "Pilotando con mucha experiencia.",
        "edificio corporativo": "Volando por los pasillos mientras juega.",
        "bar lujoso": "Haciendo acrobacias en el aire algo ebrio volando alrededor del bar.",
        "ciberespacio": "Volando alrededor del espacio con destreza.",
        "ciudad subterránea": "Volando entre las calles subterráneas explorando los alrededores.",
        "batalla de por territorio": "Atacando desde el aire con velocidad."
    },
    "ingeniero": {
        "bar clandestino": "Reparando sistemas ocultos del bar.",
        "base espacial": "Ajustando los motores y circuitos con sus herramientas.",
        "ciudad futurista": "Diseñando infraestructuras avanzadas.",
        "barrios bajos": "Construyéndose soluciones improvisadas.",
        "nave espacial": "Manteniendo la nave en operación.",
        "edificio corporativo": "Optimizando la tecnología empresarial.",
        "bar lujoso": "Supervisando sistemas de energía.",
        "ciberespacio": "Programando defensas digitales.",
        "ciudad subterránea": "Instalando maquinaria para sobrevivir.",
        "batalla de por territorio": "Creando armas y defensas estratégicas con sus herramientas."
    },
    "sicario": {
        "bar clandestino": "Esperando recibir órdenes en silencio mientras mantiene su mano en su arma.",
        "base espacial": "Eliminando enemigos con puntería y precisión.",
        "ciudad futurista": "Se mueve entre las sombras buscando su objetivo.",
        "barrios bajos": "Se muestra imponente respecto a la violencia.",
        "nave espacial": "Ejecutando sus objetivos en silencio dentro de la nave.",
        "edificio corporativo": "Atacando a rivales dentro de rivales.",
        "bar lujoso": "Se infiltra disfrazado del otro bando del élite.",
        "ciberespacio": "Hackeando y localizando sus víctimas en su teléfono holograma.",
        "ciudad subterránea": "Controlando territorios con audacia acompañado de sus compañeros y sus armas.",
        "batalla de por territorio": "Luchando sin piedad por el dominio matando a quien se le atraviese."
    },
    "doctor": {
        "oficina": "Atendiendo a sus pacientes con precisión.",
        "barrio": "Revisando a los enfermos en sus casas.",
        "calle transitada": "Auxiliando en emergencias rápidas.",
        "transporte público": "Ayudando a un pasajero desmayado.",
        "bar": "Ayudando a un ebrio fuera del bar tirado en el piso.",
        "parque": "Apoyando en una campaña de vacunación."
    },
    "estudiante": {
        "oficina": "Haciendo su tarea en la entrada de la recepción.",
        "barrio": "Estudiando en casa de sus amigos.",
        "calle transitada": "Corriendo para llegar a sus clases.",
        "transporte público": "Repasando sus tareas mientras llega a la escuela.",
        "bar": "Socializando con sus amigos y bebiendo un poco.",
        "parque": "Jugando con sus amigos trepando árboles."
    },
    "chofer": {
        "oficina": "Esperando órdenes de su ruta de transporte.",
        "barrio": "Conduciendo entre calles estrechas que apenas y entra.",
        "calle transitada": "Maniobrando con destreza y paciencia.",
        "transporte público": "Llevando a sus pasajeros por su ruta.",
        "bar": "Bebiendo un poco después de trabajar por varias horas.",
        "parque": "Estacionandose cerca del parque para descansar."
    },
    "bartender": {
        "oficina": "Preparando los cafés.",
        "barrio": "Montando un puesto de bebidas para ofrecer en el barrio.",
        "calle transitada": "Vendiendo bebidas rápidas a la gente que va pasando.",
        "transporte público": "Ofreciendo bebidas en el transporte público.",
        "bar": "Mezclando cócteles como entretenimiento a los clientes.",
        "parque": "Sirviendo bebidas en un festival en el parque."
    },
    "oficinista": {
        "oficina": "Organizando documentos y agendas.",
        "barrio": "Trabajando de manera remoto desde casas.",
        "calle transitada": "Se apresura a llegar tarde al trabajo.",
        "transporte público": "Revisando correos en su móvil.",
        "bar": "Relajado después de tener un día pesado en la oficina junto a sus compañeros.",
        "parque": "Trabajando al aire libre en una banca del parque."
    },
    "chef": {
        "oficina": "Diseñando su menu de manera corporativa.",
        "barrio": "Cocinando en una fonda local del barrio platillos típicos.",
        "calle transitada": "Ofreciendo comidas para llevar a las personas que viven cerca.",
        "transporte público": "Transportando los ingredientes frescos para su restaurante.",
        "bar": "Preparando botanas gourmet para los clientes.",
        "parque": "Sirviendo comida en un food truck."
    },
    "artista": {
        "oficina": "Decorando la oficina con paredes de colores con su arte.",
        "barrio": "Haciendo arte callejera en las paredes del barrio.",
        "calle transitada": "Exponiendo su arte urbano.",
        "transporte público": "Dibujando pasajeros que hay en el transporte público.",
        "bar": "Creando escenarios y personajes creativos mientras dibuja en su libro.",
        "parque": "Exhibiendo su arte al aire libre."
    },
    "cholo": {
        "oficina": "Graffiteando el edificio con arte callejera.",
        "barrio": "Pasando el rato con sus amigos en el barrio.",
        "calle transitada": "Se desplaza en grupos.",
        "transporte público": "Escuchando música mientras ve fuera del transporte público.",
        "bar": "Bebiendo cerveza junto a sus amigos.",
        "parque": "Organizando encuentros callejeros entre más gente del barrio."
    },
    "programador": {
        "oficina": "Codificando proyectos empresariales.",
        "barrio": "Trabajando desde su casa hackeando computadoras.",
        "calle transitada": "Descansando viendo alrededor con su laptop en mano.",
        "transporte público": "Programando su laptop y cambiando algunos códigos para trabajar.",
        "bar": "Trabajando en un área apartada del bar hackeando a escondidas en el mismo bar.",
        "parque": "Hackeando con WI-FI al aire libre mientras actúa como si nada alrededor de las personas."
    },
    "abogado": {
        "oficina": "Revisando contratos y casos importantes.",
        "barrio": "Asesorando vecinos en problemas legales.",
        "calle transitada": "Defendiendo a su cliente en un tribunal cercano en las calles transitadas.",
        "transporte público": "Estudiando leyes mientras va de camino al tribunal.",
        "bar": "Descansando mientras negocia un nuevo caso con un posible cliente en el bar.",
        "parque": "Ofreciendo su trabajo a posibles clientes en el parque."
    },
    "profesor": {
        "oficina": "Corrigiendo exámenes y preparando la próxima clase.",
        "barrio": "Dando tutorías privadas a estudiantes que van atrasados en su clase.",
        "calle transitada": "Dirigiéndose a la escuela mientras bebe un vaso de cafe.",
        "transporte público": "Revisando sus apuntes que va a dar en la clase a la que va llegar a explicar.",
        "bar": "Tomando junto a sus demás compañeros profesores riendo y hablando de manera tranquila.",
        "parque": "Enseñando a sus estudiantes al aire libre y sentados en el césped."
    }
}
