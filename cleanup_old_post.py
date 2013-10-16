import os
import sys


def check(fname):
    content = []

    for i, line in enumerate(open(fname)):
        if '###' in line:
            head = '=' * (len(line) + 1) + '\n'
            content.insert(0, head)
            content[i] = ' ' + content[i]
            content.append(head)
        elif len(line) < 70 and line.endswith('.\n'):
            content.append(line)
            content.append('\n')
        else:
            content.append(line)

    fixed_content = ''.join(content)
    print('>>> START')
    print(fixed_content)
    print('<<< END')
    fix = raw_input('How does it look? ')
    if fix == 'y':
        open(fname, 'w').write(fixed_content)


def run(dirname):
    for root, dirs, files in os.walk(dirname):
        if files and files[0].endswith('.rst'):
            check(os.path.join(root, files[0]))

if __name__ == '__main__':
    run(sys.argv[1])
