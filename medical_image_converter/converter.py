"""
    author: siddhi.bajracharya
    desc: Converts medical image (.ima) to .jpg
    email: siddhikiran.bajracharya@gmail.com
"""

import os
import cv2
import pydicom as dicom
import concurrent.futures

def convert_dicom_to_jpg(input_path:str, output_path:str) ->str: 
    """
        Converts the input image to jpg

        param:
            input_path: input path of the .ima image
            output_path: output path where the image is stored
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError("File not found")

    try:
        print("Converting {} to {}".format(input_path, output_path))
        ds = dicom.read_file(input_path,)
        pixel_array_numpy = ds.pixel_array
        cv2.imwrite(output_path, pixel_array_numpy)
        return output_path
    except Exception as e:
        print("Error while converting dicom to jpg.:", str(e))
        return ''

def multithread_converter(source_list:list, dest_list:list)->None:
    """
        Use multithreading to write the jpg files

        params:
            source_list: list of source files.
            dest_list: list of destination files where the files are to be stored
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(convert_dicom_to_jpg, source_list, dest_list)
