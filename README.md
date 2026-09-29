Hinweisschilder an den Maschinen
================================

Hinweisschilder an den Maschinen des [FAU FabLab](https://fablab.fau.de).

Inhalt
------

- Schilder mit Ampelfarbe (rot/gelb/grün), Hinweisen zur Benutzung und QR-Code zur Einweisung

Download
--------

Die neueste Version aus [GitHub](https://github.com/fau-fablab/hinweisschilder) ist als PDF abrufbar:

- [Hinweisschilder](https://brain.fablab.fau.de/build/hinweisschilder/hinweisschilder.pdf)

Außerdem baut eine GitHub Action die PDFs bei jedem Push. Auf dem Hauptbranch entsteht dabei ein
[Release](https://github.com/fau-fablab/hinweisschilder/releases) mit Datums-Version (`vJJJJ.MM.TT`) und den PDFs.

Auschecken und bauen
--------------------

```bash
git clone --recursive git@github.com:fau-fablab/hinweisschilder.git
cd hinweisschilder
make
```

Die PDFs landen in `output/`. Layout, Kopf- und Fußzeile und das Logo des FAU FabLab (mit
FAU-Schriftzug) kommen aus dem Untermodul [fablab-document](https://github.com/fau-fablab/fablab-document),
das Logo wiederum aus dessen Untermodul [logo](https://github.com/fau-fablab/logo). Bei einem bestehenden
Klon die Untermodule mit `git submodule update --init --recursive` laden.

Technische Details zum Buildserver: [fau-fablab/buildserver](https://github.com/fau-fablab/buildserver)

[![Build Status](https://brain.fablab.fau.de/build/hinweisschilder/status.svg)](https://brain.fablab.fau.de/build/hinweisschilder/)
[![TODOs](https://brain.fablab.fau.de/build/hinweisschilder/status-todos.svg)](https://brain.fablab.fau.de/build/hinweisschilder/)
[![PDF bauen](https://github.com/fau-fablab/hinweisschilder/actions/workflows/pdf.yml/badge.svg)](https://github.com/fau-fablab/hinweisschilder/actions/workflows/pdf.yml)

Lizenz
------

[![Lizenz: CC BY-SA 3.0](https://licensebuttons.net/l/by-sa/3.0/de/88x31.png)</br>CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
