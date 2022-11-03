import os
from medical_image_converter.converter import multithread_converter


def convert_files(source_dir:str, dest_dir:str) ->None:
    """
        Converts the files in source_dir to jpg and stores it in dest_dir
    """
    source_list = []
    dest_list = []
    for file in os.listdir(source_dir):
        if file.endswith('.ima'):
            source_list.append(
                    os.path.join(
                        source_dir, 
                        file
                        )
                    )

            dest_list.append(
                    os.path.join(
                        dest_dir, 
                        file.replace(
                            '.ima',
                            '.jpg'
                            )
                        )
                    )
    multithread_converter(source_list, dest_list)

def parse_args():
    """
        Parse the arguments
    """
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-s',
            '--source_dir', 
            type=str,
            help='Source directory'
            )
    parser.add_argument(
            '-d',
            '--dest_dir', 
            default = 'JPG_files', 
            type=str, 
            help='Destination directory'
            )
    return parser.parse_args()

def main(args):
    """
        Main function
    """
    if not os.path.exists(args.dest_dir):
        os.makedirs(args.dest_dir)
    convert_files(args.source_dir, args.dest_dir)

if __name__ == '__main__':
    main(parse_args())
