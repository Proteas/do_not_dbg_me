# Issue
If `settings set target.load-script-from-symbol-file true`, lldb will auto run the python script embedded in dSYM file, then it can be used to do evil things.

# Advise
When debug untrusted binary with dSYM file, review the embedded python script first.

# PoC
* run `make` to build payload
* `cd payload`
* `lldb do_not_dbg_me`

# Contact
* Weibo : [Proteas](http://weibo.com/proteaswang)
* Twitter : [ProteasWang](https://twitter.com/ProteasWang)
