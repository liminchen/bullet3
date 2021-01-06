import subprocess
import string

# first, use genXML.py in ../fixing-collisions to generate MJCF file input for bullet

# then, run bullet
# for dt in ['1e-2', '1e-3', '1e-4']:
for dt in ['1e-2']:
    # for example in ['chain/chain-net-128x128']:
    # for example in ['5-cubes', 'large-mass-ratio', 'screw', 'wrecking-ball', 'chian/10-links']:
    for example in ['chain/10-links']:
        runCommand = 'cp -f ../fixing-collisions/fixtures/3D/' + example + '.xml data/mjcf/hello_mjcf.xml\n'
        runCommand += 'build/examples/ExampleBrowser/App_ExampleBrowser_dt' + dt + '\n'
        exampleName = example
        if example.find('/'):
            exampleName = example[(example.find('/') + 1):len(example)]
        runCommand += 'cp test.txt output_' + exampleName + '_' + dt + '.txt\n'
        subprocess.call([runCommand], shell=True)

# finally, generate obj sequence from bullet output
# for dt in ['1e-2']:
#     for example in ['chain/10-links']:
#         exampleName = example
#         if example.find('/'):
#             exampleName = example[(example.find('/') + 1):len(example)]
#         runCommand = 'cd ../fixing-collisions\npython genOBJ.py ' + example + ' ../bullet3/output_' + exampleName + '_' + dt + '.txt\n'
#         subprocess.call([runCommand], shell=True)