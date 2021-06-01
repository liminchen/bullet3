import subprocess
import string

# first, use genXML.py in rigid-ipc/tools/ to generate MJCF file input for bullet,
# and compile Bullet with different time step sizes (can be modified in line 39 of 
# /Users/minchen/Desktop/bullet3/examples/Importers/ImportMJCFDemo/ImportMJCFSetup.cpp,
# by default dt=0.01s)

# then, run bullet and generate output for visualization
for dt in ['1e-2']:
    # for example in ['tet-corner', 'erleben/cliff-edges', 'erleben/internal-edges', 'erleben/spike-and-wedge', 'erleben/spikes', 'erleben/wedges', 'simple/edge-edge-parallel', 'simple/edge-edge', 'simple/face-vertex', 'simple/vertex-face', 'simple/vertex-vertex']:
    # for example in ['chain/chain-net-16x16-0.1scale', 'chain/chain-net-16x16-0.01scale']:
    # for example in ['chain/chain-net/chain-net-4x4', 'chain/chain-net/chain-net-8x8', 'chain/chain-net/chain-net-16x16']:
    # for example in ['friction/incline-plane/slopeTest_highSchoolPhysics_mu=0.5']:
    # for example in ['friction/arch/arch-101-stones']:
    # for example in ['chain/chain-net/chain-net-16x16-0.1scale']:
    for example in ['mechanisms/bolt']:
        runCommand = 'cp -f ../rigid-ipc/fixtures/3D/' + example + '.xml data/mjcf/hello_mjcf.xml\n' # copy scene file and rename for bullet to load
        runCommand += 'build/examples/ExampleBrowser/App_ExampleBrowser_dt' + dt + '\n' # run bullet, it will automatically load data/mjcf/hello_mjcf.xml

        exampleName = example
        if example.rfind('/') >= 0:
            exampleName = example[(example.rfind('/') + 1):len(example)]
        runCommand += 'cp test.txt output/' + exampleName + '_' + dt + '.txt\n' # copy output (test.txt, stores each bodies SE(3) info in each time step) and save

        # finally, generate obj sequence from bullet output
        runCommand += 'cd ../rigid-ipc\npython genOBJ.py ' + example + ' ../bullet3/output/' + exampleName + '_' + dt + '.txt\n'
        # print(runCommand)
        subprocess.call([runCommand], shell=True)

# generate obj sequence from mujoco output
# for dt in ['1e-2', '1e-3', '1e-4']:
#     # for example in ['tet-corner', 'erleben/cliff-edges', 'erleben/internal-edges', 'erleben/spike-and-wedge', 'erleben/spikes', 'erleben/wedges']:
#     for example in ['friction/incline-plane/slopeTest_highSchoolPhysics_mu=0.5', 'friction/incline-plane/slopeTest_highSchoolPhysics_mu=0.49']:
#     # for example in ['friction/arch/arch-101-stones']:
#         exampleName = example
#         if example.rfind('/') >= 0:
#             exampleName = example[(example.rfind('/') + 1):len(example)]

#         runCommand = 'cd ../rigid-ipc\npython genOBJ.py ' + example + ' ~/Desktop/mujocoResults/output_' + exampleName + '_mjc_' + dt + '.txt\n'
#         # print(runCommand)
#         subprocess.call([runCommand], shell=True)