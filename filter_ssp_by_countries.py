import rasterio as rio
import numpy as np

# Load countries.tif as numpy array
with rio.open('countries.tif') as src:
    # read raster to np array
    img = src.read()
    img_meta = src.profile
    print(src.profile)
    print(img.dtype)

with rio.open('ssp4urb2010.tif') as src:
    # read raster to np array
    ssp = src.read()
    ssp = ssp.astype('float64')
    ssp_meta = src.profile
    # Change meta data dictionary
    ssp_meta['dtype'] = 'float64'
    print(ssp_meta)
    print(ssp.dtype)

# Set country value
country = 524

# Extract country fra source
ssp[img < country] = np.nan #-9999
ssp[img > country] = np.nan #-9999
ssp[ssp == 0] = np.nan #-9999

ssp_meta['nodata'] = np.nan #-9999

with rio.open('output.tif', 'w', **ssp_meta) as dst:
    dst.write(ssp)