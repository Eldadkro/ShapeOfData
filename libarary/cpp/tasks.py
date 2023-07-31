from invoke import task

def concut(values:list[str], sep:str = " "):
    final_command = ""
    for val in values:
        final_command += (val+sep)
    return final_command

@task
def build(c, docs=False):
    command  = "g++"
    complie_flags = " -fPIC -shared -fdiagnostics-color=always"
    output = "-o libinvarientscpp.so"
    input_file = "invarientscpp.cpp"
    print("compiling", input_file)
    c.run(concut([command,complie_flags,output,input_file]))


@task
def test(c):
    c.run("export LD_LIBRARY_PATH=\"$PWD:$LD_LIBRARY_PATH\"")
    build(c)
    command  = "g++"
    complie_flags = "-c -g -fdiagnostics-color=always"
    output = "-o libinvarientscpp.o"
    input_file = "invarientscpp.cpp"
    print("compiling", input_file)
    c.run(concut([command,complie_flags,output,input_file]))
    
    command  = "g++"
    complie_flags = " -c -g -fdiagnostics-color=always"
    output = "-o main.o"
    input_file = "main.cpp"
    print("compiling", input_file)
    c.run(concut([command,complie_flags,output,input_file]))
    command  = "g++"
    complie_flags = " -fdiagnostics-color=always -pthread  -L. "
    output = "-o main"
    input_file = "main.o libinvarientscpp.o"
    print("linking: ", input_file)
    c.run(concut([command,complie_flags,output,input_file]))


