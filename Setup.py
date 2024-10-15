import kaggle 
import os
kaggle.api.authenticate()

# Imports data from: https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017?resource=download
kaggle.api.dataset_download_files("martj42/international-football-results-from-1872-to-2017", unzip=True, path='data')

