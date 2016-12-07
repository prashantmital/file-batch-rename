import glob
import os
import shutil

# operations (can be input as JSON/YAML)
file_operations = [
    {
        "src": "test_data/*glob1*.txt",
        "dst": "tempdir_glob1/",
        "transformations": [
            {
                "method": str.replace,
                "args": ('glob1', 'globb1'),
            },
        ]
    },
    {
        "src": "test_data/*glob2*.txt",
        "dst": "tempdir_glob2/",
        "transformations": [
            {
                "method": str.replace,
                "args": ('file_', ''),
            },
        ]
        },
]


def main():
    for operation in file_operations:
        source_files = glob.glob(operation["src"])
        destination_dir = operation["dst"]
        os.makedirs(destination_dir)
        for sfile in source_files:
            src_basename = os.path.basename(sfile)
            for transformation in operation["transformations"]:
                dst_basename = transformation["method"](
                    src_basename, *transformation["args"]
                )
            if dst_basename is None:
                dst_basename = src_basename
            shutil.copy(sfile, os.path.join(destination_dir, dst_basename))


if __name__ == '__main__':
    main()
