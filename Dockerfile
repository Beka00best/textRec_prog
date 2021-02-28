FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git gcc make cmake python3.6 python3-dev python3-pip libgtk-3-dev pkg-config \
    libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libavcodec-dev libavformat-dev libswscale-dev libavresample-dev
RUN pip3 install numpy

# Clone Repos
WORKDIR /opencv
RUN git clone -b '4.5.0' --depth 1 https://github.com/opencv/opencv

# Build openvc with gstreamer support
WORKDIR /build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D INSTALL_C_EXAMPLES=OFF \
    -D PYTHON_EXECUTABLE=$(which python3) \
    -D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") \
    -D PYTHON3_EXECUTABLE=$(which python3) \
    -D PYTHON3_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
    -D PYTHON3_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
    -D WITH_GSTREAMER=ON \
    -D WITH_OPENEXR=OFF \
    -D OPENCV_GENERATE_PKGCONFIG=YES \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_LIST=core,imgcodecs,imgproc,videoio,python3 \
    -D BUILD_SHARED_LIBS=OFF \
    ../opencv
RUN make -j8
RUN make package



ADD program.py /test/program.py

CMD ["python3", "/test/program.py"]