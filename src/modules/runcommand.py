import subprocess


def run(**args):
    command = args['command']
    op = subprocess.Popen(command, shell=True,
                          stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    output = op.stdout.read().decode() or ""
    output_error = op.stderr.read().decode() or ""

    return {"output": output, "output_error": output_error}
