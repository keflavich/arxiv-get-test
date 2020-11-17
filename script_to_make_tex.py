import arxiv
import re

def make_tex_file(arxiv_id_list, tex_filename='test.tex'):
    arxiv_meta = arxiv.query(id_list=arxiv_id_list)

    with open('test_example.tex', 'w') as fh:
        for row in arxiv_meta:
            # all the formatting happens here
            fh.write(row['title'] + "\\\\ \n")
            fh.write("\\url{" + row['id'] + "}\\\\ \n")
            fh.write(", ".join(row['authors']) + "\\\\ \n")
            fh.write(row['summary'] + '\n\\\\ \n\n')
            fh.write("% ----------------------------------- \n\n\n")


def get_arxiv_ids(arxiv_idlist_filename='arxiv.id'):

    with open('arxiv.id', 'r') as fh:
        arxiv_ids = [re.compile("([0-9]{4}\.[0-9]{5})").search(row).groups()[0] for row in fh.readlines()]

    return arxiv_ids

if __name__ == "__main__":
    arxiv_ids = get_arxiv_ids()
    make_tex_file(arxiv_ids)
