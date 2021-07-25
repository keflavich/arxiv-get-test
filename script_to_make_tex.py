"""
script_to_make_tex:

2021 July 25: updated to work with arxiv==1.4.0
"""

import arxiv
import re

tex_template = r"""

\href{{{id}}}{{\textcolor{{myred}}{{\large\bf{{{title}}}}}}}

{{\bf{{ \small \textcolor{{Grey}}{{{authors_joined}}}}}}}

{summary}


"""

def make_tex_file(arxiv_id_list, tex_filename='test.tex'):
    arxiv_meta = arxiv.Search(id_list=arxiv_id_list)
    firstauthors = [row.authors[0].name for row in arxiv_meta.results()]

    with open('test_example.tex', 'w') as fh:
        rowdata = {}
        # x[0]: firstauthors
        # split()[-1]: last name
        # [0]: first letter
        for _,row in sorted(zip(firstauthors, arxiv_meta.results()), key=lambda x: x[0].split()[-1][0]):

            rowdata['authors_joined'] = ", ".join([auth.name for auth in row.authors])
            rowdata['title'] = row.title
            rowdata['id'] = row.entry_id
            rowdata['summary'] = row.summary

            fh.write(tex_template.format(**rowdata))

            fh.write("% ----------------------------------- \n\n\n")


def get_arxiv_ids(arxiv_idlist_filename='arxiv.id'):

    with open('arxiv.id', 'r') as fh:
        arxiv_ids = [re.compile("([0-9]{4}\.[0-9]{5})").search(row).groups()[0] for row in fh.readlines()]

    return arxiv_ids

if __name__ == "__main__":
    arxiv_ids = get_arxiv_ids()
    make_tex_file(arxiv_ids)
