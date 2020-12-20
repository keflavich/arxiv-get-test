import arxiv
import re

tex_template = r"""

\href{{{id}}}{{\textcolor{{myred}}{{\large\bf{{{title}}}}}}}

{{\bf{{ \small \textcolor{{Grey}}{{{authors_joined}}}}}}}

{summary}

\url{{{id}}}

"""

def make_tex_file(arxiv_id_list, tex_filename='test.tex'):
    arxiv_meta = arxiv.query(id_list=arxiv_id_list)

    with open(tex_filename, 'w') as fh:
        for row in sorted(arxiv_meta, key=lambda x: x['authors'][0]):
            row['authors_joined'] = ", ".join(row['authors'])

            fh.write(tex_template.format(**row))

            fh.write("% ----------------------------------- \n\n\n")


def get_arxiv_ids(arxiv_idlist_filename='arxiv.id'):

    with open('arxiv.id', 'r') as fh:
        arxiv_ids = [re.compile("([0-9]{4}\.[0-9]{5})").search(row).groups()[0] for row in fh.readlines()]

    return arxiv_ids

if __name__ == "__main__":
    arxiv_ids = get_arxiv_ids()
    make_tex_file(arxiv_ids)
