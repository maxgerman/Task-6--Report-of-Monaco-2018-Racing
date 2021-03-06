## Monaco 2018 report
#### This tool creates sorted report tables with results of the best lap times based on the log files of the drivers' start and finish times.

The log files must include abbreviations, start and end times. Default path is "data".

CLI parameters:
- --files - path to the folder with the data files (with names ABBR_FILENAME, START_LOG, END_LOG)
- --asc or --desc - order of the report
- --driver - name or its part of the driver whose report to show


##### Examples:
```python
>report.py
 1. Sebastian Vettel     |FERRARI                   |0:01:04.415
 2. Valtteri Bottas      |MERCEDES                  |0:01:12.434
 3. Stoffel Vandoorne    |MCLAREN RENAULT           |0:01:12.463
 4. Kimi Räikkönen       |FERRARI                   |0:01:12.639
 5. Fernando Alonso      |MCLAREN RENAULT           |0:01:12.657
 6. Charles Leclerc      |SAUBER FERRARI            |0:01:12.829
 7. Sergio Perez         |FORCE INDIA MERCEDES      |0:01:12.848
 8. Romain Grosjean      |HAAS FERRARI              |0:01:12.930
 9. Pierre Gasly         |SCUDERIA TORO ROSSO HONDA |0:01:12.941
10. Carlos Sainz         |RENAULT                   |0:01:12.950
11. Nico Hulkenberg      |RENAULT                   |0:01:13.065
12. Brendon Hartley      |SCUDERIA TORO ROSSO HONDA |0:01:13.179
13. Marcus Ericsson      |SAUBER FERRARI            |0:01:13.265
14. Lance Stroll         |WILLIAMS MERCEDES         |0:01:13.323
15. Kevin Magnussen      |HAAS FERRARI              |0:01:13.393
------------------------------------------------------------
16. Daniel Ricciardo     |RED BULL RACING TAG HEUER |0:02:47.987
17. Sergey Sirotkin      |WILLIAMS MERCEDES         |0:04:47.294
18. Esteban Ocon         |FORCE INDIA MERCEDES      |0:05:46.972
19. Lewis Hamilton       |MERCEDES                  |0:06:47.540


>report.py -d Gas
Pierre Gasly         |SCUDERIA TORO ROSSO HONDA |0:01:12.941

>report.py --files "..\data2" --desc
19. Lewis Hamilton       |MERCEDES                  |0:06:47.540
18. Esteban Ocon         |FORCE INDIA MERCEDES      |0:05:46.972
17. Sergey Sirotkin      |WILLIAMS MERCEDES         |0:04:47.294
16. Daniel Ricciardo     |RED BULL RACING TAG HEUER |0:02:47.987
15. Kevin Magnussen      |HAAS FERRARI              |0:01:13.393
14. Lance Stroll         |WILLIAMS MERCEDES         |0:01:13.323
13. Marcus Ericsson      |SAUBER FERRARI            |0:01:13.265
12. Brendon Hartley      |SCUDERIA TORO ROSSO HONDA |0:01:13.179
11. Nico Hulkenberg      |RENAULT                   |0:01:13.065
10. Carlos Sainz         |RENAULT                   |0:01:12.950
 9. Romain Grosjean      |HAAS FERRARI              |0:01:12.930
 8. Sergio Perez         |FORCE INDIA MERCEDES      |0:01:12.848
 7. Charles Leclerc      |SAUBER FERRARI            |0:01:12.829
 6. Fernando Alonso      |MCLAREN RENAULT           |0:01:12.657
 5. Kimi Räikkönen       |FERRARI                   |0:01:12.639
 4. Stoffel Vandoorne    |MCLAREN RENAULT           |0:01:12.463
 3. Valtteri Bottas      |MERCEDES                  |0:01:12.434
 2. Sebastian Vettel     |FERRARI                   |0:01:04.415
 1. Pierre Gasly         |SCUDERIA TORO ROSSO HONDA |0:00:12.941


```