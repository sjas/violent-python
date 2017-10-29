#!/bin/bash

./004-fs-operations.py
echo
./004-fs-operations.py exists asdf_not_existing_file.txt
./004-fs-operations.py exists 004a-everything-possible.txt
echo
./004-fs-operations.py readable 004a-not-readable.txt
./004-fs-operations.py readable 004a-everything-possible.txt
echo
./004-fs-operations.py writable 004a-not-writable.txt
./004-fs-operations.py writable 004a-everything-possible.txt
echo
./004-fs-operations.py executable 004a-not-executable.txt
./004-fs-operations.py executable 004a-everything-possible.txt
