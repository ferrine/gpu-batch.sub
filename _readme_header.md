Batch bsub launcher
===================
Pure python script to create batched GPU jobs using BSUB

Installation / Update
---------------------
```
pip install -U git+https://github.com/ferrine/gpu-batch.sub

```

Example Config
--------------
Default config for script (location `~/.gpubatch.conf`) should look like
```
> cat config
[gpubatch]
batch=-1
gpu=1
; use ';' for comments
;paths are relative
out=bsub-log/out
err=bsub-log/err
hosts=host1 host2 host3
queue=normal
header=
    #BSUB option1
    #BSUB option2
    #BSUB option3
    custom code you want
```

Examples
--------
```
# batch by -1
# yields 1 job
> gpu-batch.sub 'python script_1.py' 'python script_2.py' 'python script_2.py --other-args'

# batch by 2
# yields 2 jobs
> gpu-batch.sub -b 2 'python script_1.py' 'python script_2.py' 'python script_2.py --other-args'

# run from file
> gpu-batch.sub -b 2 -f filewithjobs1 filewithjobs2 filewithjobs3
> cat filewithjobs1
multiline \ # comments are ok
    job number one
# comments here are ok too
multiline \
    job number two

# naming jobs
# special syntax is applied (no spaces allowed in jobname)
gpu-batch.sub 'jobname : python script1.py'
```
