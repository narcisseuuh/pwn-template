import os 
import subprocess

def contains(pattern, content):
    return (len(content.split(pattern)) != 1)

# changing our template to fit the context of the challenge

def change(old, new, content):
    file_to_change = content.split(old)
    new_file = ""
    for i in range(len(file_to_change)):
        new_file += file_to_change[i]
        if i != len(file_to_change) - 1:
            new_file += new 
    return new_file 

def iter_changes(olds, news, content):
    for (old, new) in [(olds[i], news[i]) for i in range(len(olds))]:
        content = change(old, new, content)
    return content

def contains_libc(content, contains = False):
    if not contains:
        new_content = change('libc = ELF(b\'./libc.so.6\')', '', content)
        return new_content
    return content

def modify_template(binary_name, ip, port, contains):
    new_file = ''
    with open('solve.py', 'r') as f:
        content = f.read()
        new_file = iter_changes(['binary', '\'ip\'', 'porto'], [binary_name, '\'' + ip + '\'', port], content)
        new_file = contains_libc(new_file, contains)
    with open('solve_' + binary_name + '.py', 'w') as f:
        f.write(new_file)


def main():
    print("[*] Collecting data for the template generation")
    binary_name = input("select binary name : ")
    ip = input("select ip for the challenge : ")
    port = input("select port for the challenge : ")
    ls_res = subprocess.check_output("ls", shell = True).decode()
    contains_libc = bool(contains('libc.so.6', ls_res))
    print("[+] Data acquired!")

    print("[*] Generating the solve script")
    os.system('touch solve_' + binary_name + '.py')

    modify_template(binary_name, ip, port, contains_libc)

    os.system('rm solve.py')
    print("[+] Solve script generated!")


if __name__ == '__main__':
    main()
