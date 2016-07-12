#!/usr/bin/python
import fileinput

indexID = 0
indexTempoGuasto = 1
data = {}

for line in fileinput.input():
	values = line.split('\t')
	machineId = values[indexID]
	tempoGuasto = float(values[indexTempoGuasto])
	temp = {machineId:tempoGuasto}

	if machineId in data:
		data[machineId] = data[machineId] + temp[machineId]
	else:
		data.update(temp)
print(data)