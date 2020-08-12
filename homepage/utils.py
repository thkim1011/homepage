import os


def traverse_directory(source_dir, output_dir, map_fn):
    """
    Takes a source_dir, output_dir, and a mapping fn which the output dir
    and a filename, and maps each file in the source_dir using the map fn.
    """
    def traverse_directory_helper(source_dir, output_dir, map_fn, rel_path):
        for filename in os.listdir(os.path.join(source_dir, rel_path)):
            filepath = os.path.join(source_dir, rel_path, filename)
            if os.path.isdir(filepath):
                os.mkdir(os.path.join(output_dir, rel_path, filename))
                traverse_directory_helper(
                    source_dir,
                    output_dir,
                    map_fn,
                    os.path.join(rel_path, filename)
                )
            else:
                map_fn(filepath, os.path.join(output_dir, rel_path, filename))
    traverse_directory_helper(source_dir, output_dir, map_fn, '')
