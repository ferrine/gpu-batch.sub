import pytest
from importlib.machinery import SourceFileLoader
gpu_batch_sub = SourceFileLoader("gpu_batch_sub", "gpu-batch.sub").load_module()


@pytest.mark.parametrize(
    ['input', 'expected'],
    [
        (['job1', 'job2'], [['job1'], ['job2']]),
        (['job1#comment', 'job2'], [['job1'], ['job2']]),
        (['job1', '#comment',  'job2'], [['job1'], ['job2']]),
        (['job1\\', 'job2'], [['job1\\\njob2']]),
        (['<sequential>', 'job1', 'job2', '</sequential>', 'job3'], [['job1', 'job2'], ['job3']]),
        (['<sequential>', 'job1', 'job2', '', '</sequential>', 'job3'], [['job1', 'job2'], ['job3']]),
        (['<sequential>', 'job1', 'job2', '', 'job3\\', 'job4', '</sequential>', 'job5'],
         [['job1', 'job2', 'job3\\\njob4'], ['job5']])
    ]
)
def test_possibly_multiline_jobs(input, expected):
    output = gpu_batch_sub.possibly_multiline_jobs(input)
    assert output == expected
