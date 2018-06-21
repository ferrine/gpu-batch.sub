Batch bsub launcher. Default config for script (location ~/.gpubatch.conf) should look like

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
More info in help command

```
gpu-batch.sub --help
usage: 
Batch bsub launcher. Default config for script (location ~/.gpubatch.conf) should look like

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
---------------------------------
       [-h] [--batch BATCH] [--gpu GPU] [--out OUT] [--err ERR] [--name NAME]
       [--hosts HOSTS] [--file FILE] [--queue QUEUE] [--debug]
       [jobs [jobs ...]]

positional arguments:
  jobs                  jobs to execute like 'python script.py'

optional arguments:
  -h, --help            show this help message and exit
  --batch BATCH, -b BATCH
                        number of jobs in batch
  --gpu GPU, -g GPU     number of gpu per batch
  --out OUT, -o OUT     output path for stdout
  --err ERR, -e ERR     output path for stderr
  --name NAME, -n NAME  name for job, defaults to base directory of execution
  --hosts HOSTS         allowed hosts
  --file FILE, -f FILE  Read jobs from file
  --queue QUEUE, -q QUEUE
                        queue name
  --debug               prints commands to execute first
```

