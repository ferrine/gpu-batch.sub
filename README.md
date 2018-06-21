Batch bsub launcher. 

Installation
------------
```
pip install git+https://github.com/ferrine/gpu-batch.sub

```

Config
------
Default config for script (location `~/.gpubatch.conf`) should look like
```
> cat config
[gpubatch]
batch=1
gpu=1
; use ';' for comments
;paths are relative
out=bsub-log/out
err=bsub-log/err
hosts=host1,host2,host3
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
```

Arguments
---------
```
       [-h] [--batch BATCH] [--gpu GPU] [--out OUT] [--err ERR] [--name NAME]
       [--hosts HOSTS] [--files FILES [FILES ...]] [--queue QUEUE] [--debug]
       [jobs [jobs ...]]

positional arguments:
  jobs                  jobs to execute like 'python script.py', you can
                        specify either files or explicit jobs (default: [])

optional arguments:
  -h, --help            show this help message and exit
  --batch BATCH, -b BATCH
                        number of jobs in batch where -1 stands for unlimited
                        batch (default: -1)
  --gpu GPU, -g GPU     number of gpu per batch (default: 1)
  --out OUT, -o OUT     output path for stdout (default: bsub-log/out)
  --err ERR, -e ERR     output path for stderr (default: bsub-log/err)
  --name NAME, -n NAME  name for job, defaults to base directory of execution
                        (default: gpu-batch)
  --hosts HOSTS         allowed hosts (default: )
  --files FILES [FILES ...], -f FILES [FILES ...]
                        Read jobs from file (default: [])
  --queue QUEUE, -q QUEUE
                        queue name (default: normal)
  --debug               prints commands to execute first (default: False)
```