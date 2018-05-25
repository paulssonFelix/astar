Undersökning av A*
==================

Problem
-------
Problemet för denna uppgift är att skriva ett program som i en given karta hittar
den närmsta vägen från punkt a till punkt b med hjälp av sökalgoritmen A*. Detta
problem delas upp i två delproblem: `Skapande av kartan`_ och `Framställning av
A* algoritmen`_.

_`Skapande av kartan`
----------------------

Först skapar jag klassen :py:class:`Graph` och bestämer med hjälp av
:py:const:`MAX_SIZE_X`, :py:const:`MAX_SIZE_Y` och :py:const:`OBSTACLES` storleken av kartan
och antalet hinder som ska genereras:

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 4-9, 11-14

Sedan skapar jag en metod :py:meth:`generate_map` till klassen :py:class:`Graph` som ska generera kartans
koordinater och bestämma vilka av dessa som är hinder och vilka som går att gå på.
Koordinaterna genereras i en nästlad loop som tilldelar dem värdet 1 och lägger dem
i dictionaryn :py:data:`map_`. Variablerna :py:data:`xmax` och :py:data:`ymax`
används i loopen för att beskriva koordinatsystemets storlek i x- och y-led.
Jag skapar sedan ytterligare en nästlad loop som slumpar fram alla hinders koordinater
och tilldelar dem värdet -1.

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 16, 18-35

Jag ska även beräkna vilka rutor som är grannar till en undersökt ruta i en
given karta, då jag behöver veta koordinaterna för de steg som är möjliga att utföra.
Därför skapar jag metoden :py:meth:`neighbors` till klassen :py:class:`Graph`
som ska addera den undersökta rutans :py:data:`x`-värde med :py:data:`x_step`
och rutans :py:data:`y`-värde med :py:data:`y_step`, där :py:data:`x_step` och
:py:data:`y_step` kommer från en lista tupler vid namnet
:py:data:`possible_steps`. Listan beskriver grannarnas positioner relativt
den undersökta rutan. Notera att jag tilldelar ``self.map.get(nb, -1)`` värdet
-1 om metoden undersöker en ruta som inte finns definierad i koordinatsystemet,
detta för att undvika eventuella fel. Metoden returnerar sedan en lista med koordinater för möjliga steg:

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 37, 39-47

Sist skapar jag en väldigt simpel metod :py:meth:`cost` som beskriver kostnaden
för att ta ett steg i kartan:

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 49, 51

_`Framställning av A* algoritmen`
----------------------------------

Innan jag skriver A* algoritmen så vill jag först bestämma vilken heuristik jag skall
använda, det vill säga hur jag ska mäta avstånd i koordinatsystemet. I detta
projekt har jag valt att mäta med manhattanavstånd. Manhattanavståndet kan beskrivas som summan av
differensen mellan två koordinaters x-värden plus differensen mellan deras y-värden.
För att beräkna detta skapar jag en funktion :py:func:`heuristic` med målets
och den undersökta rutans koordinater som argument:

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 54, 56-58

Nu har det blivit dags att skriva A* algoritmen. Jag börjar med att skapa en
funktion :py:func:`astar` med tre argument: En karta från klassen :py:class:`Graph`
samt koordinaterna för start och mål. Sedan skapar jag :py:data:`frontier`, en så kallad "prioriterad kö",
som kommer att behövas för att kunna prioritera undersökningen av den kortaste
möjliga vägen mellan start och mål. Jag lägger till startpositionen i
:py:data:`frontier` med prioriteringen 0.

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 60, 62-67

Sedan skapar jag en while-loop som hämtar den ruta som står först i :py:data:`frontier`.
I while-loopen skapar jag en for-loop som ska beräkna längden av vägen mellan
start och mål för den nuvarande rutans alla grannar. Om den undersökta koordinaten
inte har något värde från en tidigare beräkning eller har ett värde som är större
än den nya beräkningen så tilldelas den undersökta koordinaten värdet från
den nya beräkning. Den undersökta rutan läggs även till i dictionaryn
:py:data:`came_from` och tilldelas där föregående rutas koordinat som värde.
Genom att göra detta så går det följa vilka steg som togs för att gå den kortaste
vägen till målet för att sedan rita upp denna väg. Sammansättningen av de steg som skapar den kortaste vägen
görs i loopen ``while current:``, där den lägger till den nuvarande koordinaten
(vilket i detta fall är den sist undersökta, förhoppningsvis även målets
koordinat) i listan :py:data:`path`, för att sedan byta den "nuvarande" koordinaten
mot den granne som har den beräknat kortaste vägen (``current = came_from[current]``).
Denna loop fortsätter tills startrutan är den "nuvarande" koordinaten, då
``came_from[start] = None``.

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 69-87

Till sist ska jag skriva koden som kör själva sökalgorithmen. Jag börjar med att
tilldela variabeln :py:data:`graph` en karta med storleken given av :py:const:`MAX_SIZE_X`
och :py:const:`MAX_SIZE_Y`. Sedan tilldelas en ny variabel :py:data:`path` värdet
av funktionen :py:func:`astar` med följande argument: kartan :py:data:`graph`,
koordinaten för övre vänstra hörnet (start) och koordinaten för nedre högra hörnet
(mål). Sist skapar jag en nästlad loop som hanterar ritandet av kartan där alla hinder
är markerade med "#", vägen är markerad med "X" och resten av kartans koordinater
representeras av punkter.

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 92-110
