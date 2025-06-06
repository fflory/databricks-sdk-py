import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.recipients.create(name=f"sdk-{time.time_ns()}")

w.recipients.update(name=created.name, comment=f"sdk-{time.time_ns()}")

# cleanup
w.recipients.delete(name=created.name)
