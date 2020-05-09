# Reproducing https://github.com/jeromerobert/pdfarranger/issues/195

import sys
import pikepdf

print(pikepdf.__version__)

if len(sys.argv) < 2:
    print("Need one pdf as argument")
    exit(1)


doc = pikepdf.open(sys.argv[1])
with doc.open_metadata() as meta:
    meta.load_from_docinfo(doc.docinfo)

print("Done")


"""
Results
File: https://github.com/jeromerobert/pdfarranger/files/4553811/Algo_Extrem.pdf
(from https://github.com/jeromerobert/pdfarranger/issues/195#issuecomment-621396280)

Fix:
1.11.2.dev17+g8f7dd4d.d20200503
/home/da/.local/lib/python3.7/site-packages/pikepdf/models/metadata.py:321: UserWarning: The metadata field /AAPL:Keywords with value 'pikepdf.Array([  ])' has no XMP equivalent, so it was discarded
  warn(msg)
Done


No error:
1.7.0
1.8.2
1.8.3

Error:

1.9.0
Traceback (most recent call last):
  File "/home/da/git/pdfarranger/pdfarranger/pikepdf_how_to_str_err.py", line 15, in <module>
    meta.load_from_docinfo(doc.docinfo)
  File "/home/da/.local/lib/python3.7/site-packages/pikepdf/models/metadata.py", line 305, in load_from_docinfo
    ).format(extra, docinfo.get(extra))
NotImplementedError: don't know how to __str__ this object

1.10.0
Traceback (most recent call last):
  File "/home/da/git/pdfarranger/pdfarranger/pikepdf_how_to_str_err.py", line 15, in <module>
    meta.load_from_docinfo(doc.docinfo)
  File "/usr/lib64/python3.7/site-packages/pikepdf/models/metadata.py", line 317, in load_from_docinfo
    ).format(extra, docinfo.get(extra))
NotImplementedError: don't know how to __str__ this object



1.11.0
Traceback (most recent call last):
  File "/home/da/git/pdfarranger/pdfarranger/pikepdf_how_to_str_err.py", line 15, in <module>
    meta.load_from_docinfo(doc.docinfo)
  File "/usr/lib64/python3.7/site-packages/pikepdf/models/metadata.py", line 317, in load_from_docinfo
    ).format(extra, docinfo.get(extra))
NotImplementedError: don't know how to __str__ this object


"""