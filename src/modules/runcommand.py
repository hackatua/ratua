import subprocess


def run(**args):
    command = args['command']
    op = subprocess.Popen(command, shell=True,
                          stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    output = op.stdout.read()
    output_error = op.stderr.read()

    if(not output and not output_error):
        return b"Done!"

    return output + output_error
