from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# 1. Build circuit with a named classical register "meas"
qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# 2. Run using native sampler
sampler = StatevectorSampler()
job = sampler.run([qc])
result = job.result()

# 3. Print counts
counts = result[0].data.c.get_counts()
print("Measurement counts:", counts)