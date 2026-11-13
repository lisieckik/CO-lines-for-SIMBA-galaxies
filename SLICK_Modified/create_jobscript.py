import pathlib


def create_jobscript(param_filename, param_file,runName = 'slickRun', nNodes = 1, logName = 'slickOut',ncores = 32):

    with open("slick_run_jobscript.sh", "w") as f:
        f.write("#!/bin/bash\n#SBATCH -J=%s"%runName+
                "\n#SBATCH --nodes=%s"%nNodes+
                "\n#SBATCH --output=%s"%logName+
                "_%A_%a.log"+
                "\n#SBATCH --array=1-%i"%(ncores)+
                "\n#SBATCH	--ntasks=1"
                "\n#SBATCH --qos=interq"
                "\n#SBATCH -p INTEL_IVY,INTEL_CASCADE,INTEL_SKYLAKE,INTEL_HASWELL"
                )
        f.write(
            "\n"
            "\nmodule purge"
            "\nsource /mnt/opt/spack/0.20/share/spack/setup-env.sh"
            "\nmodule load gcc-8.5.0-gcc-8.5.0-3ldkfvy"
            "\nmodule load gsl-2.7-gcc-8.3.0-xyhguff"
            "\nsource /mnt/home/share/simbas/miniconda3/etc/profile.d/conda.sh"
            "\nconda activate /mnt/home/share/simbas/miniconda3/envs/slick/"
        )
        f.write(
            f"\nslick run --parameters {param_file} --cloudinfofile {param_filename} --cloudinfoline $SLURM_ARRAY_TASK_ID\n"
        )
