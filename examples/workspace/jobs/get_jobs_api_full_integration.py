import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import jobs

w = WorkspaceClient()

notebook_path = f"/Users/{w.current_user.me().user_name}/sdk-{time.time_ns()}"

cluster_id = (
    w.clusters.ensure_cluster_is_running(os.environ["DATABRICKS_CLUSTER_ID"]) and os.environ["DATABRICKS_CLUSTER_ID"]
)

created_job = w.jobs.create(
    name=f"sdk-{time.time_ns()}",
    tasks=[
        jobs.Task(
            description="test",
            existing_cluster_id=cluster_id,
            notebook_task=jobs.NotebookTask(notebook_path=notebook_path),
            task_key="test",
            timeout_seconds=0,
        )
    ],
)

by_id = w.jobs.get(job_id=created_job.job_id)

# cleanup
w.jobs.delete(job_id=created_job.job_id)
