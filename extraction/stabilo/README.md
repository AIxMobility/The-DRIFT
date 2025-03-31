# 🗂️ Additional Files
- `run.sh` : This script is used to stabilize a given video using a reference frame. It sets necessary environment variables and executes the stabilization script with the specified options.

## Commands Used

### 1. Run the stabilization script
This command will run the stabilization process for the given video using the reference frame.
```bash
sh run.sh
```

### 2. Explanation of Parameters
The `run.sh` script uses the following parameters:

- **`--model <Your Model Path>`**: The path to the stabilization model used in the script.
- **`--input <Input Video Path>`**: The path to the input video that needs stabilization.
- **`--output <Output Path>`**: The path where the stabilized video will be saved.
- **`--save`**: Enables saving the stabilized video output.
- **`--no-mask`**: Disables masking during the stabilization process.
