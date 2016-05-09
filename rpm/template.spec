Name:           ros-kinetic-openhrp3
Version:        3.1.8
Release:        4%{?dist}
Summary:        ROS openhrp3 package

Group:          Development/Libraries
License:        EPL
URL:            https://openrtp.jp/svn/hrg/openhrp/
Source0:        %{name}-%{version}.tar.gz

Requires:       atlas-devel
Requires:       boost-devel
Requires:       collada-dom-devel
Requires:       eigen3-devel
Requires:       f2c
Requires:       f2c-libs
Requires:       jython
Requires:       libjpeg-turbo-devel
Requires:       libpng12-devel
Requires:       libxml2-devel
Requires:       omniORB-devel
Requires:       python-omniORB
Requires:       ros-kinetic-openrtm-aist
BuildRequires:  atlas-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  collada-dom-devel
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  f2c
BuildRequires:  f2c-libs
BuildRequires:  jython
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng12-devel
BuildRequires:  libxml2-devel
BuildRequires:  omniORB-devel
BuildRequires:  pkgconfig
BuildRequires:  python-omniORB
BuildRequires:  ros-kinetic-openrtm-aist

%description
This package does not only wrap OpenHRP3 but actually provides the built
artifact from the code from its mainstream repository. Being ROS-agnostic by
itself, you can also use this via ROS together with the packages in
rtmros_common that bridge between two framework. OpenHRP3 (Open Architecture
Human-centered Robotics Platform version 3) is an integrated software platform
for robot simulations and software developments. It allows the users to inspect
an original robot model and control program by dynamics simulation. In addition,
OpenHRP3 provides various software components and calculation libraries that can
be used for robotics related software developments (excerpts from here). The
package version number is synchronized to that of mainstream, based on this
decision.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue May 10 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.8-4
- Autogenerated by Bloom

* Sat May 07 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.8-3
- Autogenerated by Bloom

* Thu May 05 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.8-2
- Autogenerated by Bloom

* Wed May 04 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.8-1
- Autogenerated by Bloom

* Fri Apr 22 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.1.8-0
- Autogenerated by Bloom

