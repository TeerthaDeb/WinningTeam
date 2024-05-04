curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init

Then log in and you can use the project-id and credentials to access the bucket. 
gcloud auth application-default login

import os
# Load project ID from environment variable
project_id = os.getenv('PROJECT_ID')
For bash or zsh:
```export PROJECT_ID=your_project_id```
For Windows cmd:

```set PROJECT_ID=your_project_id```
For PowerShell:
$env:PROJECT_ID="your_project_id"

cd WinningTeam/Image_analysis
python simple.py
