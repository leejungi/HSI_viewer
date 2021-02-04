import spectral
import os
import numpy as np
import h5py

def open_file(dataset, rawbin=None):
    """
    input
        ~~.mat
        ~~.hdr +[~~.bin]
    output
        np.array. check shape (row, column, band)!!
    """
    _, ext = os.path.splitext(dataset)
    ext = ext.lower()
    if ext == '.mat':
        # Load Matlab array
        with h5py.File(dataset, 'r') as f:
            x = list(f.keys())
            return np.array(f[x[0]])
    elif ext == '.hdr':
        # img = spectral.open_image(dataset)
        data_ref = spectral.io.envi.open(dataset, rawbin)
        return np.array(data_ref.load())
    else:
        raise ValueError("Unknown file format: {}".format(ext))


def calibration(rawdata, whiterep, darkrep):
    pass