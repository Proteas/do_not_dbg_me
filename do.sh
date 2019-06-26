#!/bin/sh
set -e

make clean
make

cd payload
lldb do_not_dbg_me
