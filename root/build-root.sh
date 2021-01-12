#!/usr/bin/bash

# build root from git source
# https://github.com/root-project/root
#
# rmlm (2019/06/27)

# New build instructions:
# https://root.cern/install/build_from_source/


# change $SRC_DIR to where you want to store the git repo & the build directory
SRC_DIR=$PWD
#ROOT_VERSION=v6-16-00
# note: v6-18-00 is the latest, but I was unable to build it today

GIT_DIR=$SRC_DIR/root
#BUILD_DIR=$SRC_DIR/root_$ROOT_VERSION
BUILD_DIR=$SRC_DIR/build/root
#BUILD_DIR=$GIT_DIR/build

# move to the desired $SRC_DIR
cd $SRC_DIR
echo "cd $SRC_DIR"

# optionally download and move into the git repo
if [ ! -d "$GIT_DIR" ]; then
   git clone https://github.com/root-project/root.git
   echo "git clone https://github.com/root-project/root.git"
fi
cd $GIT_DIR
echo "cd $GIT_DIR"

# make sure we are in the master branch and update the git repo
#git checkout master
git pull --all

# checkout the version we want to build
#git checkout $ROOT_VERSION -b $ROOT_VERSION

# move into the $BUILD_DIR
if [ ! -d "$BUILD_DIR" ]; then
   mkdir $BUILD_DIR
   echo "mkdir $BUILD_DIR"
fi
cd $BUILD_DIR
echo "cd $BUILD_DIR"

# generate the makefiles and build the source code
# an incomplete and out-of-date list of build options can be found here:
# https://root.cern.ch/building-root
#
# some notes on what to include:
# - builtin_llvm must be included (though this may change after v6-12-06)
# - afterimage support must be included (system or builtin)
# - asimage support needs to be on in order to be able to plot things
# - turn off jemalloc as it doesn't play nice with -D CMAKE_VERBOSE_MAKEFILE=ON \pyroot
#
# Option for more verbose makefile output:
# -D CMAKE_VERBOSE_MAKEFILE=ON \
# Idiomatic way to specify c++ standard going forward
# -D CMAKE_CXX_STANDARD=17 \
# -D cxx17=ON \

# alias llvm-config=llvm-config-5.0-64
# alias llvm-cov=llvm-cov-5.0

# cmake-gui $GIT_DIR

# -D afdsmgrd=OFF
# -D afs=OFF
# -D astiff=ON
# -D bonjour=OFF
# -D chirp=OFF
# -D cling=ON
# -D explicitlink=ON
# -D genvector=ON \
# -D hdfs=OFF \
# -D srp=OFF \
# -D xft=ON \
# -D memstat=ON \
# -D python=ON \
# -D vmc=OFF \
# -D CMAKE_CXX_FLAGS_RELEASE="-march=native -O2 -DNDEBUG" \
# -D CMAKE_C_FLAGS_RELEASE="-march=native -O2 -DNDEBUG" \
# -D PYTHON_EXECUTABLE=/usr/bin/python3 \
# -D LLVM_TARGETS_TO_BUILD="host;NVPTX" \
# -D compression_default=zlib \
# -D gcctoolchain=/usr/bin/gcc \
# -D git_executable=/usr/bin/git \
# -D macos_native=OFF \
# -D CMAKE_INSTALL_PREFIX=$BUILD_DIR \
# -D Python2_EXECUTABLE=/usr/bin/python2 \

cmake \
-D CMAKE_BUILD_TYPE=Release \
-D CMAKE_CXX_STANDARD=17 \
-D CMAKE_CXX_COMPILER=/usr/bin/g++ \
-D CMAKE_Fortran_COMPILER=/usr/bin/gfortran \
-D CMAKE_C_COMPILER=/usr/bin/gcc \
-D CMAKE_VERBOSE_MAKEFILE=OFF \
-D CMAKE_MAKE_PROGRAM=/usr/bin/gmake \
-D LLVM_ENABLE_DOXYGEN=ON \
-D LLVM_ENABLE_THREADS=ON \
-D Python3_EXECUTABLE=/usr/bin/python3 \
-D alien=OFF \
-D all=OFF \
-D arrow=OFF \
-D asimage=ON \
-D builtin_afterimage=OFF \
-D builtin_cfitsio=OFF \
-D builtin_clang=ON \
-D builtin_davix=OFF \
-D builtin_fftw3=OFF \
-D builtin_freetype=OFF \
-D builtin_ftgl=OFF \
-D builtin_gl2ps=OFF \
-D builtin_glew=OFF \
-D builtin_gsl=OFF \
-D builtin_llvm=ON \
-D builtin_lz4=OFF \
-D builtin_lzma=OFF \
-D builtin_openssl=OFF \
-D builtin_pcre=OFF \
-D builtin_tbb=OFF \
-D builtin_unuran=OFF \
-D builtin_vc=OFF \
-D builtin_vdt=ON \
-D builtin_veccore=OFF \
-D builtin_xrootd=OFF \
-D builtin_xxhash=OFF \
-D builtin_zlib=OFF \
-D builtin_zstd=OFF \
-D ccache=OFF \
-D cefweb=OFF \
-D clad=ON \
-D clingtest=OFF \
-D cocoa=OFF \
-D coverage=OFF \
-D cuda=OFF \
-D cudnn=OFF \
-D cxxmodules=OFF \
-D dataframe=ON \
-D davix=OFF \
-D dcache=OFF \
-D distcc=OFF \
-D exceptions=ON \
-D fail-on-missing=ON \
-D fcgi=ON \
-D fftw3=ON \
-D fitsio=ON \
-D fortran=ON \
-D gdml=ON \
-D geocad=OFF \
-D gfal=OFF \
-D glite=OFF \
-D globus=OFF \
-D gminimal=OFF \
-D gnuinstall=ON \
-D gsl_shared=ON \
-D gviz=ON \
-D http=ON \
-D imt=ON \
-D jemalloc=OFF \
-D libcxx=OFF \
-D mathmore=ON \
-D memory_termination=OFF \
-D minimal=OFF \
-D minuit2=ON \
-D minuit2_mpi=OFF \
-D minuit2_omp=OFF \
-D mlp=ON \
-D monalisa=OFF \
-D mpi=OFF \
-D mysql=ON \
-D odbc=OFF \
-D opengl=ON \
-D oracle=OFF \
-D pgsql=ON \
-D pyroot=ON \
-D pyroot_experimental=OFF \
-D pythia6=OFF \
-D pythia6_nolink=OFF \
-D pythia8=ON \
-D qt5web=ON \
-D r=OFF \
-D roofit=ON \
-D root7=ON \
-D rootbench=OFF \
-D roottest=OFF \
-D rpath=ON \
-D ruby=OFF \
-D runtime_cxxmodules=OFF \
-D shadowpw=ON \
-D shared=ON \
-D soversion=ON \
-D spectrum=ON \
-D sqlite=ON \
-D ssl=ON \
-D tbb=ON \
-D tcmalloc=OFF \
-D testing=OFF \
-D thread=ON \
-D tmva=ON \
-D tvma-cpu=ON \
-D tvma-gpu=OFF \
-D tvma-pymva=ON \
-D tvma-rmva=OFF \
-D unuran=ON \
-D vc=ON \
-D vdt=OFF \
-D veccore=ON \
-D vecgeom=OFF \
-D webgui=ON \
-D win_broken_tests=OFF \
-D winrtdebug=OFF \
-D x11=ON \
-D xml=ON \
-D xrootd=ON \
$GIT_DIR

# get max num processors
NPROC=`nproc --all`

echo "cmake --build ./ --clean-first --target -- -j$NPROC"
# build the new version
# cmake --build ./ --clean-first -- -j$NPROC
# cmake --build ./ --target -- -j$NPROC
cmake --build ./ --clean-first --target -- -j$NPROC
sudo cmake --build ./ --target install -- -j$NPROC
# cmake --build . --target install




# in v6-16-00, there is a bug in the cmake build scripts that require sudo permissions
# for building clad -> I think it tries to move it to the install location too early!
#sudo cmake --build ./ --clean-first -- -j8

# install the new version
# sudo make install

# update the linker (see /etc/ld.so.conf.d/root.conf)
# sudo echo "/usr/local/lib/root" >> /etc/ld.so.conf.d/root.conf
# ldconfig

# note: you can uninstall an old build by doing
# cd $BUILD_DIR
# sudo xargs rm < install_manifest.txt
