Batch bsub launcher
===================

Pure python script to create batched GPU jobs using BSUB

Installation / Update
---------------------

::

    pip install -U git+https://github.com/ferrine/gpu-batch.sub
    # or
    pip install -U gpu-batch-sub

Example Config
--------------

Default config for script (location ``~/.gpubatch.conf``) should look
like

::

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

Examples
--------

::

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

    # running sequential jobs
    # yields 2 jobs with sequentially running commands
    > gpu-batch.sub -b 2 -s 'python script_1.py' 'python script_2.py' 'python script_2.py --other-args'

Checking Command Submission
---------------------------

``--debug`` flag helps to print expected submissions to LSF

::

    > gpu-batch.sub --debug --batch 2 command1 command2 named:command3
    >>>>>>>>>>
    #SUBMIT: 0
    vvvvvvvvvv
    #!/bin/sh
    #BSUB -J gpu-batch.sub
    #BSUB -o bsub-log/out/gpu-batch.sub-%J-stats.out
    #BSUB -q normal
    #BSUB -n 1
    #BSUB -gpu "num=1:j_exclusive=no:mode=shared"
    cd ${LS_SUBCWD}
    mkdir -p bsub-log/out
    mkdir -p bsub-log/err
    {
    command1 >\
      bsub-log/out/gpu-batch.sub-${LSB_JOBID}-0.0.0.out 2> bsub-log/err/gpu-batch.sub-${LSB_JOBID}-0.0.0.err ;
    } & {
    command2 >\
      bsub-log/out/gpu-batch.sub-${LSB_JOBID}-0.1.0.out 2> bsub-log/err/gpu-batch.sub-${LSB_JOBID}-0.1.0.err ;
    } & wait

    >>>>>>>>>>
    #SUBMIT: 1
    vvvvvvvvvv
    #!/bin/sh
    #BSUB -J gpu-batch.sub
    #BSUB -o bsub-log/out/gpu-batch.sub-%J-stats.out
    #BSUB -q normal
    #BSUB -n 1
    #BSUB -gpu "num=1:j_exclusive=no:mode=shared"
    cd ${LS_SUBCWD}
    mkdir -p bsub-log/out
    mkdir -p bsub-log/err
    {
    command3 >\
      bsub-log/out/gpu-batch.sub-${LSB_JOBID}-1.0.0-named.out 2> bsub-log/err/gpu-batch.sub-${LSB_JOBID}-1.0.0-named.err ;
    } & wait

Running commands from file
--------------------------

::

    > cat commands
    command1
    command2
    <sequential> # indicates sequential jobs start
    command3
    command4
    </sequential> # indicates sequential jobs end
    > gpu-batch.sub --debug -b 2 -f commands
    >>>>>>>>>>
    #SUBMIT: 0
    vvvvvvvvvv
    #!/bin/sh
    #BSUB -J gpu-batch.sub
    #BSUB -o bsub-log/out/gpu-batch.sub-%J-stats.out
    #BSUB -q normal
    #BSUB -n 1
    #BSUB -gpu "num=1:j_exclusive=no:mode=shared"
    cd ${LS_SUBCWD}
    mkdir -p bsub-log/out
    mkdir -p bsub-log/err
    {
    command1 >\
      bsub-log/out/gpu-batch.sub-${LSB_JOBID}-0.0.0.out 2> bsub-log/err/gpu-batch.sub-${LSB_JOBID}-0.0.0.err ;
    } & {
    command2 >\
      bsub-log/out/gpu-batch.sub-${LSB_JOBID}-0.1.0.out 2> bsub-log/err/gpu-batch.sub-${LSB_JOBID}-0.1.0.err ;
    } & wait

    >>>>>>>>>>
    #SUBMIT: 1
    vvvvvvvvvv
    #!/bin/sh
    #BSUB -J gpu-batch.sub
    #BSUB -o bsub-log/out/gpu-batch.sub-%J-stats.out
    #BSUB -q normal
    #BSUB -n 1
    #BSUB -gpu "num=1:j_exclusive=no:mode=shared"
    cd ${LS_SUBCWD}
    mkdir -p bsub-log/out
    mkdir -p bsub-log/err
    {
    command3 >\
      bsub-log/out/gpu-batch.sub-${LSB_JOBID}-1.0.0.out 2> bsub-log/err/gpu-batch.sub-${LSB_JOBID}-1.0.0.err ;
    command4 >\
      bsub-log/out/gpu-batch.sub-${LSB_JOBID}-1.0.1.out 2> bsub-log/err/gpu-batch.sub-${LSB_JOBID}-1.0.1.err ;
    } & wait

Running single command, no quotes
---------------------------------

::

    > gpu-batch.sub --debug -C python main.py
    >>>>>>>>>>
    #SUBMIT: 0
    vvvvvvvvvv
    #!/bin/sh
    #BSUB -J gpu-batch.sub
    #BSUB -o bsub-log/out/gpu-batch.sub-%J-stats.out
    #BSUB -q normal
    #BSUB -n 1
    #BSUB -gpu "num=1:j_exclusive=no:mode=shared"
    cd ${LS_SUBCWD}
    mkdir -p bsub-log/out
    mkdir -p bsub-log/err
    {
    python main.py >\
      bsub-log/out/gpu-batch.sub-${LSB_JOBID}-0.0.0.out 2> bsub-log/err/gpu-batch.sub-${LSB_JOBID}-0.0.0.err ;
    } & wait

Program Description
-------------------

::

    usage: gpu-batch.sub [-h] [--batch BATCH] [--sequential] [--gpu GPU]
                         [--out OUT] [--err ERR] [--name NAME] [--hosts HOSTS]
                         [--files FILES [FILES ...]] [-C [C [C ...]]]
                         [--queue QUEUE] [--exclusive] [--debug]
                         [--bsub-bin BSUB_BIN] [--version]
                         [jobs [jobs ...]]

    gpu-batch.sub is a util to wrap submissions to LSF in a batch. It
    automatically collects jobs, prepares submission file you can check beforehand
    with `--debug` flag. `gpu-batch.sub` asks LSF for desired number of GPU per
    batch and allocates them in shared or exclusive (not recommended) mode.

    positional arguments:
      jobs                  Jobs to execute (e.g. 'python script.py') enclosed as
                            strings, you can specify either files or explicit jobs
                            in command line. Multiline jobs in files are
                            supported. Optional naming schema for jobs has the
                            following syntax 'name:command' (default: [])

    optional arguments:
      -h, --help            show this help message and exit
      --batch BATCH, -b BATCH
                            Number of jobs in batch where -1 stands for unlimited
                            batch (default: -1)
      --sequential, -s      Make all jobs sequential within bsub submit (default:
                            False)
      --gpu GPU, -g GPU     Number of gpu per batch (default: 1)
      --out OUT, -o OUT     Output path for stdout (default: bsub-log/out)
      --err ERR, -e ERR     Output path for stderr (default: bsub-log/err)
      --name NAME, -n NAME  Name for job, defaults to base directory of execution
                            (default: $(basename `pwd`))
      --hosts HOSTS         Space or comma separated allowed hosts. Empty string
                            holds for ALL visible hosts. It is suggested to
                            specify hosts in `.conf` file. Passing hosts in
                            command line looks like `--hosts ''` for ALL or
                            `--hosts 'host1,host2'` for 2 hosts (default: )
      --files FILES [FILES ...], -f FILES [FILES ...]
                            Read jobs from files. File can contain multiline jobs
                            for readability (default: [])
      -C [C [C ...]]        Single command, does not require quotes (default: [])
      --queue QUEUE, -q QUEUE
                            Queue name (default: normal)
      --exclusive, -x       Exclusive mode allocates GPU only for 1 separate job.
                            (default: no)
      --debug               Print submissions and exit (default: False)
      --bsub-bin BSUB_BIN   bsub binary path (default: bsub)
      --version             Print version and exit (default: False)

    Default settings are stored in `$HOME/.gpubatch.conf`. They will override the
    help message as well. Possible settings for config file: batch, gpu, hosts,
    header, queue. Header will be appended to LSF submission file as is, there is
    no default extra header.
