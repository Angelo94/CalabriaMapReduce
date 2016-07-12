#!/usr/bin/python
import fileinput

indexID = 2
indexTempoGuasto = 3

for line in fileinput.input():
  values = line.split(';')
  idMacchina = values[indexID]
  tempoGuasto = values[indexTempoGuasto]
  print(('{0}\t{1}'.format(idMacchina, tempoGuasto)).replace("\n",""))