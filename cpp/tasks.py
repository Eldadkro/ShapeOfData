from invoke import task

def concut(values:list[str], sep:str = " "):
    final_command = ""
    for val in values:
        final_command += (val+sep)
    return final_command

@task
def build(c, docs=False):
    command  = "gcc"
    complie_flags = "-fPIC -shared"
    output = "-o libtest.so"
    input_file = "clibarary.c"
    print("compiling", input_file)
    c.run(concut([command,complie_flags,output,input_file]))