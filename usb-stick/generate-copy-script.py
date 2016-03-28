import subprocess

drives = ['e', 'f', 'g', 'i', 'j', 'k', 'm', 'n', 'o', 'q']
size = [8 - 1]
source_path = 'd:\\Projects\\ProgKurs\\UsbStick\\ToStick\\'

def exe(args):
    # print args
    return subprocess.Popen(args, stdout=subprocess.PIPE)


def disk_size_in_gb(letter):
    df = exe(["df", "%s:\\" % letter])
    output = df.communicate()[0]
    device, size, used, available, percent, mountpoint = output.split("\n")[1].split()
    return int(size) / 1024 / 1024


def get_format(letter, label='ProgKurs'):
    return ['C:\\Windows\\System32\\format.com', '%s:' % letter, '/Q', '/Y', '/X', '/V:%s' % label]


def get_robocopy(dir, letter):
    return ['C:\\Windows\\System32\\robocopy.exe', '/MIR', dir, '%s:\\' % letter]


def get_removedrive(letter):
    return ['c:\\users\\born\\Programs\\bin\\removedrive.exe', '%s:' % letter]


def log(msg):
    print '[] %s' % msg


print '%i drives are going to be progkursed' % len(drives)

f = open('copy.bat', 'w')
f.write('pause\n')
for drive in drives:
    log('Analyzing drive %s' % drive)
    if disk_size_in_gb(drive) not in size:
        log('Skipping drive %s' % drive)
        continue
    f.write('%s\n' % ' '.join(get_format(drive)))
    f.write('%s\n' % ' '.join(get_robocopy(source_path, drive)))
    f.write('%s\n' % ' '.join(get_removedrive(drive)))
f.close()
