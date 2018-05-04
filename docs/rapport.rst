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
:py:const:`MAX_SIZE_X`, :py:const:`MAX_SIZE_Y` och :py:const:`WALLS` storleken av kartan
och antalet hinder som ska genereras:

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 4-9, 11-14

Sedan skapar jag en metod :py:meth:`generate_map` till klassen :py:class:`Graph` som ska generera kartans
koordinater och bestämma vilka av dessa som är hinder och vilka som går att gå på.
Koordinaterna genereras i en nästlad loop som fyller dictionaryn :py:data:`map_`
med koordinater tilldelade värdet 1, där :py:data:`xmax` och :py:data:`ymax` beskriver
koordinatsystemets storlek i x- och y-led.
Jag skapar sedan ytterligare en nästlad loop som slumpar fram alla hinders koordinater
och tilldelar dem värdet -1.

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 16, 18-35

Jag behöver även beräkna vilka rutor som är grannar till en undersökt ruta i en
given karta, då jag behöver koordinaterna för de möjliga steg som går att utföra.
Därför skapar jag metoden :py:meth:`neighbors` till :py:class:`Graph` som adderar den undersökta
rutans :py:data:`x`-värde med :py:data:`x_step` och rutans :py:data:`y`-värde
med :py:data:`y_step`, där :py:data:`x_step` och :py:data:`y_step` kommer från
en lista tupler tilldelad namnet :py:data:`possible_steps`.
Listan beskriver grannarnas positioner relativt
den undersökta rutan. Notera att ...
Metoden returnerar sedan en lista med koordinater för möjliga steg:

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
samt koordinaterna för start och mål.

.. literalinclude:: ../astar/astar.py
  :language: python
  :lines: 60, 62-87
