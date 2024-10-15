import numpy as np

percentiles = [
(10,14629),
(20 ,25600),
(30 ,37002),
(40 ,50000),
(50 ,63179),
(60 ,79542),
(70 ,100162),
(80 ,130000),
(90 ,184292)
]


# Convert to a NumPy array
percentiles_array = np.array(percentiles)

print(f"the percentiles_array is {percentiles_array.ndim} dim and {percentiles_array.size} elements")