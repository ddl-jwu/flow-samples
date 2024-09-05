from flytekit import workflow
from typing import TypeVar
from flytekit.types.file import FlyteFile
from flytekitplugins.domino.helpers import Input, Output, run_domino_job_task

'''
To run this flow, execute the command below:

pyflyte run --remote workflow.py multiple_inputs --data_path_a /mnt/data/snapshots/DatasetA/1 --data_path_b /mnt/data/snapshots/DatasetB/1 --data_path_c /mnt/data/snapshots/DatasetC/1

'''
@workflow
def multiple_inputs(data_path_a: str, data_path_b: str, data_path_c: str) -> FlyteFile[TypeVar("pdf")]:

    data_outputs = run_domino_job_task(
        flyte_task_name="Merge data",
        command="prod/adam.sas",
        environment_name="SAS Analytics Pro",
        inputs=[
            Input(name="data_path_a", type=str, value=data_path_a),
            Input(name="data_path_b", type=str, value=data_path_b),
            Input(name="data_path_c", type=str, value=data_path_c)
        ],
        output_specs=[Output(name="adam", type=FlyteFile[TypeVar("sas7bdat")])],
        use_project_defaults_for_omitted=True
    )

    report_outputs = run_domino_job_task(
        flyte_task_name="Create report",
        command="prod/tfl.sas",
        environment_name="SAS Analytics Pro",
        inputs=[Input(name="adam", type=FlyteFile[TypeVar("sas7bdat")], value=data_outputs["adam"])],
        output_specs=[Output(name="report", type=FlyteFile[TypeVar("pdf")])],
        use_project_defaults_for_omitted=True
    )

    return report_outputs["report"]