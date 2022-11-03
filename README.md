# medicalimage_converter


## Installation

```
pip install git+https://github.com/siddhi47/medicalimage_converter.git

```


Usage:

```python

from medical_image_converter.converter import multithread_converter


folder_path = "dicom_files"
jpg_folder_path = "JPG_files"
images_path = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]
output_path = [os.path.join(jpg_folder_path, f.replace('.ima','.jpg')) for f in os.listdir(folder_path)]

multithread_converter(images_path, output_path)

```
