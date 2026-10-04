Hinweisschilder an den Maschinen
================================

Hinweisschilder an den Maschinen des [FAU FabLab](https://fablab.fau.de).

Inhalt
------

- Schilder mit Ampelfarbe als Hintergrund: grün (allgemeine Werkstatt-Einweisung),
  gelb (nur mit unterschriebener Einweisung für das Gerät), rot (nur nach Rücksprache),
  dazu Verläufe gelb-grün und gelb-rot
- Hinweise zur Benutzung, Sicherheitszeichen (GHS, ISO 7010) und ein QR-Code, der auf das
  neueste Release der passenden Einweisung zeigt (sonst auf fablab.fau.de)
- im PDF sortiert: erst Geräte mit eigener Einweisung, dann allgemeine Werkstatt-Einweisung,
  dann ohne Einweisung

Die Schilder gibt es in zwei Größen, jeweils als DIN-A4-Bögen zum Ausschneiden
(Schnittlinien mit Schere):

- `hinweisschilder-a6.pdf`: DIN A6, 4 Schilder pro Bogen (A4 quer)
- `hinweisschilder-a7.pdf`: DIN A7, 8 Schilder pro Bogen (A4 hoch)

Für die Festool-Geräte gibt es zusätzlich Etiketten, die genau in das Beschriftungsfeld
der Systainer passen (Systainer³ M/L und T-Loc, 85,72 × 54,03 mm wie die
[Festool-Vorlage](https://www.festool.com/knowledge/systainer-labels)):

- `hinweisschilder-systainer.pdf`: 10 Etiketten pro Bogen (A4 hoch), direkt aneinander,
  Schnittmarken im Rand. Kompaktes Layout ohne Ansprechpartner.

Welche Schilder als Etikett erscheinen, steuert die Option `systainer` in `schilder.tex`.

Beim Drucken **tatsächliche Größe (100 %)** wählen, nicht „An Seite anpassen“.

Die Schilder stehen in `schilder.tex`, Aufbau und Farben in `schilder-layout.tex`.

Download
--------

Die neueste Version aus [GitHub](https://github.com/fau-fablab/hinweisschilder) ist als PDF abrufbar:

- [Hinweisschilder DIN A6](https://brain.fablab.fau.de/build/hinweisschilder/hinweisschilder-a6.pdf)
- [Hinweisschilder DIN A7](https://brain.fablab.fau.de/build/hinweisschilder/hinweisschilder-a7.pdf)
- [Systainer-Etiketten](https://brain.fablab.fau.de/build/hinweisschilder/hinweisschilder-systainer.pdf)

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
