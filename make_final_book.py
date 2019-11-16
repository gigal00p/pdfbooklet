#!/usr/bin/env python
import pprint
import subprocess
import os, shutil


def make_chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def calc_pages(start_page, stop_page):
    stop_page = stop_page + 1
    pages_range = range(start_page, stop_page)
    pages_range = list(pages_range)
    return pages_range

def delete_dir_content(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def first_last(my_list):
    res = [ my_list[0], my_list[-1]]
    return res

def main():
    my_pages = calc_pages(1, 628)
    page_chunks = list(make_chunks(my_pages ,16))

    book_input = "/servil/book.pdf"
    target_path = "/results/"
    delete_dir_content(target_path)
    
    output = 100
    
    for l in page_chunks:
        output = output + 1
        res = first_last(l)

        first_page = res[0]
        last_page = res[1]
        taget_name = "book_" + str(output) + ".pdf"
        full_target_name = target_path + taget_name

        first_page = str(first_page)
        last_page = str(last_page)

        print("Processing first page: {}, last page: {}, target book name: {}".format(first_page, last_page, full_target_name))
        subprocess.call(["python", "pdfbooklet.py", "-f", first_page, "-l", last_page, "-o", full_target_name, book_input])


if __name__ == "__main__":
    main()
